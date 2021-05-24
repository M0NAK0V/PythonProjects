import math
def f(n):
    if (n == 0):
        return 6
    elif (n == 1):
        return 6
    else:
        return (math.sin(f(n-2)) + 1/41*f(n-1))

print('%.2e' % f(11))
print('%.2e' % f(13))