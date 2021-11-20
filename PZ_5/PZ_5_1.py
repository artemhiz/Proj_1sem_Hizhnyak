def countdig(k):
    b = k
    a = 1
    while b // 10 != 0:
        b = b // 10
        a += 1
    return a


def sumdig(k):
    a = countdig(k)
    b = 0
    while a:
        b += k // (10 ** (a - 1)) % 10
        a -= 1
    return b


def mindig(k):
    a = 0
    while k > 0:
        k -= sumdig(k)
        a += 1
    return a


print('Число станет равно нулю через', mindig(int(input('Введите целое число:'))), 'разностей.')