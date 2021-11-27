a = []
n = int(input('Введите количество элементов в списке: '))

while n:
    a.append(input('Введите число: '))
    n -= 1

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
