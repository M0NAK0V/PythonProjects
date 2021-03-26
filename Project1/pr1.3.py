import math
def f(n, m):
    pervoe = 0
    vtoroe = 0
    for i in range(n):
        for j in range(m):
            pervoe += 34 * (math.fabs(j+1) + 60 * math.pow (j+1, 5) + 73)
            vtoroe += math.tan(i+1) - (i+1) - 27
    result = pervoe + vtoroe
    return ('%.2e' % result)
print(f(67,75))
print(f(12,61))