from coinbase.wallet.client import Client


# taker fees below, maker fees are 0. See https://www.gdax.com/fees
GDAX_BTC_FEE = 0.0025
GDAX_ETH_FEE = 0.0030

api_key = input('Enter your Coinbase API Key: ')
api_secret = input('Enter your Coinbase API Secret: ')

client = Client(api_key, api_secret)
