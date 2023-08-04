import pandas as pd
import math

length_rsi = 14
over_sold_start = 30
over_bought_start = 70

size = 100
depo = 1000
last_long_price = 0
last_short_price = 0
last_depo = depo
max_depo = depo
min_depo = depo
max_drawdown = 0
max_growth = 0

last_depo_deal = size
max_depo_deal = size
min_depo_deal = size
max_drawdown_deal = 0
max_growth_deal = 0
dd_last = 0
gr_last = 0
first = 0


def init_variables_deal():
    global size, last_depo_deal, max_depo_deal, min_depo_deal, max_drawdown_deal, max_growth_deal, dd_last, gr_last

    last_depo_deal = size
    max_depo_deal = size
    min_depo_deal = size
    max_drawdown_deal = 0
    max_growth_deal = 0
    dd_last = 0
    gr_last = 0


def init_variables():
    global size, depo, last_long_price, last_short_price, last_depo, max_depo, min_depo, max_drawdown, max_growth

    size = 100
    depo = 1000
    last_long_price = 0
    last_short_price = 0
    last_depo = depo
    max_depo = depo
    min_depo = depo
    max_drawdown = 0
    max_growth = 0


def read_data_csv(file_name='data\BTCUSDT_data_1d.csv'):
    data = pd.read_csv(file_name)
    df_csv = pd.DataFrame(data, columns=['Datetime', 'Open', 'High', 'Low', 'Close'])
    return df_csv


def save_data_csv(df_res, file_name='RESULT_RSI.csv'):
    df_res.to_csv(file_name, index=False)


def calculate_rsi(df, rsi_source='Close', length=14):
    delta = df[rsi_source].diff()
    gains = delta.where(delta > 0, 0)
    losses = -delta.where(delta < 0, 0)

    alpha = 1 / length
    gain_smoothing = gains.ewm(alpha=alpha, adjust=False).mean()
    loss_smoothing = losses.ewm(alpha=alpha, adjust=False).mean()

    rs = gain_smoothing / loss_smoothing
    rsi = 100 - (100 / (1 + rs))

    df['RSI'] = rsi
    # Cut off the extreme values of the extrema
    df.loc[(df['RSI'] == 100) & (df.index < 50), 'RSI'] = 50
    return df


def mark_long_short(df, source='Close', over_sold=30, over_bought=70):
    price_current = df[source]
    rsi = df['RSI']
    price_long = price_current.where((rsi > over_sold) & (rsi.shift(1) <= over_sold), 0)
    price_short = price_current.where((rsi < over_bought) & (rsi.shift(1) >= over_bought), 0)

    df['mark_long'] = 1
    df['mark_short'] = 1

    m_long = df['mark_long']
    m_short = df['mark_short']

    mark_long = m_long.where(price_long > 0, 0)
    mark_short = m_short.where(price_short > 0, 0)

    df['mark_long'] = mark_long
    df['mark_short'] = mark_short

    df['price_long'] = price_long
    df['price_short'] = price_short

    df['deal_cur'] = 0

    # Look for indexes when 'price_long' and 'price_short' are greater than 0
    price_long_gt_0 = df['price_long'].gt(0)
    price_short_gt_0 = df['price_short'].gt(0)

    # Find the moments of transition to a long position
    df.loc[price_long_gt_0 & (df['deal_cur'].shift(1) != 1), 'deal_cur'] = 1

    # Find the moments of going short
    df.loc[price_short_gt_0 & (df['deal_cur'].shift(1) != -1), 'deal_cur'] = -1

    # Fill in the gaps in 'deal_cur' with values from previous non-zero values
    df['deal_cur'] = df['deal_cur'].replace(0, method='ffill')

    df['price_long'] = df['price_long'].where((df['price_long'] > 0) & (df['deal_cur'].shift(1) != 1), 0)
    df['price_short'] = df['price_short'].where((df['price_short'] > 0) & (df['deal_cur'].shift(1) != -1), 0)

    df['deal_long'] = 1
    df['deal_short'] = 1

    df['deal_long'] = df['deal_long'].where((df['deal_cur'] == 1) & (df['deal_cur'].shift(1) == -1), 0)
    df['deal_short'] = df['deal_short'].where((df['deal_cur'] == -1) & (df['deal_cur'].shift(1) == 1), 0)
    return df


