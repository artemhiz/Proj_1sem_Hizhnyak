# Программа возвращает день недели, соответствующий введенному числу
while True:
    try:
        a = int(input('Введите число от 1 до 7: '))
        if a == 1:  # Сравнение с днями недели
            print('ПН')
            break
        elif a == 2:
            print('ВТ')
            break
        elif a == 3:
            print('СР')
            break
        elif a == 4:
            print('ЧТ')
            break
        elif a == 5:
            print('ПТ')
            break
        elif a == 6:
            print('СБ')
            break
        elif a == 7:
            print('ВС')
            break
        else:
            print('Ошибка ввода')
    except ValueError:  # Проверка исключений
        print('Ошибка ввода. Введите целочисленное значение')
