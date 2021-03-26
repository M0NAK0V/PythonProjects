import math
def f(x):
    if(x<71):
        r1 = math.pow(x, 6) + math.pow(x, 5)
        return ('%.2e' % r1)
    elif ((71 <= x) and (x < 129)):
        r2 = 30 * math.pow(x, 8) - 78 * math.pow(x, 5) + 83
        return ('%.2e' % r2)
    elif ((129 <= x) and (x < 222)):
        r3 = math.pow(x, 8) - 6 * math.pow(x, 7)
        return ('%.2e' % r3)
    elif ((222 <= x) and (x < 295)):
        r4 = math.tan(2 * math.pow(x, 6)) - math.exp(x)
        return ('%.2e' % r4)
    elif (295 <= x):
        r5 = math.pow(math.tan(x) - math.pow(x, 8), 3) + math.pow(x, 7)
        return ('%.2e' % r5)

print(f(98))
print(f(204))
