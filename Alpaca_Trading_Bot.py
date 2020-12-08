import alpaca_trade_api as tradeapi 
from Login_Information_Confidential import API_Key_ID,Secret_Key

# Alpaca Component 
class Broker:
    def __init__(self,API_Key,Secret_Key):
        self.alpaca_endpoint = 'https://paper-api.alpaca.markets'
        self.Key = API_Key
        self.Secret_Key = Secret_Key
        self.api = tradeapi.REST(self.Key, self.Secret_Key, self.alpaca_endpoint) # Send request over to Alpaca with my login information.
        self.Stock ="IVV" # Currently bot only works on a single stock. 

    def LoginStatus(self):
        account = self.api.get_account() 
        print(account.status) # Must say ACTIVE for successful connection.
        print("My name is Yasteera!")

### Communicate order to Alpaca ###
order = Broker(API_Key_ID,Secret_Key)
order.LoginStatus()