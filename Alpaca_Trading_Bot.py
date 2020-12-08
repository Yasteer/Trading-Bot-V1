import alpaca_trade_api as tradeapi 
from Login_Information_Confidential import API_Key_ID,Secret_Key

## Alpaca Component ##
class Broker:
    def __init__(self,API_Key,Secret_Key):
        self.alpaca_endpoint = 'https://paper-api.alpaca.markets'
        self.Key = API_Key
        self.Secret_Key = Secret_Key
        self.api = tradeapi.REST(self.Key, self.Secret_Key, self.alpaca_endpoint) # Send request over to Alpaca with my login information.
        self.Stock ="IVV" # Currently bot only works on a single stock. 
        self.Quanity = 5
        self.PurchasePrice = 0

    def LoginStatus(self):
        account = self.api.get_account() 
        print(account.status) # Must say ACTIVE for successful connection.

    def BuyStock(self, Stock, Quanity):
        # Market order to make the purchase as soon as possible.
        self.api.submit_order(self.Stock, self.Quanity, 'buy', 'market', 'day')
        self.PurchasePrice = 0

    def SellStock(self, Stock, Quanity):
        # Limit order to only make a sale when a certain maximum/minimum limit is met.
        SalePrice = self.PurchasePrice + self.PurchasePrice*0.1 # 10% Markup to cover costs.
        self.api.submit_order(self.Stock, self.Quanity, 'sell', 'limit', 'opg', SalePrice)

## Trading Algorithm ##


### Communicate order to Alpaca ###
order = Broker(API_Key_ID,Secret_Key)
order.LoginStatus()