import MetaTrader5 as mt5
from mt5_login import login_func

login_func(501032179, "RoboForex-Pro", "W-5oHuSk")

def modify_order(symbol):
    # Retrieve positions
    positions = mt5.positions_get(symbol=symbol)

    # Check if symbol exists
    symbol_info = mt5.symbol_info(symbol)
    if symbol_info is None:
        print(symbol, "not found, cannot call order_check()")
        return False

    # Check if symbol is visible
    if not symbol_info.visible:
        print(symbol, "is not visible, trying to switch on")
        if not mt5.symbol_select(symbol, True):
            print("symbol_select({}}) failed, exit", symbol)
            return False

    # Check if there's an open position
    if not positions:
        print("No open positions for", symbol)
        return False

    # Calculate stop loss
    point = mt5.symbol_info(symbol).point
    sl_price = 2280.00

    # Prepare order request
    request = {
        "action": mt5.TRADE_ACTION_SLTP,
        "position": positions[0].ticket,
        "sl": sl_price,
        "tp": 2295.00
    }

    # Send order
    result = mt5.order_check(request)
    print(result)
    result = mt5.order_send(request)
    print("1. order_send()")

    # Handle result
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print("2. order_send failed, retcode={}".format(result.retcode))
        result_dict = result._asdict()
        for field in result_dict.keys():
            print("   {}={}".format(field, result_dict[field]))
            if field == "request":
                traderequest_dict = result_dict[field]._asdict()
                for tradereq_field in traderequest_dict:
                    print("       traderequest: {}={}".format(tradereq_field, traderequest_dict[tradereq_field]))
        print("shutdown() and quit")
        return False

    return True

modify_order('XAUUSD')