def fill_price_open_long(row):
    global last_long_price
    # print(row)
    if row['price_long'] > 0:
        last_long_price = row['price_long']

    if row['deal_cur'] == 1 and row['price_long'] == 0:
        return last_long_price
    else:
        return row['price_long']


def fill_price_open_short(row):
    global last_short_price
    # print(row)
    if row['price_short'] > 0:
        last_short_price = row['price_short']

    if row['deal_cur'] == -1 and row['price_short'] == 0:
        return last_short_price
    else:
        return row['price_short']


def create_deal_long(df):
    df['price_open_long'] = 0
    df['price_open_long'] = df.apply(lambda row: fill_price_open_long(row), axis=1)
    df.loc[df['deal_cur'] == 1, 'profit_long'] = df['Close'] - df['price_open_long']
    return df


def create_deal_short(df):
    df['price_open_short'] = 0
    df['price_open_short'] = df.apply(lambda row: fill_price_open_short(row), axis=1)
    df.loc[df['deal_cur'] == -1, 'profit_short'] = df['price_open_short'] - df['Close']
    return df

def calc_profit_long_close(df):
    df['profit_long_close'] = 0
    df.loc[(df['price_short'] > 0) & (df['deal_cur'].shift(1) != 0), 'profit_long_close'] = df['price_short'] - df['price_open_long'].shift(1)
    return df


def calc_profit_short_close(df):
    df['profit_short_close'] = 0
    df.loc[(df['price_long'] > 0) & (df['deal_cur'].shift(1) != 0), 'profit_short_close'] = df['price_open_short'].shift(1) - df['price_long']
    return df


def calc_amount_long(df, size):
    df['amount_long'] = 0
    df['am_profit_long'] = 0
    df.loc[df['price_open_long'] > 0, 'amount_long'] = size / df['price_open_long']
    df.loc[df['amount_long'] > 0, 'am_profit_long'] = df['amount_long'] * df['profit_long']
    df.loc[df['profit_long_close'] != 0, 'am_profit_long'] = df['amount_long'].shift(1) * df['profit_long_close']
    return df


def calc_amount_short(df, size):
    df['amount_short'] = 0
    df['am_profit_short'] = 0
    df.loc[df['price_open_short'] > 0, 'amount_short'] = size / df['price_open_short']
    df.loc[df['amount_short'] > 0, 'am_profit_short'] = df['amount_short'] * df['profit_short']
    df.loc[df['profit_short_close'] != 0, 'am_profit_short'] = df['amount_short'].shift(1) * df['profit_short_close']
    return df


def calc_am_profit_long_close(df):
    df['am_profit_long_close'] = 0
    df.loc[df['profit_long_close'] != 0, 'am_profit_long_close'] = df['am_profit_long']
    return df


def calc_am_profit_short_close(df):
    df['am_profit_short_close'] = 0
    df.loc[df['profit_short_close'] != 0, 'am_profit_short_close'] = df['am_profit_short']
    return df


def calc_depo(row):
    global last_depo, max_depo, max_drawdown, min_depo, max_growth

    last_depo = last_depo + (row['am_profit_long_close'] + row['am_profit_short_close'])
    # Calculate the maximum drawdown on the deposit
    if last_depo > max_depo:
        max_depo = last_depo
    drawdown = max_depo - last_depo

    if drawdown > max_drawdown:
        max_drawdown = drawdown
    # Calculate the maximum deposit growth
    if last_depo < min_depo:
        min_depo = last_depo
    growth = last_depo - min_depo

    if growth > max_growth:
        max_growth = growth

    return last_depo


def create_depo(df):
    df.loc[(df['am_profit_long_close'] != 0) | (df['am_profit_short_close'] != 0), 'depo'] = df.apply(lambda row: calc_depo(row), axis=1)
    return df


