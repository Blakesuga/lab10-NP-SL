"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math


# add function
def add(a, b): 
    a + b


# sub function
def sub(a, b):
    return a - b


# mul function
def mul(a, b):
    return a * b


# div function
def div(a, b):
    try:
        return b / a

    except:
        if a == 0:
            raise ZeroDivisionError


# log function
def log(a, b):

    try:
        return math.log(b, a)

    except:
        if a == 0:
            raise ValueError

# expo function
def exp(a, b):
    return math.pow(a, b)
