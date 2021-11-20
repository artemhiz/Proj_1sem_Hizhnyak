# Функция добавляет введенное число слева. Функция вызвана в программе дважды, последовательно показаны шаги решения
def countdig(k):
    a = 1
    while k // 10 != 0:
        k = k // 10
        a += 1
    return a


def addleftdigit(d, k):
    if 0 < d < 10:
        k += d * (10 ** countdig(K))
        return k
    else:
        print('Произошла ошибка во время рассчета. Проверьте введенные данные и попробуйте еще раз.')
        return None


K = int(input('Введите цифру К:'))
D1 = int(input('Введите D1:'))
D2 = int(input('Введите D2:'))

print(addleftdigit(D1, K))
print(addleftdigit(D2, addleftdigit(D1, K)))
