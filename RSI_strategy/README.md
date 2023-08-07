
# RSI

A brief description of what this project does and who it's for
Hi everyone, we are backtesting various indicators and strategies on the crypto market. In this post we are going to talk about RSI.
Most likely, everyone is already familiar with this indicator. A lot of articles and different algorithms have been written about this indicator. I propose to analyze the work and logic of the indicator itself.
Relative Strength Index (RSI) is a technical analysis tool, an indicator that measures the speed and magnitude of price movements of an asset.
The main task of RSI is to analyze the strength of the price impulse and help in determining the overbought or oversold level of the asset.
RSI is depicted on the chart as an oscillator with a value from 0 to 100. The generally accepted overbought level of an asset is the zone above the value of 70, and oversold - below 30.
The RSI indicator "weighs the forces" of growth and fall of the asset price. The following formula is used to calculate RSI values:
RSI = 100 - 100 / (1+RS)
RS is the average exponential of the price when the asset rose over the time period in question, divided by the average exponential of the price when the asset fell over the time period in question.
RSI has gained popularity for its simple calculations and clear interpretation of data. It has become a popular tool for technical analysis of long-term price movements of cryptocurrencies: the higher the price averaging period, the fewer false signals the indicator shows.
Of course, there are advantages and disadvantages to using RSI. There are people who use it in trading, and there are those who do not know how to use it. We have decided for ourselves that this indicator suits our trading style and we actively use it. In the next post we will present you our first strategy, which continues to be used in our trading. In the following files you will see the results of our backtests. We use one rule for all strategies - you are allowed to hold only one trade, without adding margin to the position. This rule is called - One. 

These are the results of our RSI backtests on the BTCUSDT pair on the most common timeframes. 
All tests were conducted with the amount of transaction in 100$, without leverage. This is done for the convenience of your calculations, as 100$ = 100%.  
During the testing, we used dynamic RSI parameters, they are shown in the RSI_limit column. As we can see RSI parameters have a very strong influence on the number of trades. The file also contains: 
Maximum drawdown of a trade
Maximum deposit drawdown 
Maximum gain in a deal 
Maximum deposit growth
Remember, this is not financial advice, but as you can see, even RSI has a high winrate and can be profitable.
