#!/usr/bin/python3
# Import the TradingBot class from the trading_bot_module
from trading_bot_module import TradingBot

if __name__ == "__main__":
    # MetaTrader 5 demo server credentials
    login =  160408249 # change to your login
    password = '@Adegoke001' # change to your password
    server = 'ForexTimeFXTM-Demo01'

    # Trading parameters
    ticker = "NZDUSD"  # Replace with the currency of your choice
    qty = 0.01
    sl_pct = 0.05  # Stop-loss percentage
    tp_pct = 0.1   # Take-profit percentage

    # Create an instance of the TradingBot
    bot = TradingBot(ticker, qty, sl_pct, tp_pct)

    # Initialize connection to MetaTrader 5
    bot.initialize_connection(login, password, server)

    # Run the trading bot
    bot.run()
