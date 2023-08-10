# RSI Trading Strategy and Backtest Results

Welcome to the Readme for the Relative Strength Index (RSI) trading strategy and the obtained results. In this document, we'll delve into the RSI strategy and its performance analysis based on backtests carried out on different timeframes using historical data of the BTCUSDT trading pair. The strategy's implementation can be found in the provided [rsi.py](https://github.com/slinkslinkovich/backtesting_crypto/blob/main/RSI_strategy/rsi.py) script.

## Table of Contents

- [Introduction](#introduction)
- [Strategy Overview](#strategy-overview)
- [Backtest Data](#backtest-data)
  - [H4 Timeframe](#h4-timeframe)
  - [H1 Timeframe](#h1-timeframe)
  - [M30 Timeframe](#m30-timeframe)
  - [M15 Timeframe](#m15-timeframe)
  - [M5 Timeframe](#m5-timeframe)
  - [M3 Timeframe](#m3-timeframe)
  - [M1 Timeframe](#m1-timeframe)
- [Advantages and Recommendations](#Advantages-and-Recommendations)
- [Summary](#summary)

## Introduction

The RSI (Relative Strength Index) is a widely used technical analysis tool that measures the speed and magnitude of price movements of an asset. Its primary purpose is to analyze the strength of price impulses and identify overbought or oversold levels. The RSI oscillator ranges from 0 to 100, with values above 70 indicating overbought conditions and values below 30 indicating oversold conditions. One trade means that the strategy opens only one trade and does not add margin to it. At the same time, the condition for closing this trade is the appearance of a signal in the opposite direction.
Testing range: 01.01.2021 - 07.01.2023

**Keywords**

RSI_limit - RSI values that were tested.

Count_deal - number of trades.

Max_growth_deal - the indicator of the largest profit in one trade.

Max_drawdown_deal - indicator of the largest drawdown in one trade.

Max_growth_depo - maximum deposit growth.

Max_ drawdown_depo - maximum drawdown of the deposit.

Avg_profit_deal - average profit on a deal.

Avg_loss_deal - average drawdown on a deal.

Winrate - ratio of profitable deals to the total number of deals.

## Strategy Overview

The standard RSI strategy involves:
- Opening long positions when RSI reaches 30 (oversold)
- Opening short positions when RSI reaches 70 (overbought)

This classic strategy was employed in our research, with variations in the overbought and oversold thresholds tested across different timeframes.
All calculations are made with a margin in the deal of 100 dollars without using leverage. This is done for simplicity of your personal calculations, as 100 dollars = 100% and you can use any amount.

## Backtest Data

### H4 Timeframe

The highest timeframe on which our backtest was conducted. It was on this timeframe that we saw one of the best results, namely +84% at RSI 80/20 settings. Check out the detailed [H4 backtest results](https://github.com/slinkslinkovich/backtesting_crypto/blob/main/RSI_strategy/BTCUSDT_RSI_4h_One_01_01_2021-07_01_2023.csv).

### H1 Timeframe

The H1 also performed very well, with the settings even further away from the classic settings on it. Thus, at RSI 14/86 settings we managed to get +105%. Explore the [H1 backtest results](https://github.com/slinkslinkovich/backtesting_crypto/blob/main/RSI_strategy/BTCUSDT_RSI_1h_One_01_01_2021-07_01_2023.csv).

### M30 Timeframe

M30 was not as interesting as H1, but even on this timeframe I managed to find optimal settings. The settings 13/87 - they brought +19.28%.However, if you change the strategy to a reversal strategy and trade in the opposite direction of the signals - you can get +214% with an RSI configuration of 21/79. Explore the [M30 backtest results]
(https://github.com/slinkslinkovich/backtesting_crypto/blob/main/RSI_strategy/BTCUSDT_RSI_30m_One_01_01_2021-07_01_2023%20-%20BTCUSDT_RSI_30m_One_01_01_2021-07_01_2023.csv).

### M15 Timeframe

M15 again shows that RSI is not always good with a standard strategy. In this case, the strategy is profitable only when trading in the opposite direction. With 15/85 settings and reverse entry system the maximum profit of +162% was achieved. See the [M15 backtest results](https://github.com/slinkslinkovich/backtesting_crypto/blob/main/RSI_strategy/BTCUSDT_RSI_15m_One_01_01_2021-07_01_2023.csv).

### M5 Timeframe

M5 did not please with a profit, but if we had used a reverse entry, we would have been profitable even on this timeframe. The 16/84 settings and the reversal system are the key to +200% profit. [M5 backtest results](https://github.com/slinkslinkovich/backtesting_crypto/blob/main/RSI_strategy/BTCUSDT_RSI_5m_One_01_01_2021-07_01_2023.csv).

### M3 Timeframe

M3 pleased us with an abundance of profitable parameters. But 16/84 and 151% profit settings are clearly our favorites. Explore the [M3 backtest results](https://github.com/slinkslinkovich/backtesting_crypto/blob/main/RSI_strategy/BTCUSDT_RSI_3m_One_01_01_2021-07_01_2023.csv).

### M1 Timeframe

M1 exceeded expectations but we'll stop at +258% and 27/73 settings. 
This is the magic of RSI! Check out the [M1 backtest results](https://github.com/slinkslinkovich/backtesting_crypto/blob/main/RSI_strategy/BTCUSDT_RSI_1m_One_01_01_2021-07_01_2023.csv).

## Advantages and Recommendations

The RSI strategy, due to its simplicity and customizable parameters, has a number of advantages:

- **Proven profitability**: The strategy has demonstrated profits on various timeframes, which shows its reliability.
- **Versatility**: The RSI strategy adapts to different trading scenarios, ranging from longer intervals such as H4 to fast intervals such as M1.
- **Win Optimization**: The H1 timeframe showed the importance of individual settings that optimize a strategy's win rate.
- **Risk Management**: RSI oversold and overbought levels are valuable signals for risk management and potential reversals.

For optimal results:

- **Adjustment**: Consider adjusting RSI thresholds based on timeframe and market conditions. Work on a reversal strategy and adjust Risk/Profit values.
- **Backtesting**: Continue backtesting with different settings to find the optimal settings for your trading style.
- **Risk Control**: Use the RSI strategy paired with effective risk management techniques to achieve consistent success.
- **Reversion**: It is worth considering working in reverse in our estimation - reversing RSI should be profitable on all TFs.

## Summary

This comprehensive analysis highlights the potential of the RSI strategy to generate consistent profits across a variety of timeframes. The provided script [rsi.py](https://github.com/slinkslinkovich/backtesting_crypto/blob/main/RSI_strategy/rsi.py) and the results proved that RSI can and is profitable, not on all timeframes but profitable.

Feel free to study the provided CSV files to analyze each backtest in detail and learn more about the strategy's performance.
