'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from pandas_datareader import data as web

stock = 'MSFT'

df = web.DataReader(stock, data_source='yahoo', start='01-01-2021')

df['Adj Close'].plot(label='MSFT',figsize=(16,8),title='Adjusted Closing price')


'''


import mplfinance as fplt
import pandas as pd
from pandas_datareader import data as web
from dateutil import parser
from datetime import datetime


def historicalChart(assetname,startdate,atype):

    if atype == 'Stock':

        df = web.DataReader(assetname, data_source='yahoo', start=startdate)
        df.to_csv('stock.csv')
        plotdata = pd.read_csv('stock.csv',index_col=0,parse_dates=True)

    #crypto
    else:
        print("its ETHcrypto")
        plotdata = pd.read_csv('%s.csv' % assetname, index_col=0, parse_dates=True)

    fplt.plot(
                plotdata,
                type='candle',
                ylabel='Price ($)',
                savefig = '%s.png' % assetname
            )

historicalChart('BTC','11-01-2021','Crypt')


