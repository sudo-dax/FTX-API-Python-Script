import datetime
import requests
import pandas as pd
from client import FtxClient
from local_settings import ftx as local_settings

# API FOR ALL MARKETS
# GET /markets
api_url = 'https://ftx.com/api'
api = '/markets'
url = api_url + api
markets = requests.get(url).json()
data = markets['result']
df = pd.DataFrame(data)
df = df.set_index('name')
# print(df.iloc[:,4].head())


# API FOR SINGLE MARKET
# GET /markets/{market_name}
market_name = 'ETH/USD'
path = f'/markets/{market_name}'
url = api_url + path
res = requests.get(url).json()
df = pd.DataFrame(res)['result']
# print(df)

# API FOR HISTORICAL DATA
# GET /markets/{market_name}/candles?resolution={resolution}&start_time={start_time}&end_time={end_time}
resolution = 60 * 60 * 24
start = datetime.datetime(2022,2,1).timestamp()
path = f'/markets/{market_name}/candles?resolution={resolution}&start={start}'
url = api_url + path
res = requests.get(url).json()
df = pd.DataFrame(res['result'])
df['date'] = pd.to_datetime(df['startTime'])
df = df.set_index('date')
df = df.drop(columns = ['startTime', 'time'])
# print(df.head())

# GET ORDER BOOK DATA
# GET /markets/{market_name}/orderbook?depth={depth}
depth = 20
path =  f'/markets/{market_name}/orderbook?depth={depth}'
url = api_url + path
url

'https://ftx.us/api/markets/ETH/USD/orderbook?depth=20'

res = requests.get(url).json()
bids = pd.DataFrame(res['result']['bids'])
asks = pd.DataFrame(res['result']['asks'])
bids.columns = ['Bid Price', 'Bid Amount']
asks.columns = ['Ask Price','Ask Amount']
df = pd.merge(bids, asks, left_index=True, right_index=True)
# print(df.head())

# GET TRADES
# GET /markets/{market_name}/trades
path = f'/markets/{market_name}/trades'
url = api_url + path
res = requests.get(url).json()
df = pd.DataFrame(res['result'])
print(df.head())
