import yfinance as yf
import json
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import logging

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# returns all price data for ticker param
@app.route('/get/<ticker>')
@cross_origin(origin='*')
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

@app.route('/get-one', methods=['POST'])
@cross_origin(origin='*')
def getByDateAndTicker():
    body = request.json
    print(body)
    return 'hola bitch'


#idiot testing
@app.route('/')
def home():
    print('hellooooooo')

# start
if __name__ == "__main__":
    logging.getLogger('flask_cors').leel = logging.DEBUG
    app.run(debug=True, host="0.0.0.0")
