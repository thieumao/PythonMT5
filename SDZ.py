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

currentPrice = 0
while (True):
    time.sleep(1)
    price = mt5.symbol_info_tick(symbol).ask
    if price != currentPrice:
        currentPrice = price
        count = count + 1
        point = mt5.symbol_info(symbol).point
        print(">> ", count, ", price = ", price, ", point = ", point)
    # if isDemandZone():
    #     buy()
    # elif isSupplyZone():
    #     sell()
    # print(mt5.symbol_info_tick(symbol).last)
