from test_new_ma import main as send_message
import time
from get_news import get_news
from investing import Investing
while True:   
    i = Investing('http://investing.com/economic-calendar/')
    if not i.news():
        try:    
            send_message()
        except Exception as e:
            print('Error: ', str(e))
    time.sleep(900)