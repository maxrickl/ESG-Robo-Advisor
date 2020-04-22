import pandas as pd
import pandas_datareader as web

DATA_DIR="data_dump"

def get_tickers():
    # read the list of companies from static data file
    with open(f"{DATA_DIR}/tickers") as f:
        tickers = []
        for ticker in f.readlines():
            tickers.append(ticker.strip())
    return tickers
            
def get_price_matrix():
    data = pd.read_csv(f"{DATA_DIR}/stock_prices")
    stocks = get_tickers()
    nans = data.isna().any()
    for i, v in enumerate(nans.values):
         if v:
             print(f"{i} {v} {stocks[i]}")
    return data.dropna(axis=1)

def get_bond_return():
    data = web.DataReader(['AGG'], data_source='yahoo',start='2017-01-01', end='2019-01-01')['Adj Close']
    return data.pct_change().mean()[0]