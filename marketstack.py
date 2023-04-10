import requests
import os
import json
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('MARKET_STACK_API_KEY')

BASE_URL = "http://api.marketstack.com/v1/"

def get_stock_price(stock_symbol):
    params = {
        'access_key': API_KEY
    }
    end_point = ''.join([BASE_URL, "tickers/", stock_symbol, "/intraday/latest"])

    api_result = requests.get(end_point, params)
    json_results = json.loads(api_result.text)
    if json_results:
        rs = f"The last price of {stock_symbol} is ${json_results['last']}"
        return rs
    else:
        return "This is not listed in stock market."

