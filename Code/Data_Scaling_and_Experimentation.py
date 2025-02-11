import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt


def  test_function(arr):
    # Calculating number of data points, mean and standard deviations
    n = len(arr)
    mean = np.sum(arr)/n
    sd = np.sqrt(np.sum(np.square(arr - mean))/n)

    # Scaling the data (In this case with regards to Conjecture 1)
    data = []
    for i in range(n-1):
        data.append((arr[i+1]-mean)/np.abs((arr[i] - mean - sd)))
    
    
    # Define bounds for outliers (1st and 99th percentiles)
    lower_bound = np.percentile(data, 1)
    upper_bound = np.percentile(data, 99)

    # Remove outliers from the data
    filtered_data = [val for val in data if lower_bound <= val <= upper_bound]
    
    return filtered_data
