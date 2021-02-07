
import yfinance as yf
ticker = 'MSFT'

msft = yf.Ticker(ticker)

print(msft.info)