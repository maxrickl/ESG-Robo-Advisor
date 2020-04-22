# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 12:28:52 2020

@author: maxri
"""

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from pandas_datareader import data as web
from datetime import datetime as dt
import stock_portfolio
import utils
import numpy as np


score = 28
total_amount = 100000
stck_weight = (score-1)/(46-1)
bond_weight = 1 - stck_weight
stck_amount = total_amount * stck_weight
bond_amount = total_amount * bond_weight


stck_port = stock_portfolio.get_max_portfolio()
prices = utils.get_price_matrix()

sel_prices = np.dot(prices, stck_port[3:].T)
sel_prices = sel_prices / sel_prices[0] * stck_amount

bond = web.DataReader(['AGG'], data_source='yahoo',start='2018-01-01', end='2020-01-01')['Adj Close']
bond = bond / bond.values[0] * bond_amount
bond = bond.AGG

returns = np.diff(sel_prices) / sel_prices[1:]


df = web.DataReader("^GSPC", "yahoo", dt(2019, 1, 1), dt(2020, 1, 1))["Adj Close"]
change = df.pct_change()

app = dash.Dash("Sample Dash")

app.layout = html.Div(
    [
        dcc.Graph(
            figure={
                "data": [
                    {"x": change.index, "y": change, "name": "S&P 500"},
                    {"x": change.index, "y": returns, "name": "Selected Porfolio"},
                ],
                "layout": {"margin": {"l": 40, "r": 0, "t": 20, "b": 30}},
            }
        ),
        dcc.Graph(
            figure={
                "data": [
                    {"x": df.index, "y": sel_prices + bond, "name": "Selected"},
                ],
                "layout": {"margin": {"l": 40, "r": 0, "t": 20, "b": 30}},
            }
        ),
    
        ],
    style={"width": "500"},
)


if __name__ == "__main__":
    app.run_server()
