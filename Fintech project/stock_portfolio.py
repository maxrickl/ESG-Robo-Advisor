#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 22:09:56 2020

@author: francescatenan
"""
from utils import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def get_max_portfolio():
#list of stocks in portfolio
    tickers = get_tickers()

    #download daily price data for each of the stocks in the portfolio
    data = get_price_matrix()

    returns = data.pct_change()

    #calculate mean daily return and covariance of daily returns
    mean_daily_returns = returns.mean()
    cov_matrix = returns.cov()

    #set number of runs of random portfolio weights
    PORTFOLIOS = 10000

    #set up array to hold results
    #We have increased the size of the array to hold the weight values for each stock
    results = np.zeros((len(tickers) + 3,PORTFOLIOS))

    for i in range(PORTFOLIOS):
        #select random weights for portfolio holdings
        weights = np.array(np.random.random(len(tickers)))
        #rebalance weights to sum to 1
        weights /= np.sum(weights)
        
        #calculate portfolio return and volatility
        portfolio_return = np.sum(mean_daily_returns * weights)
        portfolio_std_dev = np.sqrt(np.dot(weights.T,np.dot(cov_matrix, weights)))
        
        #store results in results array
        results[0,i] = portfolio_return
        results[1,i] = portfolio_std_dev
        #store Sharpe Ratio (return / volatility) - risk free rate element excluded for simplicity
        results[2,i] = results[0,i] / results[1,i]
        #iterate through the weight vector and add data to results array
        for j in range(len(weights)):
            results[j+3,i] = weights[j]

    #convert results array to Pandas DataFrame
    results_frame = pd.DataFrame(results.T,columns=['ret','stdev','sharpe'] + tickers)

    #locate position of portfolio with highest Sharpe Ratio
    max_sharpe_port = results_frame.iloc[results_frame['sharpe'].idxmax()]
    return max_sharpe_port
    #locate positon of portfolio with minimum standard deviation
    # min_vol_port = results_frame.iloc[results_frame['stdev'].idxmin()]

    #create scatter plot coloured by Sharpe Ratio
    plt.scatter(results_frame.stdev,results_frame.ret,c=results_frame.sharpe,cmap='RdYlBu')
    plt.xlabel('Volatility')
    plt.ylabel('Returns')
    plt.colorbar()
    # plot red star to highlight position of portfolio with highest Sharpe Ratio
    plt.scatter(max_sharpe_port[1],max_sharpe_port[0],marker=(5,1,0),color='r',s=1000)
    # #plot green star to highlight position of minimum variance portfolio
    plt.scatter(min_vol_port[1],min_vol_port[0],marker=(5,1,0),color='g',s=10)
    


