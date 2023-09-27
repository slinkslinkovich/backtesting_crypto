import pytz
from history import get_all_klines_data
from datetime import datetime
import sys

sys.setrecursionlimit(99999)

start_time = "2020-01-01"
end_time = "2024-07-03"
symbol = "BTCUSDT" # Пара по которой тянем данные
interval = "1h" # Интервал
spot = False # True если брать спотовый график и False если фючерсный
allocated_amount = 100 # $$$$$
comis = 0.04
not_use_stop_take = True # Не используем стопы и тейки
stop_loss = -100 # Стоплос на будущее
take_profit = 100 # Тейкпрофит на будущее
reverse = False # реверсивная система


# Настройки MCAD
# short_period = 12
# long_period = 26
# signal_period = 9



data = get_all_klines_data(symbol, interval, start_time, end_time, spot)


def get_datatime(timestamp, timezone='Europe/Kiev'):
    tz = pytz.timezone(timezone)
    date = datetime.fromtimestamp(timestamp / 1000, tz)
    return date


def calculate_ema(data, period):
    if len(data) > period:
        last_ema = 0
        alpha = 2 / (period + 1)
        ema = sum(data[:period]) / period

        for i in range(period, len(data)):
            last_ema = alpha * data[i] + (1 - alpha) * ema
            ema = last_ema

        return last_ema


def calculate_macd(data, short_period, long_period, signal_period):
    data = data[-200:]
    closing_prices = [float(entry[4]) for entry in data]  # Закрытие свечи
    macd_line = []
    #print(closing_prices)
    for i in range(1, len(closing_prices)-long_period): # Если поставить range(0, то будет показывать текущее значение
        if i == 0:
            prices = closing_prices
        else:
            prices = closing_prices[:-i]
        #print(prices)
        # Вычисляем EMA для короткого периода (обычно 12)
        ema_short = calculate_ema(prices, short_period)
        # Вычисляем EMA для длинного периода (обычно 26)
        ema_long = calculate_ema(prices, long_period)
        # Вычисляем линию MACD (разница между EMA(12) и EMA(26))
        macd_line.append(ema_short - ema_long)
    macd_line.reverse()
    #print(macd_line)

    # Вычисляем Signal Line для линии MACD (обычно 9)
    macd_signal = calculate_ema(macd_line, signal_period)
    # Вычисляем Histogram
    histogram = macd_line[-1]-macd_signal

    return round(macd_line[-1], 2), round(macd_signal, 2), round(histogram, 2)


# Функция которая считает открытые позиции
def checker_opened_position(direction, positions):
    count = 0
    for i in positions:
        if i['Direction'] == direction and i['Status'] == 0:
            count += 1
    return count


def checker_opened_index(direction, positions):
    index = 0
    for i in positions:
        #print(i)
        if i['Direction'] == direction and i['Status'] == 0:
            return index
        index += 1


def convert_to_percentage(value, reference):
    if reference == 0:
        return 0
    return round((value / reference) * 100, 2)


def check_hilo_price(start, end, data=data):
    min = float('inf')
    max = float('-inf')
    hi_counter, lo_counter = float('inf'), float('inf')
    calc = 0
    #print(len(data))
    for i in data:
        if i[0] == end:
            return min, max, lo_counter, hi_counter

        #print(i[0], start, end)
        if i[0] == start:
            calc = 1
        if calc == 1:
            #print(i[0], get_datatime(i[0]), start, end, i[2], i[3])
            if float(i[2]) >= max:
                max = float(i[2])
                hi_counter = i[0]
            if float(i[3]) <= min:
                min = float(i[3])
                lo_counter = i[0]



