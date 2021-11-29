# Программа выводит только элементы списка, номер которых кратен трем
import random

a = []
while True:
    n = random.randint(0, 14)
    if n >= 15:
        print('Ошибка ввода')
    else:
        break

while n:
    a.append(random.randint(0, 15))
    n -= 1
print(a)
b = []
o = 2
while o <= len(a) - 1:
    try:
        b.append(a[o])
        o += 3
    except IndexError:
        pass
print(b)
print('В списке', len(b), 'элементов')