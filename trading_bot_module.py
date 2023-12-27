from datetime import datetime
import MetaTrader5 as mt
import pandas as pd
import time
import os


class TradingBot:
    def __init__(self, ticker, qty, sl_pct, tp_pct):
        """
        Initializes the TradingBot with parameters.

        Parameters:
        - ticker (str): Trading symbol.
        - qty (float): Quantity or lot size.
        - sl_pct (float): Stop-loss percentage.
        - tp_pct (float): Take-profit percentage.
        """
        self.ticker = ticker
        self.qty = qty
        self.sl_pct = sl_pct
        self.tp_pct = tp_pct
        self.mt = mt

    def initialize_connection(self, login, password, server):
        """
        Initializes the connection to MetaTrader 5.

        Parameters:
        - login (int): Account login ID.
        - password (str): Account password.
        - server (str): MetaTrader server name.
        """
        if not self.mt.initialize():
            print("initialize() failed")
            mt.shutdown()
        if not self.mt.login(login, password, server):
            print("failed to connect to account #{}, error code {}".format(login, self.mt.last_error()))
            mt.shutdown()

    def get_prices(self):
        """Gets the bid and ask prices for the trading symbol."""
        self.buy_price = self.mt.symbol_info_tick(self.ticker).ask
        self.sell_price = self.mt.symbol_info_tick(self.ticker).bid

    def calculate_sl_tp(self):
        """Calculates stop-loss and take-profit prices"""
        self.buy_sl = self.buy_price * (1 - self.sl_pct)
        self.buy_tp = self.buy_price * (1 + self.tp_pct)
        self.sell_sl = self.sell_price * (1 + self.sl_pct)
        self.sell_tp = self.sell_price * (1 - self.tp_pct)

    def create_order(self, order_type):
        """
        Creates a market order (buy or sell).

        Parameters:
        - order_type (int): Type of order.

        Returns:
        - order (OrderSendResult): Result of the order creation.
        """
        request = {
            "action": mt.TRADE_ACTION_DEAL,
            "symbol": self.ticker,
            "volume": self.qty,
            "type": order_type,
            "price": self.buy_price if order_type == mt.ORDER_TYPE_BUY else self.sell_price,
            "sl": self.buy_sl if order_type == mt.ORDER_TYPE_BUY else self.sell_sl,
            "tp": self.buy_tp if order_type == mt.ORDER_TYPE_BUY else self.sell_tp,
            "comment": "PYTHON SCRIPT CREATE ORDER",
            "type_time": mt.ORDER_TIME_GTC,
            "type_filling": mt.ORDER_FILLING_IOC
        }

        order = self.mt.order_send(request)

        if order.retcode != mt.TRADE_RETCODE_DONE:
            error_message = f"Error creating order: {order.comment}"
            print(error_message)
        elif order_type == mt.ORDER_TYPE_BUY:
            print("Buy Order: by {} {} lots at {}".format(self.ticker, self.qty, request["price"]))
        elif order_type == mt.ORDER_TYPE_SELL:
            print("Sell Order: by {} {} lots at {}".format(self.ticker, self.qty, request["price"]))

        return order

    def run(self):
        """Main loop for the trading bot."""
        self.get_prices()
        self.calculate_sl_tp()

        for _ in range(100):
            ohlc = pd.DataFrame(mt.copy_rates_range(ticker, mt.TIMEFRAME_M1, datetime(2023, 12, 21), datetime.now()))
            ohlc['time'] = pd.to_datetime(ohlc['time'], unit='s')
            print('currency pair {}'. format(ticker))
            print(ohlc.tail(3))

            # Add logic for buy and selling
            self.create_order(mt.ORDER_TYPE_BUY)
            self.create_order(mt.ORDER_TYPE_SELL)

            time.sleep(30)
            os.system('cls' if os.name == 'nt' else 'clear')