def calc_deal_max_dd_gr(row):
    global size, last_depo_deal, max_depo_deal, max_drawdown_deal, min_depo_deal, max_growth_deal, dd_last, gr_last, first

    str_dd_gr = ''

    last_depo_deal = (row['am_profit_long'] + row['am_profit_short']) + size
    # Calculate the maximum drawdown on the deal
    if last_depo_deal > max_depo_deal:
        max_depo_deal = last_depo_deal

    drawdown_deal = max_depo_deal - last_depo_deal

    if drawdown_deal > max_drawdown_deal:
        max_drawdown_deal = drawdown_deal
        dd_last = 1

    # Calculate the maximum gain on the deal
    if last_depo_deal < min_depo_deal:
        min_depo_deal = last_depo_deal

    growth_deal = last_depo_deal - min_depo_deal

    if growth_deal > max_growth_deal:
        max_growth_deal = growth_deal
        dd_last = 0


    if not math.isnan(row['depo']) and row['depo'] > 0:
        str_dd = round(max_drawdown_deal, 2)
        str_gr = round(max_growth_deal, 2)

        if dd_last == 1:
            first = 1
        elif dd_last == 0:
            first = -1

        str_dd_gr = f'{str_dd}_{str_gr}_{first}'

        init_variables_deal()

    return str_dd_gr


def create_maxdd_maxgr_deal(df):
    df['max_dd_gr'] = ''

    df.loc[(df['am_profit_long'] != 0) | (df['am_profit_short'] != 0), 'max_dd_gr'] = df.apply(lambda row: calc_deal_max_dd_gr(row), axis=1)

    return df

def split_dd_gr(row, pos):
    if row['max_dd_gr']:
        parts = row['max_dd_gr'].split('_')
        if len(parts) > pos:
            return float(parts[pos])
    return 0.0




def split_str_max_dd_gr(df):
    df['max_dd'] = 0.0
    df['max_gr'] = 0.0
    df['first'] = 0
    df.loc[(df['max_dd_gr'] != ''), 'max_dd'] = df.apply(lambda row: split_dd_gr(row, 0), axis=1)
    df.loc[(df['max_dd_gr'] != ''), 'max_gr'] = df.apply(lambda row: split_dd_gr(row, 1), axis=1)
    df.loc[(df['max_dd_gr'] != ''), 'first'] = df.apply(lambda row: split_dd_gr(row, 2), axis=1)

    return df



def create_df_res():
    df_r = pd.DataFrame(columns=['Rsi_limit', 'Count_deal', 'Max_growth_deal', 'Max_drawdown_deal',
                                 'Max_growth_depo', 'Max_drawdown_depo', 'Avg_profit_deal', 'Avg_loss_deal', 'Winrate'])

    return df_r


def add_res(df_res, Rsi_limit, Count_deal, Max_growth_deal, Max_drawdown_deal, Max_growth_depo, Max_drawdown_depo,
            Avg_profit_deal, Avg_loss_deal, Winrate):

    new_res_str = {'Rsi_limit': Rsi_limit, 'Count_deal': Count_deal, 'Max_growth_deal': Max_growth_deal,
                   'Max_drawdown_deal': Max_drawdown_deal, 'Max_growth_depo': Max_growth_depo,
                   'Max_drawdown_depo': Max_drawdown_depo, 'Avg_profit_deal': Avg_profit_deal,
                   'Avg_loss_deal': Avg_loss_deal, 'Winrate': Winrate}
    df_res = df_res.append(new_res_str, ignore_index=True)

    return df_res

def create_df_deals():

    df_deals = pd.DataFrame(columns=['Datetime_open', 'Datetime_close', 'Direction', 'Open_price', 'Close_price', 'Amount',
                                 'Max_growth_deal', 'Max_drawdown_deal', 'First', 'Profit'])

    return df_deals


# def add_deals(df_d, df):
#     df_d = df.loc[(df['am_profit_long_close'] != 0) | (df['am_profit_short_close'] != 0)]
#
#     return df_d

