from test_new_ma import main as send_message
import time
from get_news import get_news
while True:   
       
    if not get_news():
        try:    
            send_message()
        except Exception as e:
            print('Error: ', str(e))
    time.sleep(900)