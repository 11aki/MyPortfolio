
import yfinance as yf
import cryptocompare
from prettyprinter import pprint
import requests

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


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
        'limit':'50',
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
        


#print(currentPrice('DOGE'))