def add_deal(df_deals, datetime_open, datetime_close, direction, open_price, close_price, amount, max_growth_deal, max_drawdown_deal, first, profit):

    new_deal_str = {'Datetime_open': datetime_open, 'Datetime_close': datetime_close, 'Direction': direction, 'Open_price': open_price,
                    'Close_price': close_price, 'Amount': amount,'Max_growth_deal': max_growth_deal,
                    'Max_drawdown_deal': max_drawdown_deal, 'First': first, 'Profit': profit}
    df_deals = df_deals.append(new_deal_str, ignore_index=True)

    return df_deals


def add_deals(df, df_deals):
    for index, deal_row in df.iterrows():
        if deal_row['price_long'] > 0 or deal_row['price_short'] > 0:
            Datetime_open_prev = deal_row['Datetime']
            Open_price_prev = deal_row['price_long'] + deal_row['price_short']
            if deal_row['deal_cur'] == 1:
                Direction_prev = 'Long'
            elif deal_row['deal_cur'] == -1:
                Direction_prev = 'Short'
            Amount_prev = deal_row['amount_long'] + deal_row['amount_short']
            break

    for index, deal_row in df.iterrows():
        if deal_row['depo'] > 0:
            Datetime_open = Datetime_open_prev
            Datetime_close = deal_row['Datetime']
            Direction = Direction_prev
            Open_price = Open_price_prev
            Close_price = deal_row['Close']
            Amount = Amount_prev
            Max_growth_deal = deal_row['max_gr']
            Max_drawdown_deal = deal_row['max_dd']
            First = deal_row['first']
            Profit = deal_row['am_profit_long_close'] + deal_row['am_profit_short_close']

            df_deals = add_deal(df_deals, Datetime_open, Datetime_close, Direction, Open_price, Close_price, Amount, Max_growth_deal, Max_drawdown_deal, First, Profit)

            Datetime_open_prev = deal_row['Datetime']
            Open_price_prev = deal_row['price_long'] + deal_row['price_short']
            if deal_row['deal_cur'] == 1:
                Direction_prev = 'Long'
            elif deal_row['deal_cur'] == -1:
                Direction_prev = 'Short'
            Amount_prev = deal_row['amount_long'] + deal_row['amount_short']

    return df_deals


