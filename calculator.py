import math

def add(a, b):
    return a + b

def sub(a, b):
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

def exp(a, b):
    return math.pow(a, b)


