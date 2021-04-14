def f(x):
    a = x & 0b1111111111
    x >>= 10
    a <<= 8

    b = x & 0b1111111111111
    x >>= 13
    b <<= 18

    c = x & 0b11111111
    x >>= 8
    c <<= 0

    d = x & 0b1
    x >>= 1
    d <<= 31
    return d | b | a | c

print(hex(f(0x4e18e80c)))
print(hex(f(0x8e5c392d)))