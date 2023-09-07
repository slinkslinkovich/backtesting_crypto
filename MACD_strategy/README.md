# MACD Indicator Analysis and Strategy
Greetings!
In this README, we will discuss the MACD (Moving Average Convergence Divergence Indicator) and analyze a starting trading strategy based on this indicator. During our testing, we explored various settings for the MACD indicator.All tests were conducted between 03 January 2020 and 01 July 2023. 
Timeframes M5/M3/M1 we narrowed the range from 1 May 2023 to 1 July 2023. Also, we've changed our files - the reports - a little bit. We would be interested in your opinion!

## Table of Contents
- [Indicator Description](#indicator-description)
- [Timeframe Analysis](#timeframe-analysis)
  - [D1 (Daily)](#d1-daily)
  - [H4 (4-Hour)](#h4-4-hour)
  - [H1 (1-Hour)](#h1-1-hour)
  - [M30 (30 Minutes)](#m30-30-minutes)
  - [M15 (15 Minutes)](#m15-15-minutes)
  - [M5 (5 Minutes)](#m5-5-minutes)
  - [M3 (3 Minutes)](#m3-3-minutes)
  - [M1 (1 Minute)](#m1-1-minute)
- [Conclusion](#conclusion)

## Indicator Description

MACDI is a modified version of the classic MACD indicator. It consists of three components:
- **Fast EMA (Exponential Moving Average):** Represents the short-term trend.
- **Slow EMA:** Represents the long-term trend.
- **Signal EMA:** Provides buy/sell signals based on the convergence and divergence of the fast and slow EMAs.

## Timeframe Analysis

### D1 (Daily)
- The largest timeframe used in our test.
- Best profit: +254.52%
- Winrate: 47.92%
- Best MACD settings: 45/50/5
- Best profit with commission: 250.68%
- Commission: 3.68%
- [D1 backtest results](https://github.com/slinkslinkovich/backtesting_crypto/blob/main/MACD_strategy/BTCUSDT_MACD_D1_One_03_01_2020-07_01_2023.csv).
### H4 (4-Hour)
- The next timeframe in our study.
- Best profit: +226%
- Winrate: 35.74%
- Best MACD settings: 25/35/35
- Best profit with commission: 207.92%
- Commission: 18.08%
- [H4 backtest results](https://github.com/slinkslinkovich/backtesting_crypto/blob/main/MACD_strategy/BTCUSDT_MACD_H4_One_03_01_2020-07_01_2023.csv).
### H1 (1-Hour)
- The most interesting timeframe in our test.
- Best profit: +382.99%
- Winrate: 34.21%
- Best MACD settings: 20/50/10
- Best profit with commission: 258.11%
- Commission: 124.88%
- [H1 backtest results](https://github.com/slinkslinkovich/backtesting_crypto/blob/main/MACD_strategy/BTCUSDT_MACD_H1_One_03_01_2020-07_01_2023.csv).


### M30 (30 Minutes)
- Opens the way to shorter timeframes.
- Best profit: +138.57%
- Winrate: 34.79%
- Best MACD settings: 45/50/30
- Best profit with commission: 85.18%
- Commission: 53.52%
- [M30 backtest results](https://github.com/slinkslinkovich/backtesting_crypto/blob/main/MACD_strategy/BTCUSDT_MACD_M30_One_03_01_2020-07_01_2023.csv).


### M15 (15 Minutes)
- Best profit: +64.21%
- Winrate: 35.31%
- Best MACD settings: 10/15/15
- Best profit with commission: not possible 
- Commission: 144.56%
- [M15 backtest results](https://github.com/slinkslinkovich/backtesting_crypto/blob/main/MACD_strategy/BTCUSDT_MACD_M15_One_03_01_2020-07_01_2023.csv).


### M5 (5 Minutes)
- Narrowed testing range, starting from May 1, 2023.
- Best profit: +11.64%
- Best MACD settings: 50/55/40
- [M5 backtest results](https://github.com/slinkslinkovich/backtesting_crypto/blob/main/MACD_strategy/BTCUSDT_MACD_M5_One_05_01_2023-07_01_2023.csv).

### M3 (3 Minutes)
- Best profit: +8.81%
- Best MACD settings: 45/50/15
- [M3 backtest results](https://github.com/slinkslinkovich/backtesting_crypto/blob/main/MACD_strategy/BTCUSDT_MACD_M3_One_05_01_2023-07_01_2023.csv).


### M1 (1 Minute)
- The worst timeframe in our testing, no profit obtained.
- Suggested use: Consider employing a reversal system.
- [M1 backtest results](https://github.com/slinkslinkovich/backtesting_crypto/blob/main/MACD_strategy/BTCUSDT_MACD_M1_One_05_01_2023-07_01_2023.csv).


## Conclusion

The MACD indicator showed promising results across various timeframes, with the best results achieved on bigger timeframes such as H4,H1 and D1. These results can serve as a starting point for developing a trading strategy based on the MACD indicator. However, please remember that past performance is not indicative of future results, and it's essential to conduct thorough backtesting and risk management before implementing any trading strategy.
