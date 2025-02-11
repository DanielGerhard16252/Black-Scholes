# Black-Scholes
Fair Option Pricing and Data Analysis

Overview

This repository contains a set of Python scripts that implement financial data analysis, stock data retrieval, and option pricing using the Black-Scholes model. The scripts leverage real market data obtained via Yahoo Finance (yfinance) and perform various computations related to financial modeling and risk assessment.

Files and Functionality

Getting_Data.py

Retrieves daily open prices for selected stock tickers (currently NVIDIA: NVDA).

Converts price data into continuous returns over a two-year period.

Returns the computed continuous returns as a NumPy array.

Data_Scaling_and_Experimentation.py

Implements a function (test_function) to compute statistics (mean, standard deviation) on stock return data.

Scales the data according to a conjectured method.

Filters out outliers using the 1st and 99th percentiles.

Returns the processed dataset.

Calculating_fair_option_price_example.py

Computes option prices using the Black-Scholes formula.

Uses market data (yfinance) to fetch the latest closing price of NVDA.

Computes drift, volatility, and risk-free interest rate.

Computes d1 and d2 for the Black-Scholes model.

Outputs a list of call option prices for a range of strike prices.

Plots.py

Fetches stock return data and processes it using test_function.

Creates a histogram of normalized stock returns.

Overlays a normal distribution for comparison.

Displays the histogram and normal distribution plot.

Requirements

To run the scripts, you will need the following Python libraries:

pip install numpy scipy yfinance matplotlib

Usage

Fetch Stock Data

from Getting_Data import get_data
data = get_data()

Process Data and Remove Outliers

from Data_Scaling_and_Experimentation import test_function
filtered_data = test_function(data)

Compute and Print Option Prices

python Calculating_fair_option_price_example.py

Generate Plots

python Plots.py