def calc_print_stat_amount(df, str_limit_rsi, df_res):
    count_long_cross_rsi = df['mark_long'].sum()
    count_short_cross_rsi = df['mark_short'].sum()
    count_long_deal = df['deal_long'].sum()
    count_short_deal = df['deal_short'].sum()
    count_deal = df['deal_long'].sum() + df['deal_short'].sum()

    # LONG statistics
    am_profit_long_close = round(df['am_profit_long_close'].sum(), 2)
    am_profit_long_close_plus = round(df.loc[df['am_profit_long_close'] >= 0, 'am_profit_long_close'].sum(), 2)
    am_profit_long_close_minus = round(df.loc[df['am_profit_long_close'] < 0, 'am_profit_long_close'].sum(), 2)
    am_count_long_profit = df.loc[df['am_profit_long_close'] > 0, 'am_profit_long_close'].count()
    am_count_long_loss = df.loc[df['am_profit_long_close'] < 0, 'am_profit_long_close'].count()
    am_avg_long_profit = round(df.loc[df['am_profit_long_close'] > 0, 'am_profit_long_close'].mean(), 2)
    am_avg_long_loss = round(df.loc[df['am_profit_long_close'] < 0, 'am_profit_long_close'].mean(), 2)
    winrate_long = round((am_count_long_profit / (am_count_long_profit + am_count_long_loss)) * 100, 2)

    am_max_long = round(df['am_profit_long_close'].max(), 2)
    am_min_long = round(df['am_profit_long_close'].min(), 2)

    am_drawdown_long = round(abs(df['am_profit_long'].min()), 2)
    am_growth_long = round(df['am_profit_long'].max(), 2)

    # SHORT statistics
    am_profit_short_close = round(df['am_profit_short_close'].sum(), 2)
    am_profit_short_close_plus = round(df.loc[df['am_profit_short_close'] >= 0, 'am_profit_short_close'].sum(), 2)
    am_profit_short_close_minus = round(df.loc[df['am_profit_short_close'] < 0, 'am_profit_short_close'].sum(), 2)
    am_count_short_profit = df.loc[df['am_profit_short_close'] > 0, 'am_profit_short_close'].count()
    am_count_short_loss = df.loc[df['am_profit_short_close'] < 0, 'am_profit_short_close'].count()
    am_avg_short_profit = round(df.loc[df['am_profit_short_close'] > 0, 'am_profit_short_close'].mean(), 2)
    am_avg_short_loss = round(df.loc[df['am_profit_short_close'] < 0, 'am_profit_short_close'].mean(), 2)
    winrate_short = round((am_count_short_profit / (am_count_short_profit + am_count_short_loss)) * 100, 2)

    am_max_short = round(df['am_profit_short_close'].max(), 2)
    am_min_short = round(df['am_profit_short_close'].min(), 2)

    am_drawdown_short = round(abs(df['am_profit_short'].min()), 2)
    am_growth_short = round(df['am_profit_short'].max(), 2)

    # General Statistics
    am_profit_close = round(am_profit_long_close + am_profit_short_close, 2)
    am_profit_close_plus = round(am_profit_long_close_plus + am_profit_short_close_plus, 2)
    am_profit_close_minus = round(am_profit_long_close_minus + am_profit_short_close_minus, 2)
    am_count_profit = am_count_long_profit + am_count_short_profit
    am_count_loss = am_count_long_loss + am_count_short_loss
    am_avg_profit = round(am_profit_close_plus / am_count_profit, 2)
    am_avg_loss = round(am_profit_close_minus / am_count_loss, 2)

    am_max = round(max(am_max_long, am_max_short), 2)
    am_min = round(min(am_min_long, am_min_short ), 2)

    am_drawdown = round(max(am_drawdown_long, am_drawdown_short), 2)
    am_growth = round(max(am_growth_long, am_growth_short), 2)

    min_depo_df = round(df['depo'].min(), 2)
    max_depo_df = round(df['depo'].max(), 2)

    winrate = round((am_count_profit / (am_count_profit + am_count_loss)) * 100, 2)

    # print(df.tail(50))
    # print(df.iloc[5425:5435])
    # print(df[['Datetime', 'Close', 'price_open_long', 'profit_long']].head(10))
    # print(df[['Datetime', 'Close', 'amount_long', 'amount_short']].head(20))
    """
    print(df)

    print('-------------------------------------------------------')
    print(f'RSI limits {str_limit_rsi}')
    print(f'Number of trades {count_deal}')
    print(f'Number of LONG trades {count_long_deal}')
    print(f'Number of SHORT trades {count_short_deal}')
    print('-------------------------------------------------------')
    print(f'Profit {am_profit_close}')
    print(am_profit_close_plus, am_profit_close_minus, sep=' | ')
    print(f'Average \"+\" trade {am_avg_profit}')
    print(f'Average \"-\" trade {am_avg_loss}')
    print(f'Number of \"+\" trades {am_count_profit}')
    print(f'Number of \"-\" trades {am_count_loss}')

    print(f'Maximum profitable trade {am_max}')
    print(f'Maximum losing trade {am_min}')
    print(f'Maximum growth on a deal {am_growth}')
    print(f'Maximum drawdown on a trade {am_drawdown}')
    print(f'Maximum deposit value {max_depo_df}')
    print(f'Minimum deposit value {min_depo_df}')
    print(f'Maximum deposit growth {round(max_growth, 2)}')
    print(f'Maximum deposit drawdown {round(max_drawdown, 2)}')

    print(f'Winrate {winrate}%')
    print('-------------------------------------------------------')
    print(f'Profit LONG {am_profit_long_close}')
    print(am_profit_long_close_plus, am_profit_long_close_minus, sep=' | ')
    print(f'Average \"+\" LONG trade {am_avg_long_profit}')
    print(f'Average \"-\" LONG trade {am_avg_long_loss}')
    print(f'Number of \"+\" LONG trades {am_count_long_profit}')
    print(f'Number of \"-\" LONG trades {am_count_long_loss}')

    print(f'Maximum profitable LONG trade {am_max_long_long}')
    print(f'Maximum losing LONG trade {am_min_long}')
    print(f'Maximum growth on a LONG trade {am_growth_long}')
    print(f'Maximum drawdown on LONG trade {am_drawdown_long}')
    print(f'Winrate LONG {winrate_long}%')
    print('-------------------------------------------------------')
    print(f'Profit SHORT {am_profit_short_close}')
    print(am_profit_short_close_plus, am_profit_short_close_minus, sep=' | ')
    print(f'Average \"+\" SHORT trade {am_avg_short_profit}')
    print(f'Average \"-\" SHORT trade {am_avg_short_loss}')
    print(f'Number of \"+\" SHORT trades {am_count_short_profit}')
    print(f'Number of \"-\" SHORT trades {am_count_short_loss}')

    print(f'Maximum profitable SHORT trade {am_max_short}')
    print(f'Maximum losing SHORT trade {am_min_short}')
    print(f'Maximum growth on a SHORT trade {am_growth_short}')
    print(f'Maximum Drawdown SHORT trade {am_drawdown_short}')
    print(f'Winrate SHORT {winrate_short}%')
    """



    Rsi_limit = str_limit_rsi
    Count_deal = count_deal
    Max_growth_deal = am_growth
    Max_drawdown_deal = am_drawdown
    Max_growth_depo = round(max_growth, 2)
    Max_drawdown_depo = round(max_drawdown, 2)
    Avg_profit_deal = am_avg_profit
    Avg_loss_deal = am_avg_loss
    Winrate = winrate

    df_res = add_res(df_res, Rsi_limit, Count_deal, Max_growth_deal, Max_drawdown_deal, Max_growth_depo,
                     Max_drawdown_depo, Avg_profit_deal, Avg_loss_deal, Winrate)

    return df_res


