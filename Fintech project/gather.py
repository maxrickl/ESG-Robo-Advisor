#!/usr/bin/env python3
from utils import *
import datetime
from pandas_datareader import data


# get Adj close price for stocks from start date s to end date e
def get_yahoo_data(stocks,start_date,end_date):
    stocks = data.DataReader(stocks, data_source='yahoo', start = start_date, end = end_date)['Adj Close']
    return stocks

tickers = get_tickers()
start_date = '2017-01-01'
end_date = '2019-01-01'

# get data from Yahoo finance API
stock_prices = get_yahoo_data(tickers, start_date, end_date)

# output retrieved data to file to read later
with open(f"{DATA_DIR}/stock_prices", "w") as f:
    # write list of companies as table header
    f.write(", ".join(tickers) + '\n')
    for r in stock_prices.values:
        # convert all prices to string and write row for this day's prices
        f.write(",".join(map(str, r)) + '\n')
