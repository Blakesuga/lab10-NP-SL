# https://github.com/Blakesuga/lab10-NP-SL
# Partner 1: Natania Philippe
# Partner 2: Seth Lea

import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        return b / a

    except:
        if a == 0:
            raise ZeroDivisionError

def log(a, b):
    try:
        return math.log(b, a)

    except:
        if b <= 0:
            raise ValueError

def logarithm(a, b):
    try:
        return math.log(b, a)
    except:
        if b <= 0:
            raise ValueError

def exp(a, b):
    return math.pow(a, b)

def square_root (a):
    try:
        return math.sqrt(a)

    except:
        if a < 0:
            raise ValueError

# hypotenuse function
def hypotenuse(a, b):
    return math.hypot(a, b)