import math
def func(x, y, z):
    first = 57*(math.pow(y, 4) + math.sin(z))
    second = 21*(math.pow(y, 5) - 30*(math.pow(z, 2)))
    third = (math.pow(z, 7) - 53*(math.pow(y, 8)))
    fourth = (math.pow(x, 4) - math.sin(z))
    fifth = (math.pow(y, 6) - (math.pow(x, 7)))
    result = first/second - third + fourth/fifth
    return('%.2e' % result)
print(func(15, 59, 39))
print(func(-59, -54, 17))