a = []
while True:
    n = int(input('Введите кол-во элементов в списке: '))
    if n >= 15:
        print('Ошибка ввода')
    else:
        break

while n:
    a.append(int(input('Введите число: ')))
    n -= 1

b = []
o = 3
while o <= len(a) - 1:
    try:
        b.append(a[o])
        o += 3
    except:
        pass