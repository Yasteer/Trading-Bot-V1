import alpaca_trade_api as tradeapi 
from Login_Information_Confidential import API_Key_ID,Secret_Key

alpaca_endpoint = 'https://paper-api.alpaca.markets'
api = tradeapi.REST(API_Key_ID,Secret_Key,alpaca_endpoint) # Send request over to Alpaca with my login information.

# Checks if connection was succesful.
account = api.get_account() 
print(account.status) # Must say ACTIVE for successful connection.