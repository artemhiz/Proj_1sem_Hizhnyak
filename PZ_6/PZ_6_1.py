# Программа выводит на экран только нечетные элементы списка
import random
a = []
n = int(input('Введите количество элементов в списке: '))

while n:
    a.append(random.randint(0, 100))
    n -= 1
print(a)
b = []
for i in range(len(a)):
    if (i + 1) % 2 != 0:
       b.append(a[i])
b.sort()

Max = b[-1]
index = int
for i in range(len(a) - 1):
    if a[i] == Max:
        index = i

print('Максимальное значение у элемента №', index + 1, '=', Max)
