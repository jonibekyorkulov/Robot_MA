import MetaTrader5 as mt5
from order_close import close_position




def create_order(symbol, order_type):
    if order_type == "Buy":
        positions=mt5.positions_get(symbol=symbol)
        filling_modes = mt5.symbol_info(symbol).filling_mode

        if filling_modes & mt5.ORDER_FILLING_FOK:
            filling_type = mt5.ORDER_FILLING_FOK
        elif filling_modes & mt5.ORDER_FILLING_IOC:
            filling_type = mt5.ORDER_FILLING_IOC
        else:
            print("No supported filling modes")
            return False
       
        if len(positions)>0:
            if positions[0].type == mt5.ORDER_TYPE_BUY:
                return False

            elif positions[0].type == mt5.ORDER_TYPE_SELL:
                close_position(symbol)
        
        trade_type = mt5.ORDER_TYPE_BUY

        symbol = symbol
        symbol_info = mt5.symbol_info(symbol)
        if symbol_info is None:
            print(symbol, "not found, can not call order_check()")
            
   
        if not symbol_info.visible:
            print(symbol, "is not visible, trying to switch on")
            if not mt5.symbol_select(symbol,True):
                print("symbol_select({}}) failed, exit",symbol)
        
        lot = 0.01
        point = mt5.symbol_info(symbol).point
        price = mt5.symbol_info_tick(symbol).ask
        deviation = 20

        risk_percentage = 0.07

        
        
        request_1 = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": 0.02,
            "type": trade_type,
            "price": price,
            "sl": price - 2500 * point,
            "tp": price + 3000 * point,
            "deviation": deviation,
            "magic": 234000,
            "comment": "order creade",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": filling_type,
        }

        request_2 = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": lot,
            "type": trade_type,
            "price": price,
            "sl": price - 2500 * point,
            "tp": price + 7500 * point,
            "deviation": deviation,
            "magic": 234000,
            "comment": "order creade",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": filling_type,
        }

        request_3 = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": lot,
            "type": trade_type,
            "price": price,
            "sl": price - 2500 * point,
            "deviation": deviation,
            "magic": 234000,
            "comment": "order creade",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": filling_type,
        }

        
    
        result = mt5.order_send(request_1)
        result = mt5.order_send(request_2)
        result = mt5.order_send(request_3)
        print("1. order_send(): by {} {} lots at {} with deviation={} points".format(symbol,lot,price,deviation))

        if result.retcode != mt5.TRADE_RETCODE_DONE:
            print("2. order_send failed, retcode={}".format(result.retcode))
            result_dict=result._asdict()
            for field in result_dict.keys():
                print("   {}={}".format(field,result_dict[field]))
                if field=="request":
                    traderequest_dict=result_dict[field]._asdict()
                    for tradereq_filed in traderequest_dict:
                        print("       traderequest: {}={}".format(tradereq_filed,traderequest_dict[tradereq_filed]))
            print("shutdown() and quit")
            
        return True
            






    elif order_type == "Sell":
        positions=mt5.positions_get(symbol=symbol)
        
       
        if len(positions)>0:
            if positions[0].type == mt5.ORDER_TYPE_BUY:
                close_position(symbol)

           
            elif positions[0].type == mt5.ORDER_TYPE_SELL:
                return False

        trade_type = mt5.ORDER_TYPE_SELL


        symbol = symbol
        symbol_info = mt5.symbol_info(symbol)
        if symbol_info is None:
            print(symbol, "not found, can not call order_check()")
            
        
        if not symbol_info.visible:
            print(symbol, "is not visible, trying to switch on")
            if not mt5.symbol_select(symbol,True):
                print("symbol_select({}}) failed, exit",symbol)
                
        filling_type = mt5.symbol_info(symbol).filling_mode
        risk_percentage = 0.07


        lot = 0.01
        point = mt5.symbol_info(symbol).point
        price = mt5.symbol_info_tick(symbol).ask
        deviation = 20
        request_1 = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": 0.02,
            "type": mt5.ORDER_TYPE_SELL,
            "price": mt5.symbol_info_tick(symbol).bid,
            "sl": price + 2500 * point,
            "tp": price - 3000 * point,
            "deviation": deviation,
            "type_filling": mt5.ORDER_FILLING_IOC,
            "type_time": mt5.ORDER_TIME_GTC
        }

        request_2 = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": lot,
            "type": mt5.ORDER_TYPE_SELL,
            "price": mt5.symbol_info_tick(symbol).bid,
            "sl": price + 2500 * point,
            "tp": price - 7500 * point,
            "deviation": deviation,
            "type_filling": mt5.ORDER_FILLING_IOC,
            "type_time": mt5.ORDER_TIME_GTC
        }

        request_3 = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": lot,
            "type": mt5.ORDER_TYPE_SELL,
            "price": mt5.symbol_info_tick(symbol).bid,
            "sl": price + 2500 * point,
            "deviation": deviation,
            "type_filling": mt5.ORDER_FILLING_IOC,
            "type_time": mt5.ORDER_TIME_GTC
        }

        result = mt5.order_send(request_1)
        result = mt5.order_send(request_2)
        result = mt5.order_send(request_3)
        print("1. order_send(): by {} {} lots at {} with deviation={} points".format(symbol,lot,price,deviation))
        if result.retcode != mt5.TRADE_RETCODE_DONE:
            print("2. order_send failed, retcode={}".format(result.retcode))
            result_dict=result._asdict()
            for field in result_dict.keys():
                print("   {}={}".format(field,result_dict[field]))
                if field=="request":
                    traderequest_dict=result_dict[field]._asdict()
                    for tradereq_filed in traderequest_dict:
                        print("       traderequest: {}={}".format(tradereq_filed,traderequest_dict[tradereq_filed]))
            print("shutdown() and quit")

        return True


    else:
        print("Noto'g'ri harakat")
        return False

