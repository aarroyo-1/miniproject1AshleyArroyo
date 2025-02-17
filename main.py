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
import pprint
import yfinance as yf

#tickers Amazon, Spotify, Ebay, Google, Microsoft
mytickers = ["AMZN", "SPOT", "EBAY", "GOOG", "MSFT"]

mydata = {}

mytickers.sort()
for ticker in mytickers:
    result = yf.Ticker(ticker)
    mydata[ticker] = {'ticker': ticker,
                      'dailyHigh': result.info['dayHigh']
                        }
pprint.pprint(mydata)