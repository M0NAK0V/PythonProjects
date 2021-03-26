def f(x):
    a = x & 0b11111111111111
    x >>= 14
    a <<= 0

    b = x & 0b1111111
    x >>= 7
    b <<= 25

    c = x & 0b111111111
    x >>= 9
    c <<= 14

    d = x & 0b11
    x >>= 2
    d <<= 23
    return b | d | c | a

print(hex(f(0x272f25e7)))
print(hex(f(0xf15660af)))