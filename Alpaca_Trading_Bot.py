import alpaca_trade_api as tradeapi 
from Login_Information_Confidential import API_Key_ID,Secret_Key

alpaca_endpoint = 'https://paper-api.alpaca.markets'
api = tradeapi.REST(API_Key_ID,Secret_Key,alpaca_endpoint)
account = api.get_account()

print(account.status)