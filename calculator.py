import math

<<<<<<< HEAD
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b


def log(a, b):
    try:
        return math.log(b, a)
    except:
        if b <= 0:
            raise ValueError

def exp(a, b):
    return math.pow(a, b)