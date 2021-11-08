# Программа вычисляет результат в последовательности n^2 + (n+1)^2 + (n+2)^2 ... (2n)^2
while True:
    try:
        n = int(input('Введите целое число: '))
        if n > 0:
            break
        else:
            print('Ошибка ввода. Введите число больше нуля')
    except ValueError:
        print('Ошибка ввода')

ans = 0
k = 0
while k <= n:
    ans += (n + k) ** 2
    k += 1
print(ans)
