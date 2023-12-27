# MT5-Trading-Bot

## Description

This Python script automates trading on the MetaTrader 5 (MT5) platform, placing alternating buy and sell orders for a specified currency pair. It calculates stop-loss and take-profit levels based on user-defined percentages and monitors the trade execution process.

## Installation

Install MetaTrader5: Ensure you have MT5 installed and running on your system.

Install Required Libraries: Use pip to install the necessary Python libraries:

Bash

<code>pip install MetaTrader5 pandas</code>

## Usage

Edit Configuration Parameters:

In the mt5TradingBot.py file in the if __name__ == "__main__": section, modify the following values:


login: Your MT5 account login number

password: Your MT5 account password

server: The MT5 server name ('MetaQuotes-Demo' for demo accounts)

ticker: The currency pair you want to trade (e.g., "EURUSD")

qty: The trade quantity in lots

sl_pct: The stop-loss percentage (e.g., 0.05 for 5%)

tp_pct: The take-profit percentage (e.g., 0.1 for 10%)

Run the Script: Execute the script using Python:

Bash

<code>python mt5TradingBot.py</code>

## Functionality

Connects to MT5 using the provided credentials.

Retrieves current prices for the specified currency pair.

Calculates stop-loss and take-profit levels.

Loops 100 times, performing the following actions in each iteration:

Prints the current timestamp.

Retrieves recent historical price data.

Prints the last 3 bars of the historical data.

Places a buy order.

Places a sell order.

Waits for 30 seconds before the next iteration.

## Disclaimer

!This trading bot is for educational and demonstration purposes only!.

Do not use it with real funds.

Performance is not indicative of future results.

Trading involves significant risks and can result in financial losses.

## Author

Meffun Adegoke https://github.com/TheKingAde
