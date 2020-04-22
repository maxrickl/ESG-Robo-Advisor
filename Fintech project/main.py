#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 10:38:44 2020

@author: francescatenan
"""

import matplotlib.pyplot as plt
import numpy as np
import stock_portfolio
import utils
import sys
from pandas_datareader import data as web
# score = int(sys.argv[1])
score = 28
stck_weight = (score-1)/(46-1)
bond_weight = 1 - stck_weight

stck_port = stock_portfolio.get_max_portfolio()
stck_return = stck_port.ret * stck_weight * 252 * 100
bond_return = utils.get_bond_return() * bond_weight * 252 * 100

print("Stock weight: %.2f%%" % (stck_weight*100))
print("Bond weight: %.2f%%" % (bond_weight*100))
print("Stock return: %.4f%%" % stck_return)
print("Bond return: %.4f%%" % bond_return)
print("Cumulative: %.4f%%" % (stck_return + bond_return))

#cumulative returns

# #plot graph
# fig = plt.figure()
# ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
# ax1.plot(cumulative_ret)
# ax1.set_xlabel('Date')
# ax1.set_ylabel("Cumulative Returns")
# ax1.set_title("Portfolio Sharpe Cumulative Returns")
# plt.show();

# cumulative_ret.to_excel("output.xlsx")
