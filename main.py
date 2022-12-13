import yfinance as yf
from flask import Flask, jsonify

app = Flask(__name__)

# returns all price data for ticker param
@app.route('/get/<ticker>')
def get_ticker_data(ticker):
    ticker = yf.Ticker('VTI')
    hist = ticker.history(period='max') 
    hist_json = hist.to_json()
    print(hist_json)
    return jsonify(hist_json)

#idiot testing
@app.route('/')
def home():
    print('hellooooooo')


# start
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")