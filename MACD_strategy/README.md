# Анализ MACD

Приветствуем!

В этом README мы рассмотрим индикатор MACD (Moving Average Convergence Divergence) и проанализируем начальную торговую стратегию, основанную на этом индикаторе. В ходе наших тестов мы исследовали различные настройки для индикатора MACD. Все тесты проводились с 03 января 2020 года по 01 июля 2023 года. 

Для временных интервалов M5/M3/M1 мы сократили диапазон с 1 мая 2023 года по 1 июля 2023 года. Также, мы немного изменили наши файлы - отчеты. Нам было бы интересно услышать ваше мнение!

## Содержание

- [Описание индикатора](#indicator-description)
- [Анализ таймфреймов](#timeframe-analysis)
  - [D1](#d1)
  - [H4](#h4)
  - [H1](#h1)
  - [M30](#m30)
  - [M15](#m15)
  - [M5](#m5)
  - [M3](#m3)
  - [M1](#m1)
- [Заключение](#conclusion)

## Описание индикатора

MACD - это модифицированная версия классического индикатора MACD. Он состоит из трех компонентов:

- **Быстрая ЭМА (Экспоненциальная скользящая средняя):** Представляет краткосрочную тенденцию.
- **Медленная ЭМА:** Представляет долгосрочную тенденцию.
- **Сигнальная ЭМА:** Предоставляет сигналы на покупку/продажу на основе схождения и расхождения быстрой и медленной ЭМА.

## Анализ таймфреймов

### D1

- Самый большой временной интервал, использованный в наших тестах.
- Лучшая прибыль: +254.52%
- Процент успешных сделок: 47.92%
- Лучшие настройки MACD: 45/50/5
- Лучшая прибыль с учетом комиссии: 250.68%
- Комиссия: 3.68%
- [Результаты бэктеста для D1](https://github.com/slinkslinkovich/backtesting_crypto/blob/main/MACD_strategy/BTCUSDT_MACD_D1_One_03_01_2020-07_01_2023.csv).

### H4 

- Следующий временной интервал в нашем исследовании.
- Лучшая прибыль: +226%
- Процент успешных сделок: 35.74%
- Лучшие настройки MACD: 25/35/35
- Лучшая прибыль с учетом комиссии: 207.92%
- Комиссия: 18.08%
- [Результаты бэктеста для H4](https://github.com/slinkslinkovich/backtesting_crypto/blob/main/MACD_strategy/BTCUSDT_MACD_H4_One_03_01_2020-07_01_2023.csv).

### H1

- Самый интересный временной интервал в нашем тесте.
- Лучшая прибыль: +382.99%
- Процент успешных сделок: 34.21%
- Лучшие настройки MACD: 20/50/10
- Лучшая прибыль с учетом комиссии: 258.11%
- Комиссия: 124.88%
- [Результаты бэктеста для H1](https://github.com/slinkslinkovich/backtesting_crypto/blob/main/MACD_strategy/BTCUSDT_MACD_H1_One_03_01_2020-07_01_2023.csv).

### M30

- Открывает путь к более коротким временным интервалам.
- Лучшая прибыль: +138.57%
- Процент успешных сделок: 34.79%
- Лучшие настройки MACD: 45/50/30
- Лучшая прибыль с учетом комиссии: 85.18%
- Комиссия: 53.52%
- [Результаты бэктеста для M30](https://github.com/slinkslinkovich/backtesting_crypto/blob/main/MACD_strategy/BTCUSDT_MACD_M30_One_03_01_2020-07_01_2023.csv).

### M1

- Лучшая прибыль: +64.21%
- Процент успешных сделок: 35.31%
- Лучшие настройки MACD: 10/15/15
- Лучшая прибыль с учетом комиссии: 0
- Комиссия: 144.56%
- [Результаты бэктеста для M15](https://github.com/slinkslinkovich/backtesting_crypto/blob/main/MACD_strategy/BTCUSDT_MACD_M15_One_03_01_2020-07_01_2023.csv).

### M5

- Суженный диапазон тестирования, начиная с 1 мая 2023 года.
- Лучшая прибыль: +11.64%
- Лучшие настройки MACD: 50/55/40
- [Результаты бэктеста для M5](https://github.com/slinkslinkovich/backtesting_crypto/blob/main/MACD_strategy/BTCUSDT_MACD_M5_One_05_01_2023-07_01_2023.csv).

### M3

- Лучшая прибыль: +8.81%
- Лучшие настройки MACD: 45/50/15
- [Результаты бэктеста для M3](https://github.com/slinkslinkovich/backtesting_crypto/blob/main/MACD_strategy/BTCUSDT_MACD_M3_One_05_01_2023-07_01_2023.csv).

### M1

- Самый худший временной интервал в наших тестах, прибыль не получена.
- Рекомендуется использовать систему разворота.
- [Результаты бэктеста для M1](https://github.com/slinkslinkovich/backtesting_crypto/blob/main/MACD_strategy/BTCUSDT_MACD_M1_One_05_01_2023-07_01_2023.csv).

## Заключение

Индикатор MACD продемонстрировал многообещающие результаты на различных временных интервалах, с лучшими результатами на больших временных интервалах, таких как H4, H1 и D1. Эти результаты могут служить отправной точкой для разработки торговой стратегии на основе индикатора MACD. Однако помните, что прошлые результаты не являются показателем будущих результатов, и важно проводить тщательное бэктестирование и управление рисками перед внедрением любой торговой стратегии.
