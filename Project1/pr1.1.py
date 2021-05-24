import math
def func(x, y, z):
    first = math.pow(x, 8) + 20*math.pow(y, 2)
    second = math.cos(z) + math.pow(z, 2) - 58
    third = 34*math.pow(y, 6) + math.pow(y, 8)/76
    fourth = x + math.log(z) - 67
    fifth = math.tan(x) - y - 27
    result = first/second - math.sqrt(third/fourth) - math.sqrt(fifth)
    return('%.2e' % result)
print(func(68, -91, 77))
print(func(73, -95, 82))