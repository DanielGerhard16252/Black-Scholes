from Getting_Data import get_data
import numpy as np
import yfinance as yf
from scipy.stats import norm


data = get_data()

# For this example we assume the mean and standard deviation to be constant
# Here we calculate all the parameters we require for the Black-Scholes equation
mean = np.mean(data)*252
sd = np.std(data)*np.sqrt(252)
rf_interest = mean + sd**2/2
current_price = yf.Ticker('NVDA').history()['Close'].iloc[-1]
strike_price = [124 + i for i in range(20)]
time_until_expirery = 8/252

# We now calculate the d1 and d2 in the Black-Scholes model
d1 = np.log(current_price/strike_price) + time_until_expirery*(rf_interest + sd**2/2)/(sd*np.sqrt(time_until_expirery))
d2 = np.log(current_price/strike_price) + time_until_expirery*(rf_interest - sd**2/2)/(sd*np.sqrt(time_until_expirery))

# Finally we substitute the values into the central equation
Call_Price = current_price * norm.cdf(d1) - strike_price * norm.cdf(d2)*np.e**(-rf_interest*time_until_expirery)
print(Call_Price)