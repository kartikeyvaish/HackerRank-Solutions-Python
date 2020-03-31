#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s):
    newstr = ""
    length = len(s)
    for i in range(0, length):
        if i == 0:
            stores = ord(s[i])
            if stores >= 97 and stores <= 122:
                stores = stores - 32
                newstr = newstr + chr(stores)
            else:
                newstr = newstr + chr(stores)

        elif s[i - 1] == ' ' and s[i] != ' ':
            stores = ord(s[i])
            if stores >= 97 and stores <= 122:
                stores = stores - 32
                newstr = newstr + chr(stores)
            else:
                newstr = newstr + chr(stores)
        else:
            stores = ord(s[i])
            newstr = newstr + chr(stores)

    return newstr

s = input()
result = solve(s)
print(result)
