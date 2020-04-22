#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 10:38:44 2020

@author: francescatenan
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader as web

#  Assets to be included in the portfolio
tickers = ['AAPL','AMZN','MSFT', 'WMT']

# Asset weights
wts = [0.296223,0.442899,0.812707,0.439760]

price_data = web.DataReader(tickers,data_source='yahoo',start='01/01/2018', end='01/01/2020')['Adj Close']
                             
ret_data = price_data.pct_change()[1:]

weighted_returns = (wts * ret_data)
#print(weighted_returns.head())

port_ret = weighted_returns.sum(axis=1)
# axis =1 tells pandas we want to add
# the rows
#print(port_ret)

weight_sharpe_port= (5-1)/(17-1)
#print('weight of sharpe portfolio is', weight_sharpe_port)

weight_riskfree_port= 1- weight_sharpe_port
#print('weight of risk free is', weight_riskfree_port)

#list of stocks in portfolio
stocks = ['GOOGL']

#download daily price data for each of the stocks in the portfolio
data = web.DataReader(stocks,data_source='yahoo',start='01/01/2018', end='01/01/2020')['Adj Close']

data.sort_index(inplace=True)

#convert daily stock prices into daily returns
returns_bond = data.pct_change()
#returns_bond = returns_bond.dropna()

weighted_bond_ret = weight_riskfree_port * returns_bond
#print(weighted_bond_ret)

#final portfolio returns
weighted_Sport_ret= weight_sharpe_port * port_ret
#print (weighted_Sport_ret)

frame = {'Sharpe port return':weighted_Sport_ret}
portfolio_sharpe = pd.DataFrame(frame)
#print(portfolio_sharpe)

final_frame= pd.concat([portfolio_sharpe, weighted_bond_ret], axis=1)[1:]
#print(final_frame)

totret= final_frame.sum(axis=1)
#print(totret)

#cumulative returns
cumulative_ret = (totret + 1).cumprod()

#plot graph
fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
ax1.plot(cumulative_ret)
ax1.set_xlabel('Date')
ax1.set_ylabel("Cumulative Returns")
ax1.set_title("Portfolio Sharpe Cumulative Returns")
plt.show();

cumulative_ret.to_excel("output.xlsx")





