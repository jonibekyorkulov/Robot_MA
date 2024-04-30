import MetaTrader5 as mt5
import talib
import numpy as np
from mt5_login import login_func
from order_create import create_order
import time


def check_variability(lst):
    if all(x == lst[0] for x in lst):
        return False
    else:
        return True


def get_signal(symbol, timeframe, ma_period_short, ma_period_long):
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, 10000)
    
    close_prices = np.array([rate['close'] for rate in rates])
    
    ma_short = talib.EMA(close_prices, ma_period_short)
    ma_long = talib.EMA(close_prices, ma_period_long)
    
    if len(ma_short) < 5 or len(ma_long) < 5:
        return False, "No Signal"

    type_signal = []
    for i in range(1, 6):

        ma_short_last = ma_short[-i]
        ma_long_last = ma_long[-i]

        if ma_short_last > ma_long_last:
            type_signal.append('Buy')
        
        if ma_short_last < ma_long_last:
            type_signal.append("Sell")

    if check_variability(type_signal): 

            return True, type_signal[0]
    
      
    
    return False, 'No Signal'


def main():
    login_func(68165721, "RoboForex-Pro", "Pass!123")
    symbol_list = ["XAUUSD"]
    
    
    for symbol in symbol_list:
        timeframe = mt5.TIMEFRAME_M15
        ma_short_period = 7
        ma_long_period = 40
        
        status, signal  = get_signal(symbol, timeframe, ma_short_period, ma_long_period)
        if status:
            create_order(symbol, signal)
            
        
        time.sleep(0.01)
   
    
    mt5.shutdown()
    return True
   