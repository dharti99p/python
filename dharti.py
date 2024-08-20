print("hii")

import datetime
import time

def get_time() :
    a = str(datetime.datetime.now())
    print(a)
    b = a.split()
    print(b)
    c = b[0].split("-")
    d = b[1].split(":")
    print(c)
    print(d)

get_time()