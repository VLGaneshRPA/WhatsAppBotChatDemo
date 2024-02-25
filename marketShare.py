import requests

params = {
  'access_key': 'dba6a70e212d75664a0cd82df113ae47'
}

BASE_URL = 'http://api.marketstack.com/v1/'

def getStockPrice(stock_Symbol):
    endPoint = ''.join([BASE_URL,'tickers/',stock_Symbol,'/intraday/latest'])
    api_result = requests.get(endPoint, params)
    api_response = api_result.json()
    #print(api_response.get('open'))
   # return{
   #     'OpenPrice' : str(api_response['open']),
   #     'LastPrice' : str(api_response['last'])
   # }
    return str(api_response['last'])


print(getStockPrice(stock_Symbol='AAPL'))