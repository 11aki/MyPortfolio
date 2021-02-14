
import yfinance as yf
import requests

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

import mplfinance as fplt
import matplotlib.pyplot as plt
plt.switch_backend('agg')

import pandas as pd
from pandas_datareader import data as web
from dateutil import parser
from datetime import datetime

#Check if the symbol exists and return a price if it does
#atype is whether it is a stock or crypto
def currentPrice(ticker,atype='Stock'):
    if atype == 'Stock':
#if its a stock
        try:
            stock = yf.Ticker(ticker)
            return stock.info['ask']
        except:
            return "not a stock"
#if its a crpyto
    else:

      url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
      parameters = {
        'start':'1',
        'limit':'500',
        'convert':'USD'
      }
      headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '786bbbd2-fff1-44d8-b11d-5ccbd080a45c',
      }

      session = Session()
      session.headers.update(headers)

      try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        for item in data['data']:
            if(item['symbol']==ticker):
              return(item['quote']['USD']['price'])
      except (ConnectionError, Timeout, TooManyRedirects) as e:
        return(e)
        


def historicalChart(assetname,startdate,atype):
    plotdata = pd.read_csv('BTC.csv', index_col=0, parse_dates=True)
    if atype == 'Stock':
        df = web.DataReader(assetname, data_source='yahoo', start=startdate)
        df.to_csv('stock.csv' )
        plotdata = pd.read_csv('stock.csv',index_col=0,parse_dates=True)
        print("ots a stock")
    #crypto
    else:
        print("its ETHcrypto")
        plotdata = pd.read_csv('ETH.csv', index_col=0, parse_dates=True)
    fplt.plot(
                plotdata,
                type='candle',
                ylabel='Price ($)',
                savefig = 'website/static/%s.png' % assetname
            )