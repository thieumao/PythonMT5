import MetaTrader5 as mt5
import time

mt5.initialize()

symbol = 'XAUUSD'

count = 0

def isDemandZone():
    return count % 2 == 0

def isSupplyZone():
    return count % 2 == 1

def buy():
    print('Buy Action')

def sell():
    print('Sell Action')

ask = 0
bid = 0
spread = 0
while (True):
    time.sleep(1)
    currentAsk = mt5.symbol_info_tick(symbol).ask
    currentBid = mt5.symbol_info_tick(symbol).bid
    if ask != currentAsk or bid != currentBid:
        ask = currentAsk
        bid = currentBid
        point = mt5.symbol_info(symbol).point
        digits = mt5.symbol_info(symbol).digits
        spread = round(ask - bid, digits)
        count = count + 1
       
        print(count, ">> ask = ", ask, ", bid = ", bid,  ", spread = ", spread, ", digits = ", digits)
    # if isDemandZone():
    #     buy()
    # elif isSupplyZone():
    #     sell()
    # print(mt5.symbol_info_tick(symbol).last)
