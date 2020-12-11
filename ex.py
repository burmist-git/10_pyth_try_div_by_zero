#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Date        : Fri Dec 11 12:56:00 CET 2020
Autor       : Leonid Burmistrov
Description : Simple reminder-training example.

'''

import numpy as np
import math
from itertools import combinations

def printinfo(func):
    def wrapper():
        print("")
        print("Simple reminder-training example. Function name : {} --> ".format(func.__name__))
        func()
    return wrapper

@printinfo
def div_by_zero(a=1.0):
    return a/0.0

@printinfo
def div_by_zero_try(a=1.0):
    try:
        return a/0.0
    except ZeroDivisionError: return None

def main():
    try:
        zeroDivisionVal=div_by_zero()
        print('zeroDivisionVal = ',zeroDivisionVal)
    except: pass
    zeroDivisionVal=div_by_zero_try()
    print('zeroDivisionVal = ',zeroDivisionVal)
    
if __name__ == "__main__":
    main()
