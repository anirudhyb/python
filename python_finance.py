#!/usr/local/opt/python/libexec/bin/python
# https://pythonprogramming.net/stock-data-manipulation-python-programming-for-finance/
# https://www.journaldev.com/16140/python-system-command-os-subprocess-call
# https://www.programcreek.com/python/example/92134/pandas_datareader.data.DataReader

# Review this for how to create various technical indicators in Python 
# https://blog.quantinsti.com/basic-operations-stock-data-using-python/
# https://blog.quantinsti.com/build-technical-indicators-in-python/

#Open - When the stock market opens in the morning for trading, what was the price of one share?
#High - over the course of the trading day, what was the highest value for that day?
#Low - over the course of the trading day, what was the lowest value for that day?
#Close - When the trading day was over, what was the final price?
#Volume - For that day, how many shares were traded?
#Adj Close - Stock Splits.  it accounts for future stock splits, and
#            gives the relative price to splits.  For this reason, the adjusted
#            prices are the prices you're most likely to be dealing with.

import os
import subprocess
import logging
import sys
import shutil
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2015, 1, 1)
end = dt.datetime.now()

# Closing near the 20-day SMA (Simple Moving Average)
ndays = 20

Stock_Symbols = ["CSCO", "T", "ACAD"]

# Dump all the stock data files into the DIR: ./STOCK_DATA"
#cmd="mkdir -p STOCK_DATA/"
#os.system(cmd)
STOCK_DATA = os.getcwd() + '/' + 'STOCK_DATA'
LOGS_DIR  = os.getcwd() + '/' + 'logs'
if not os.path.exists(STOCK_DATA):
        os.makedirs(STOCK_DATA)

# First delete the logs dir, and then create it. -- clean slate
if os.path.exists(LOGS_DIR):
        shutil.rmtree(LOGS_DIR)

if not os.path.exists(LOGS_DIR):
        os.makedirs(LOGS_DIR)

# Python Logger function:
def init_logging():
    rootLogger = logging.getLogger('my_logger')

    LOG_DIR = os.getcwd() + '/' + 'logs'
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
    fileHandler = logging.FileHandler("{0}/{1}.log".format(LOG_DIR, "g2"))
    rootLogger.addHandler(fileHandler)

    rootLogger.setLevel(logging.DEBUG)

    consoleHandler = logging.StreamHandler()
    rootLogger.addHandler(consoleHandler)

    return rootLogger

def Stock_Price_Print():
# Instead of yahoo -- you can use: iex, quandl, 
	for stksym in Stock_Symbols:
		df = web.DataReader(stksym, 'yahoo', start, end)
		df.reset_index(inplace=True)
		df.set_index("Date", inplace=True)
		# Number of rows in the data set
	#	print(df['Close'].count())
		# maximum close price that was reached in the given period? 
		max_price = df['Close'].max()
	#	print(max_price)
		# Max Closing Price date: 
		max_close_price_date=df.Close[df.Close == max_price].index
	#	if df['Close'] == max_price: 
	#		mycut=pd.cut(max_close_price_date, 3);
	#		print(mycut);
#		print("\n" + stksym + ":", "Max Close Price:", max_price, "On", max_close_price_date)
		print("\n" + stksym + ":", "Max Close Price:", max_price);
#		logger.debug(stk_data);
	#	print(df.head())
	#	print(df.tail())
		csv_stksym="STOCK_DATA" + "/" + stksym + "." + "csv"
		df.to_csv(csv_stksym)
	# Read from CSV: df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)
	#	df.plot()
	#	plt.show()
	#	df['Adj Close'].plot()
	#	plt.show()
	#	print(df[['High','Low']].tail())
	
	# # Deleting the "Adj Close" column
		del df['Adj Close']
		SMA = pd.Series((df['Close']).rolling(window=ndays).mean(),name = 'SMA') 
		df = df.join(SMA)
		# Higher trade Quantity
		Avg_vol = pd.Series((df['Volume']).rolling(window=5).mean(),name = '5day_AvgVol')
		df = df.join(Avg_vol)
	# Only print the last 7 entries...
		print(df.tail(7))
#		stkfile.write(df.tail(7)) 

def Finance_Main():
#	logger.debug('Execute the Stock Price print routine')
	# Print the stock price.
	Stock_Price_Print();

# Finally call the Main function
stkfile = open(LOGS_DIR + "/stkinfo.txt", "a+")
stkfile.write("My test message")
logger = init_logging();
Finance_Main();
stkfile.close();
