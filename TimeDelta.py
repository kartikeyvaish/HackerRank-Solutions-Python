import math
import os
import random
import re
import sys
from datetime import datetime
import calendar
def time_delta(t1, t2):
        print(abs(int((t1 - t2).total_seconds())))

for i in range(int(input())):
    t1 = datetime.strptime("Sun 10 May 2015 13:54:36 -0000",'%a %d %b %Y %H:%M:%S %z')
    t2 = datetime.strptime("Sun 10 May 2015 13:54:36 -0700",'%a %d %b %Y %H:%M:%S %z')
    print(t1)
    print(t2)
    time_delta(t1,t2)
