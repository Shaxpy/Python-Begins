
#event.set() #sets the flag to true
#event.clear() #sets flag to false
#event.wait() #start blocking

import queue
import threading
import numpy as np
import time

def flag():
    time.sleep(3)
    event.set()
    print('starting')
    time.sleep(5)
    print('Event success')
    event.clear()
    
def start():
    event.wait() 
    while event.is_set():
        print('starting random integer task')
        x=np.random.randint(1,30)
        time.sleep(.5)
        if x==29:
            print('True')
    print('Event has been cleared')

    
event=threading.Event()
t1=threading.Thread(target=flag)
t2=threading.Thread(target=start)
t1.start()
t2.start()