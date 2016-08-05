import GDAX


# taker fees below, maker fees are 0. See https://www.gdax.com/fees
GDAX_BTC_FEE = 0.0025
GDAX_ETH_FEE = 0.0030

api_key = raw_input('Enter your GDAX API Key: ')
api_secret = raw_input('Enter your GDAX API Secret: ')
passphrase = raw_input('Enter your passphrase: ')

public_client = GDAX.PublicClient()
auth_client = GDAX.AuthenticatedClient(key=api_key, b64secret=api_secret, passphrase=passphrase)

print auth_client.getAccounts()