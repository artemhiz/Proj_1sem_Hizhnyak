# Программа анализирует расположение точки по х и у и возвращает истину, если точка находится в I или II четверти
while True:
    try:
        print('"Точка расположена в первой или третьей четвертях" - истина или ложь?')
        x = float(input('Введите х = '))
        y = float(input('Введите у = '))
        if (x > 0 and y > 0) or (x < 0 and y < 0):  # находится ли точка в первой или в третьей четвертях
            print('Истина')
        else:
            print('Ложь')
        break
    except ValueError:  # Проверка исключений
        print('Ошибка ввода. Введите целочисленное значение')