# Функция для записи данных в ексель файл
def save_trades_to_csv(data, symbol, interval, reverse):
    import csv
    reverse_str = 'Реверсивное' if reverse else 'Обычное'
    namefile = symbol + '_' + interval + '_' + reverse_str + '.csv' # Определите заголовки столбцов
    fieldnames = list(data[0].keys())
    with open(namefile, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')

        writer.writeheader() # Запишите заголовки столбцов
        for row in data: # Запишите каждую строку данных
            # if row['Profit/Loss'] == 0 and row['Status'] == 1: # !!! V2
            #     continue
            writer.writerow(row)
    print(f"Данные успешно записаны в файл {namefile}")

# save_trades_to_csv(trades, symbol, interval, reverse) # Вызов функции


# Функция для записи итоговых данных
def save_total_to_csv(data, symbol, interval, reverse, short, long, signal):
    import csv
    reverse_str = 'Реверсивное' if reverse else 'Обычное'
    namefile = symbol + '_' + interval + '_' + reverse_str + '_total.csv' # Определите заголовки столбцов
    grouped_data = []
    counter, negative_counts = 0, [0]
    prev_month = None  # Следим за предыдущим месяцем
    for entry in data:
        # if entry['Profit/Loss'] == 0:
        #     continue

        if isinstance(entry['Time'], datetime):
            month = entry['Time'].strftime('%Y-%m')
        else:
            month = datetime.strptime(entry['Time'], '%Y-%m-%d %H:%M:%S').strftime('%Y-%m')

        if month != prev_month:
            counter = 0
            negative_counts = [0]
            prev_month = month

        existing_entry = next((x for x in grouped_data if x['Month'] == month), None)
        if existing_entry:
            existing_entry['Total Trades'] += 1
            existing_entry['Total Sum'] += entry['Profit/Loss']
            if entry['Profit/Loss'] < 0:
                counter += 1
                existing_entry['Negative Trades'] += 1
                existing_entry['Negative Sum'] += entry['Profit/Loss']
            else:
                counter = 0
                existing_entry['Positive Trades'] += 1
                existing_entry['Positive Sum'] += entry['Profit/Loss']

            negative_counts.append(counter)
            existing_entry['Max Negative Trades'] = max(negative_counts)
            #print(counter, max(negative_counts), negative_counts,  entry)
            existing_entry['Winrate'] = round(existing_entry['Positive Trades']/existing_entry['Total Trades']*100, 2)
        else:
            new_entry = {
                'Month': month,
                'Total Trades': 1,
                'Total Sum': entry['Profit/Loss'],
                'Winrate': 0,
                'Max Negative Trades': 1 if entry['Profit/Loss'] < 0 else 0,
                'Negative Trades': 1 if entry['Profit/Loss'] < 0 else 0,
                'Negative Sum': entry['Profit/Loss'] if entry['Profit/Loss'] < 0 else 0,
                'Positive Trades': 0 if entry['Profit/Loss'] < 0 else 1,
                'Positive Sum': 0 if entry['Profit/Loss'] < 0 else entry['Profit/Loss'],
                "MACD": str(short) +','+ str(long) +','+ str(signal)
            }
            grouped_data.append(new_entry)

    fieldnames = list(grouped_data[0].keys())


    with open(namefile, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')

        writer.writeheader() # Запишите заголовки столбцов
        for row in grouped_data: # Запишите каждую строку данных
            writer.writerow(row)
    print(f"Данные успешно записаны в файл {namefile}")

# save_total_to_csv(trades, symbol, interval, reverse)

# Функция для записи итоговых данных
def save_total_to_csv(data, symbol, interval, reverse, short, long, signal):
    import csv

    reverse_str = 'Реверсивное' if reverse else 'Обычное'
    namefile = symbol + '_' + interval + '_' + reverse_str + '_total.csv'

    total_trades, total_sum, negative_trades, negative_sum = 0, 0, 0, 0
    positive_trades, positive_sum, max_negative_trades = 0, 0, 0
    counter, negative_counts = 0, [0]

    for entry in data:
        # if entry['Profit/Loss'] == 0:
        #     continue

        total_trades += 1
        total_sum += entry['Profit/Loss']

        if entry['Profit/Loss'] < 0:
            counter += 1
            negative_trades += 1
            negative_sum += entry['Profit/Loss']

        else:
            counter = 0
            positive_trades += 1
            positive_sum += entry['Profit/Loss']

        negative_counts.append(counter)
        max_negative_trades = max(negative_counts)

    winrate = round(positive_trades / total_trades * 100, 2)

    header = ['Total Trades', 'Total Sum', 'Winrate', 'Max Negative Trades',
              'Negative Trades', 'Negative Sum', 'Positive Trades',
              'Positive Sum', 'MACD']

    row = [total_trades, total_sum, winrate, max_negative_trades,
           negative_trades, negative_sum, positive_trades,
           positive_sum, f"{short},{long},{signal}"]

    with open(namefile, mode='a', newline='') as file:
        writer = csv.writer(file, delimiter=';')

        if file.tell() == 0:
            writer.writerow(header)
        writer.writerow(row)

    print(f"Данные успешно записаны в файл {namefile}")

def check_strategy(data, symbol, interval, short_period, long_period, signal_period):

    # Переменные для работы
    trades = []
    prev_macd_line, prev_macd_signal, prev_histogram = 0, 0, 0

    def record_trade(direction, index, allocated_amount, volume, open_price, time, histogram, short, long, signal):
        trade = {
            "Direction": direction,
            "Index": index,
            "Amount": allocated_amount,
            "Volume": volume,
            "Open Price": open_price,
            "Close Price": 0,
            "What First": 0,
            "Max Drawdown": 0,
            "Max Growth": 0,
            "Profit/Loss": 0,
            "Status": 0,
            "Time": time,
            "Exit": '',
            "Histogram": histogram,
            "Setup" : str(short) + ',' + str(long) + ',' + str(signal)
        }
        trades.append(trade)

    for i in range(len(data)):
        if i < 200:
            continue

        macd_line, macd_signal, histogram = calculate_macd(data[:i], short_period, long_period, signal_period)
        current_time = get_datatime(data[:i][-1][0])
        if i == 200:
            prev_macd_line, prev_macd_signal, prev_histogram = macd_line, macd_signal, histogram
            continue

        if prev_histogram < 0 and histogram > 0 and checker_opened_position("Long", trades) == 0:
            print(current_time, 'LONG', macd_line, macd_signal, histogram)

            # ТУТ ПРОДАЕМ ПРОТИВОПОЛОЖНЫЙ СИГНАЛ
            if checker_opened_position("Short", trades) > 0:
                start_index = checker_opened_index("Short", trades)
                close_index = data[:i][-1][0]
                open_price = float(data[:i][-1][1])
                cur_max_price = float(data[:i][-1][2])
                cur_lo_price = float(data[:i][-1][3])
                close = False

                if trades[start_index]["Direction"] == "Short":
                    percentage_max = convert_to_percentage(trades[start_index]['Open Price'] - cur_max_price,
                                                           trades[start_index]['Open Price'])
                    percentage_lo = convert_to_percentage(trades[start_index]['Open Price'] - cur_lo_price,
                                                          trades[start_index]['Open Price'])

                    if not_use_stop_take:
                        trades[start_index]['Profit/Loss'] = convert_to_percentage(
                            trades[start_index]['Open Price'] - open_price,
                            trades[start_index]['Open Price'])
                        trades[start_index]["Close Price"] = open_price
                        lo_price, hi_price, lo_counter, hi_counter = check_hilo_price(trades[start_index]['Index'],
                                                                                      close_index)
                        close = True
                    if percentage_max <= stop_loss:
                        trades[start_index]["Profit/Loss"] = stop_loss - comis
                        lo_price, hi_price, lo_counter, hi_counter = check_hilo_price(trades[start_index]['Index'],
                                                                                      close_index)
                        trades[start_index]["Close Price"] = trades[start_index]['Open Price'] + (
                                trades[start_index]['Open Price'] * stop_loss / 100)
                        close = True
                    if percentage_lo >= take_profit:
                        trades[start_index]["Profit/Loss"] = take_profit - comis
                        lo_price, hi_price, lo_counter, hi_counter = check_hilo_price(trades[start_index]['Index'],
                                                                                      close_index)
                        trades[start_index]["Close Price"] = trades[start_index]['Open Price'] + (
                                trades[start_index]['Open Price'] * take_profit / 100)
                        close = True

                    if close:
                        trades[start_index]['Max Drawdown'] = convert_to_percentage(
                            hi_price - trades[start_index]['Open Price'], trades[start_index]['Open Price']) * -1
                        trades[start_index]['Max Growth'] = convert_to_percentage(
                            lo_price - trades[start_index]['Open Price'], trades[start_index]['Open Price']) * -1

                        if hi_counter < lo_counter:
                            if hi_counter != trades[start_index]['Index']:
                                trades[start_index]['What First'] = 'Просадка'
                            else:
                                trades[start_index]['What First'] = 'Рост'
                        if lo_counter < hi_counter:
                            if lo_counter != trades[start_index]['Index']:
                                trades[start_index]['What First'] = 'Рост'
                            else:
                                trades[start_index]['What First'] = 'Просадка'

                        trades[start_index]["Status"] = 1
                        trades[start_index]["Exit"] = current_time

            # ТУТ ПОКУПАЕМ ТЕКУЩИЙ СИГНАЛ
            direction = "Long"
            index = data[:i][-1][0]
            open_price = float(data[:i][-1][1])
            volume = allocated_amount / open_price
            record_trade(direction, index, allocated_amount, volume, open_price, current_time, histogram, short, long, signal)

        if prev_histogram > 0 and histogram < 0 and checker_opened_position("Short", trades) == 0:
            print(current_time, 'SHORT', macd_line, macd_signal, histogram)

            # ТУТ ПРОДАЕМ ПРОТИВОПОЛОЖНЫЙ СИГНАЛ
            if checker_opened_position("Long", trades) > 0:
                start_index = checker_opened_index("Long", trades)
                close_index = data[:i][-1][0]
                open_price = float(data[:i][-1][1])
                cur_max_price = float(data[:i][-1][2])
                cur_lo_price = float(data[:i][-1][3])
                close = False

                if trades[start_index]["Direction"] == "Long":
                    percentage_max = convert_to_percentage(cur_max_price - trades[start_index]['Open Price'],
                                                           trades[start_index]['Open Price'])
                    percentage_lo = convert_to_percentage(cur_lo_price - trades[start_index]['Open Price'],
                                                          trades[start_index]['Open Price'])

                    if not_use_stop_take:
                        trades[start_index]['Profit/Loss'] = convert_to_percentage(
                            open_price - trades[start_index]['Open Price'],
                            trades[start_index]['Open Price'])
                        trades[start_index]["Close Price"] = open_price
                        lo_price, hi_price, lo_counter, hi_counter = check_hilo_price(trades[start_index]['Index'],
                                                                                      close_index)
                        close = True
                    if percentage_lo <= stop_loss:
                        trades[start_index]["Profit/Loss"] = stop_loss - comis
                        lo_price, hi_price, lo_counter, hi_counter = check_hilo_price(trades[start_index]['Index'],
                                                                                      close_index)
                        trades[start_index]["Close Price"] = trades[start_index]['Open Price'] + (
                                trades[start_index]['Open Price'] * stop_loss / 100)
                        close = True
                    if percentage_max >= take_profit:
                        trades[start_index]["Profit/Loss"] = take_profit - comis
                        lo_price, hi_price, lo_counter, hi_counter = check_hilo_price(trades[start_index]['Index'],
                                                                                      close_index)
                        trades[start_index]["Close Price"] = trades[start_index]['Open Price'] + (
                                trades[start_index]['Open Price'] * take_profit / 100)
                        close = True

                    if close:
                        trades[start_index]['Max Drawdown'] = convert_to_percentage(
                            lo_price - trades[start_index]['Open Price'], trades[start_index]['Open Price'])
                        trades[start_index]['Max Growth'] = convert_to_percentage(
                            hi_price - trades[start_index]['Open Price'], trades[start_index]['Open Price'])

                        if hi_counter < lo_counter:
                            if hi_counter != trades[start_index]['Index']:
                                trades[start_index]['What First'] = 'Рост'
                            else:
                                trades[start_index]['What First'] = 'Просадка'
                        if lo_counter < hi_counter:
                            if lo_counter != trades[start_index]['Index']:
                                trades[start_index]['What First'] = 'Просадка'
                            else:
                                trades[start_index]['What First'] = 'Рост'

                        trades[start_index]["Status"] = 1
                        trades[start_index]["Exit"] = current_time

            # ТУТ ПОКУПАЕМ ТЕКУЩИЙ СИГНАЛ
            direction = "Short"
            index = data[:i][-1][0]
            open_price = float(data[:i][-1][1])
            volume = allocated_amount / open_price
            record_trade(direction, index, allocated_amount, volume, open_price, current_time, histogram, short, long, signal)

        prev_macd_line, prev_macd_signal, prev_histogram = macd_line, macd_signal, histogram

    try:
        save_trades_to_csv(trades, symbol, interval, reverse)
        save_total_to_csv(trades, symbol, interval, reverse, short, long, signal)
    except Exception as e:
        print('Нечего записать', e)


spisok_short_period = [*range(5, 55, 5)]
spisok_long_period = [*range(10, 65, 5)]
spisok_signal_period = [*range(5, 45, 5)]

spisok_short_period = [20]
spisok_long_period = [50]
spisok_signal_period = [10]

for short in spisok_short_period:
    short_period = short
    for long in spisok_long_period:
        long_period = long
        for signal in spisok_signal_period:
            signal_period = signal
            if short_period >= long_period: # убираем бредок который никогда не будет работать
                continue
            print(short_period, long_period, signal_period)
            check_strategy(data, symbol, interval, short_period, long_period, signal_period)



