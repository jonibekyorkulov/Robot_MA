import MetaTrader5 as mt5


def login_func(login, server, password):
    if not mt5.initialize(login=login, server=server, password=password):
        print("initialize() failed, error code =",mt5.last_error())
 
    authorized=mt5.login(login=login, server=server, password=password)  
    if authorized:
        print(f"connected to account #{login}")
    else:
        print(f"failed to connect at account #{login}, error code: {mt5.last_error()}")