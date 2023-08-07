# RSI Trading Strategy and Backtest Results

Welcome to the Readme for the Relative Strength Index (RSI) trading strategy and the obtained results. In this document, we'll delve into the RSI strategy and its performance analysis based on backtests carried out on different timeframes using historical data of the BTCUSDT trading pair. The strategy's implementation can be found in the provided [rsi.py](https://github.com/slinkslinkovich/backtesting_crypto/blob/main/RSI_strategy/rsi.py) script.

## Table of Contents

- [Introduction](#introduction)
- [Strategy Overview](#strategy-overview)
- [Backtest Data](#backtest-data)
  - [H4 Timeframe](#h4-timeframe)
  - [H1 Timeframe](#h1-timeframe)
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

The highest timeframe, H4, showed favorable results with standard RSI settings. By using the RSI thresholds of <span style="background-color: #00FF00; padding: 2px 5px; border-radius: 3px;">RSI 20/80</span>, we achieved the highest profit among all timeframes. This setting proved to be optimal for capturing significant price movements within this timeframe. It is this set-up that generates consistent profits for us. Check out the detailed [H4 backtest results](https://github.com/slinkslinkovich/backtesting_crypto/blob/main/RSI_strategy/BTCUSDT_RSI_4h_One_01_01_2021-07_01_2023.csv).

### H1 Timeframe

Meticulous analysis on the H1 timeframe revealed that the optimal RSI settings of <span style="background-color: #00FF00; padding: 2px 5px; border-radius: 3px;">RSI 13/87</span> significantly outperformed other configurations. This specific setup maximized the winrate, making it a promising choice for traders operating within this timeframe. Explore the [H1 backtest results](https://github.com/slinkslinkovich/backtesting_crypto/blob/main/RSI_strategy/BTCUSDT_RSI_1h_One_01_01_2021-07_01_2023.csv).

### M15 Timeframe

M15 was not successful unfortunately all variants were unprofitable.  See the [M15 backtest results](https://github.com/slinkslinkovich/backtesting_crypto/blob/main/RSI_strategy/BTCUSDT_RSI_15m_One_01_01_2021-07_01_2023.csv).

### M5 Timeframe

Like the M15, the M5 timeframe has not been successful. Unfortunately RSI is not so profitable on small timeframes. [M5 backtest results](https://github.com/slinkslinkovich/backtesting_crypto/blob/main/RSI_strategy/BTCUSDT_RSI_5m_One_01_01_2021-07_01_2023.csv).

### M3 Timeframe

On the M3 timeframe, the strategy continued to demonstrate its ineffectiveness on low TFs. Unfortunately, again only minuses. Explore the [M3 backtest results](https://github.com/slinkslinkovich/backtesting_crypto/blob/main/RSI_strategy/BTCUSDT_RSI_3m_One_01_01_2021-07_01_2023.csv).

### M1 Timeframe

On the M1 timeframe we again got only minuses, unfortunately there are no profitable setups. Check out the [M1 backtest results](https://github.com/slinkslinkovich/backtesting_crypto/blob/main/RSI_strategy/BTCUSDT_RSI_1m_One_01_01_2021-07_01_2023.csv).

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
