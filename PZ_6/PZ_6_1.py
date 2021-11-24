a = []
n = int(input('Введите количество элементов в списке:'))

while n:
    a.append(input('Введите число:'))
    n -= 1

delist = []
for i in range(len(a) - 1):
    if i % 2 == 0:
        delist.append(i)

for i in delist:
    del a[i]


max = a[0]
index = 0
k = 0

for i in a:
    k += 1
    if i > max:
        max = i
        index = k + 1
print('Максимальное значение в списке у элемента', index, '=', max)
