import yfinance as yf
import pandas as pd
from flask import Flask

app = Flask(__name__)

# returns all price data for ticker param
@app.route('/get/<ticker>')
def get_ticker_data(ticker):
    ticker = yf.Ticker('VTI')
    hist = ticker.history(period='max') 
    return hist.to_json()

#idiot testing
@app.route('/')
def home():
    print('hellooooooo')


# start
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")