def run_strat(timeframe):
    global size, depo, last_long_price, last_short_price, last_depo, max_depo, min_depo, max_drawdown, max_growth
    df_res = create_df_res()
    for delta in range(1):      # Value for RSI limits (if the value is 31, variants from 30-70 to 0-100 will be processed.
        # print(delta)
        over_sold = over_sold_start - delta
        over_bought = over_bought_start + delta
        str_limit_rsi = f'({over_sold} - {over_bought})'

        init_variables()

        df = read_data_csv(f'data/BTCUSDT_data_{timeframe}.csv')        # Path to historical data files
        df = calculate_rsi(df, 'Close', length_rsi)
        df = mark_long_short(df, 'Close', over_sold, over_bought)
        df = create_deal_long(df)
        df = create_deal_short(df)
        df = calc_profit_long_close(df)
        df = calc_profit_short_close(df)
        df = calc_amount_long(df, size)
        df = calc_amount_short(df, size)
        df = calc_am_profit_long_close(df)
        df = calc_am_profit_short_close(df)
        df = create_depo(df)
        df = create_maxdd_maxgr_deal(df)
        df = split_str_max_dd_gr(df)

        df_res = calc_print_stat_amount(df, str_limit_rsi, df_res)

        print(f'RSI limits {str_limit_rsi}')

    return df, df_res


def run_main():
    # timeframes = ['4h', '1h', '30m', '15m', '5m', '3m', '1m']
    timeframes = ['4h']
    for timeframe in timeframes:


        df, df_res = run_strat(timeframe)
        filename_res = f'BTCUSDT_RSI_{timeframe}.csv'
        save_data_csv(df_res, filename_res)
        print(f'File saved: {filename_res}')
        df_deals = create_df_deals()
        df_deals = add_deals(df, df_deals)
        print(df_deals)
        # Save the trades file
        filename_deals = f'DEALS_BTCUSDT_RSI_{timeframe}.csv'.
        save_data_csv(df_deals, filename_deals)
        print(f'Deal file saved: {filename_deals}')


run_main()


















