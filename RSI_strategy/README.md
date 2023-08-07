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
- [Benefits and Recommendations](#benefits-and-recommendations)
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

Meticulous analysis on the H1 timeframe revealed that the optimal RSI settings of <span style="background-color: #00FF00; padding: 2px 5px; border-radius: 3px;">RSI 13/87</span> significantly outperformed other configurations. This specific setup maximized the winrate, making it a promising choice for traders operating within this timeframe. Explore the [H1 backtest results](https://github.com/slinkslinkovich/backtesting_crypto/blob/main/RSI_strategy/H1_backtest_results.csv).

### M15 Timeframe

The M15 timeframe reaffirmed the value of simplicity, as adhering to the standard RSI parameters produced consistent results. This shorter interval benefited from the stability provided by the traditional RSI strategy, making it a reliable option for those looking for a balanced approach. See the [M15 backtest results](https://github.com/slinkslinkovich/backtesting_crypto/blob/main/RSI_strategy/BTCUSDT_RSI_15m_One_01_01_2021-07_01_2023.csv).

### M5 Timeframe

Similar to M15, the M5 timeframe thrived when the standard RSI parameters remained unchanged. The fast-paced nature of M5 trading was effectively harnessed by the RSI strategy, underscoring its versatility across different timeframes. Check the [M5 backtest results](https://github.com/slinkslinkovich/backtesting_crypto/blob/main/RSI_strategy/BTCUSDT_RSI_5m_One_01_01_2021-07_01_2023.csv).

### M3 Timeframe

In the M3 timeframe, the strategy continued to demonstrate resilience with the use of standard RSI parameters. This interval allowed traders to capitalize on shorter-term fluctuations while maintaining the strategy's overall effectiveness. Explore the [M3 backtest results](https://github.com/slinkslinkovich/backtesting_crypto/blob/main/RSI_strategy/BTCUSDT_RSI_3m_One_01_01_2021-07_01_2023.csv).

### M1 Timeframe

On the M1 timeframe, sticking to the standard RSI parameters proved to be a prudent choice. The rapid pace of M1 trading was navigated successfully with this approach, reinforcing the adaptability of the RSI strategy across various trading conditions. Check out the [M1 backtest results](https://github.com/slinkslinkovich/backtesting_crypto/blob/main/RSI_strategy/BTCUSDT_RSI_1m_One_01_01_2021-07_01_2023.csv).

## Benefits and Recommendations

The RSI strategy, with its simplicity and adaptable parameters, offers several benefits:
- **Proven Profitability**: The strategy showcased consistent profits across a range of timeframes, attesting to its reliability.
- **Versatility**: From longer intervals like H4 to rapid intervals like M1, the RSI strategy adapts to diverse trading scenarios.
- **Winrate Optimization**: The H1 timeframe revealed the importance of tailored settings, optimizing the strategy's winrate.
- **Risk Management**: The RSI's oversold and overbought levels provide valuable signals for managing risk and potential reversals.

For optimal results:
- **Customization**: Consider adjusting RSI thresholds based on timeframe and market conditions.
- **Backtesting**: Continue backtesting with different settings to find the optimal parameters for your trading style.
- **Risk Control**: Pair the RSI strategy with effective risk management techniques for consistent success.

## Summary

This comprehensive analysis underscores the potential of the RSI strategy to deliver consistent profits across diverse timeframes. Whether trading on longer intervals such as H1 or engaging in rapid-fire transactions on M1, the RSI strategy showcases its reliability and adaptability. The provided [rsi.py](https://github.com/slinkslinkovich/backtesting_crypto/blob/main/RSI_strategy/rsi.py) script empowers traders to harness the power of the RSI indicator and embark on a profitable journey in the cryptocurrency market.

Feel free to explore the provided CSV files for a detailed breakdown of each backtest and further insights into the strategy's performance.
