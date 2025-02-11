import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

# The companies we want to get stock market data for

def get_data():
    tickers = ['NVDA']
    
    data_daily = np.array([])
    for each in tickers:

        # Getting the daily open price for the last two years
        req = yf.Ticker(each)
        data = req.history(period = '2y', interval = '1d')['Open']

        data_daily = np.concatenate((data_daily, data))
        
    continuous_returns = []
    
    # Converting the data from prices into continuous returns
    for i in range(len(data)-1):
        continuous_returns.append(np.log(data[i+1]/data[i]))

    return continuous_returns


