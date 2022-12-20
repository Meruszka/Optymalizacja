def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    else:
        n = max(len(str(x)), len(str(y)))
        m = n // 2

        a, b = divmod(x, 10 ** m)
        c, d = divmod(y, 10 ** m)

        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        ad_bc = karatsuba(a + b, c + d) - ac - bd
        return 10 ** (2 * m) * ac + 10 ** m * ad_bc + bd


def test():
    x = 123456789012345678901234567890
    y = 987654321098765432109876543210
    print(karatsuba(x, y))
    print


test()
