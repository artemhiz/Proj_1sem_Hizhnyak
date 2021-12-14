shops = {'Магистр': {'Лермонтов', 'Достоевский', 'Пушкин', 'Тютчев'},
         'ДомКниги': {'Толстой', 'Грибоедов', 'Чехов', 'Пушкин'},
         'Букмаркет': {'Пушкин', 'Достоевский', 'Маяковский'},
         'Галерея': {'Чехов', 'Тютчев', 'Пушкин'}}


def runprog():
    s = 0
    foundin = list()
    for e, i in shops.items():
        if search in i:
            s += 1
            foundin.append(e)

    if s > 0:
        print('Автор по запросу найден в', 'магазине:' if s == 1 else 'магазинах:', foundin)
    else:
        print('Автор по запросу не найден. Переформируйте запрос и повторите попытку.')


if input('Режим выполнения программы (введите латинскую А для автоматического выполнения): ') == 'A':
    for a in ('Пушкин', 'Тютчев'):
        search = a
        print('Введите интересующего автора: ' + a)
        runprog()
else:
    while True:
        search = input('Введите интересующего автора: ')
        runprog()