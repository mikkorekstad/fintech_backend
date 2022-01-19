import datetime

import pandas as pd
import yfinance as yf
from pandas import DataFrame

# import streamlit as st
# import requests
# import pandas as pd


class Scraper:
    """Scraper class"""
    def __init__(self, ticker="^VIX", n_days=30):
        self.ticker = yf.Ticker(f"{ticker}")
        self.historic_data = self.get_historic_data(ticker=self.ticker, n_days=n_days)

    def get_json(self, ticker_str=None, n_days=30):
        """Return json from desired dataframe"""
        if ticker_str:  # If a ticker is provided, select the provided.
            ticker = yf.Ticker(f"{ticker_str}")
        else:  # Else use the one from the instance.
            ticker = self.ticker

        # Return data as a json
        data = self.get_historic_data(ticker=ticker, n_days=n_days)
        return data.to_json(index=True, orient='split')

    @staticmethod
    def get_historic_data(ticker, n_days=30):
        """Get historic data from the past n_days, with the current ticker object."""
        # Time Info
        current_datetime = datetime.datetime.now()
        start = current_datetime - datetime.timedelta(days=n_days)
        end = current_datetime - datetime.timedelta(days=1)

        # Get Data
        data = ticker.history(
            start=start.strftime("%Y-%m-%d"), end=end.strftime("%Y-%m-%d")
        )
        data.drop(labels=["Volume", "Dividends", "Stock Splits"], axis=1, inplace=True)
        if data.shape[0] < 15:
            raise RuntimeError("Not enough data, we need at least 15 days worth!")
        return pd.DataFrame(data)

    def get_extreme_value(self, col, method):
        """Expected col is either Open, High, Low or Close"""
        return eval(f"self.historic_data['{col}'].{method}()")

    def get_current_data(self):
        """Get the current price"""
        return self.ticker.info.get("regularMarketPrice")

    def get_current_val(self, col):
        """Get today's value from desired column."""
        return self.historic_data[col].iloc[-1]

    def recommendation(self, api=False):
        """Calculate a recommendation"""
        current_price = self.get_current_data()
        open_today = self.get_current_val("Open")
        low = self.get_extreme_value("Low", "min")
        high = self.get_extreme_value("High", "max")

        # Get info about stock market situation
        new_low = current_price < low
        new_high = current_price > high
        up_today = current_price > open_today

        # Do a quick analysis of the data
        if up_today and new_low:
            sell = True
        else:
            sell = False

        if not up_today and new_high:
            buy = True
        else:
            buy = False

        # Return the results
        if api:
            return {
                "recommendation": {"buy": f"{buy}", "sell": f"{sell}"},
                "new_low": f"{new_low}",
                "new_high": f"{new_high}",
                "up_today": f"{up_today}",
            }
        return f"Recommendations: \n{buy=}\n{sell=}"



