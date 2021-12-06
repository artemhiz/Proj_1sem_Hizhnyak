vcb = {'Horse': 'Лошадь', 'Immediately': 'Немедленно', 'Understandable': 'Понятно', 'Maintenance': 'Поддержка',
       'Obviously': 'Очевидно', 'Familiar': 'Знакомый', 'Thing': 'Вещь', 'Difference': 'Разница',
       'Changeable': 'Изменяемый', 'Unforgettable': 'Незабываемый'}

print('Добро пожаловать в самый маленький в мире вокабуляр! :)')
while True:
    try:
        search = input('Введите слово: ')
        if search == 'Завершить' or search == 'Quit':
            print('До свидания. Надеемся, программа подарила вам прекрасный опыт использования. :)')
            break
        print(search + ' --- ' + vcb[search])
        print('ENG' + (' ' * (len(search) + 2)) + 'RUS')
        print()
    except KeyError:
        print('Ошибка. Слова не существует в вокабуляре программы')
        print()