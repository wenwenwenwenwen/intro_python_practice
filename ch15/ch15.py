import multiprocessing as mp
from time import sleep
from random import randint
from datetime import datetime
import os

def print_current_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Process {os.getpid()}, current time: {current_time}")

if __name__ == "__main__":
    for n in range(3):
        p = mp.Process(target=print_current_time)
        sleep(randint(0, 5))
        p.start()