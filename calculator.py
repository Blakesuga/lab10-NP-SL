import math

<<<<<<< HEAD
def add(a, b):
    return a + b

<<<<<<< HEAD
# square root function
def square_root (a):
    try:
        return math.sqrt(a)

    except:
        if a < 0:
            raise ValueError

# hypotenuse function
def hypotenuse(a, b):
    return math.hypot(a, b)


# add function
def add(a, b): 
    a + b


# sub function
=======
>>>>>>> a3f1a1d933f4fde3ea7536c81e75bf90d931dd2b


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

def square_root (a):
    try:
        return math.sqrt(a)

    except:
        if a < 0:
            raise ValueError

# hypotenuse function
def hypotenuse(a, b):
    return math.hypot(a, b)