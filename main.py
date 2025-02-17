### INF601 - Advanced Programming in Python
### Ashley Guadalupe Tarin Arroyo
### Mini Project 1

'''
INF601 - Programming in Python
Assignment #
I,  Ashley Guadalupe Tarin Arroyo , affirm that the work submitted for this assignment is entirely my own.
I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism,
or the use of unauthorized materials. I have neither provided nor received unauthorized assistance and have
accurately cited all sources in adherence to academic standards. I understand that failing to comply with this
integrity statement may result in consequences, including disciplinary actions as determined by my course instructor
 and outlined in institutional policies. By signing this statement, I acknowledge my commitment to upholding the
 principles of academic integrity.
'''

#Imports
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

#tickers Amazon, Spotify, Ebay, Google, Microsoft
mytickers = ["AMZN", "SPOT", "EBAY", "GOOG", "MSFT"]


mytickers.sort()
for ticker in mytickers:
    result = yf.Ticker(ticker)
    hist = result.history(period="10d")
    last10days =[]
    for date in hist["Close"][:10]:
        last10days.append(date)
    if len(last10days) ==10:
        myarray = np.array(last10days)
        max_price = myarray.max() + (myarray.max()*.05)
        min_price = myarray.min() - (myarray.min()*.05)
        plt.plot(myarray)
        plt.xlabel('Days Ago')
        plt.axis((9, 0, min_price, max_price))
        plt.ylabel('The Closing Price')
        plt.title(f"{ticker} Last 10 Days Price")
        plt.savefig(f"charts/{ticker}.png")
    else:
        print(f"Do not have 10 days of data. Only have {len(last10days)} days.")
