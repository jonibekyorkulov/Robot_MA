from test_new_ma import main as send_message
import time
while True:   
       
        
        try:    
            send_message()
        except Exception as e:
            print('Error: ', str(e))
        time.sleep(900)  