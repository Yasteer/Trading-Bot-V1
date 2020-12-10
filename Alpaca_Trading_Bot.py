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
        self.PurchasePrice = 0
        self.Current_Order = None

    def LoginStatus(self):
        account = self.api.get_account() 
        print(account.status) # Must say ACTIVE for successful connection.

    def BuyStock(self, Quanity):
        # Market order to make the purchase as soon as possible. # 
        if self.Current_Order is None:
            self.api.submit_order(self.Stock, Quanity, 'buy', 'market', 'day')
        else
            self.api.cancel_order(self.Current_Order.id)

    def SellStock(self, Quanity):
        # NB --> Setting all sales to have a long position (Don't want to obliterate myself just yet!) # 
        # Alpaca allows the user to go short by selling a stock without first owning it. #
        # As long the position > 0, we are going long. #

        # Limit order to only make a sale when a certain maximum/minimum limit is met. #
        if int(self.api.get_position(self.Stock).qty) > 0:
            SalePrice = self.PurchasePrice + self.PurchasePrice*0.1 # 10% Markup to cover costs.
            self.api.submit_order(self.Stock, Quanity, 'sell', 'limit', 'opg', SalePrice)

## Trading Algorithm ##


### Communicate order to Alpaca ###
order = Broker(API_Key_ID,Secret_Key)
order.LoginStatus()