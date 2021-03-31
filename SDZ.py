import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime
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
        goldRates = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_H1, 0, 4)
        print(goldRates)
        rates_frame = pd.DataFrame(goldRates)
        # convert time in seconds into the datetime format
        rates_frame['time']=pd.to_datetime(rates_frame['time'], unit='s')
 
        # display data
        print("\nDisplay dataframe with data")
        print(rates_frame)
    time.sleep(10)
    # if isDemandZone():
    #     buy()
    # elif isSupplyZone():
    #     sell()
    # print(mt5.symbol_info_tick(symbol).last)

# 1 >> ask =  1708.51 , bid =  1708.35 , spread =  0.16 , digits =  2
# [(1617213600, 1703.88, 1708.68, 1701.76, 1708.06, 9507, 5, 0) 
#  (1617217200, 1708.06, 1712.4 , 1707.17, 1711.87, 6949, 5, 0) 
#  (1617220800, 1711.9 , 1715.34, 1710.58, 1710.83, 6490, 5, 0) 
#  (1617224400, 1710.83, 1711.11, 1708.09, 1708.35, 3767, 5, 0)]

# Display dataframe with data
#                  time     open     high      low    close  tick_volume  spread  real_volume
# 0 2021-03-31 18:00:00  1703.88  1708.68  1701.76  1708.06         9507       5            0
# 1 2021-03-31 19:00:00  1708.06  1712.40  1707.17  1711.87         6949       5            0
# 2 2021-03-31 20:00:00  1711.90  1715.34  1710.58  1710.83         6490       5            0
# 3 2021-03-31 21:00:00  1710.83  1711.11  1708.09  1708.35         3767       5            0
