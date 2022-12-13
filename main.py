import yfinance as yf
import json
from flask import Flask, jsonify

app = Flask(__name__)

# returns all price data for ticker param
@app.route('/get/<ticker>')
def get_ticker_data(ticker):
    ticker = yf.Ticker(ticker)
    hist = ticker.history(period='max') 
    hist['Dates Corrected'] = hist.index
    # initially to dict
    hist_dict = hist.to_dict(orient='records')
    # then to json
    # hist_json = json.dumps(hist_dict)
    # print(hist_json)
    return jsonify(hist_dict)

#idiot testing
@app.route('/')
def home():
    print('hellooooooo')


# start
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")