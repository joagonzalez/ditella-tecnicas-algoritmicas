import os
import time
from datetime import datetime
from threading import Timer

def exitfunc():
    print("Exit Time", datetime.now())
    os._exit(0)

Timer(5, exitfunc).start() # exit in 5 seconds

while True: # infinite loop, replace it with your code that you want to interrupt
    print("Current Time", datetime.now())
    time.sleep(1)