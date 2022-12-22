import yfinance as yf
import json
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import logging
from datetime import datetime, timedelta

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
    #guard
    if(body['date'] == '' or body['date'] == None or body['ticker'] == '' or body['ticker'] == None):
        return jsonify({'error': 'invalid data'})
    # cool and fun stuff
    # I love useless comments
    wanted_date = datetime.strptime(body['date'], '%Y-%m-%d')
    one_day = wanted_date + timedelta(days=1)
    try:
        hist = yf.download(body['ticker'], start=wanted_date, end=one_day)
        return jsonify(hist.to_dict(orient='records'))
    except Exception as e:
        print(e)	    
    return jsonify(hist.to_dict(orient='records'))

#idiot testing
@app.route('/')
def home():
    print('hellooooooo')

# start
if __name__ == "__main__":
    logging.getLogger('flask_cors').leel = logging.DEBUG
    app.run(debug=True, host="0.0.0.0")
