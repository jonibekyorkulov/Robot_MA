import MetaTrader5 as mt5

def close_position(symbol):
    positions = mt5.positions_get(symbol=symbol)
    
    for position in positions:
        mt5.Close(symbol,ticket=position.ticket)
   
    return True