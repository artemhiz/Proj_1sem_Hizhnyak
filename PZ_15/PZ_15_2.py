# Программа удваивает значение столбца, порядковый номер которого вводится с клавиатуры
# ПРИМЕЧАНИЕ: счёт столбцов начинается с 1
from random import randint as random
import re
a = [[random(0, 1) for i in range(0, 5)] for e in range(0, random(2, 4))]
print("Изначальная матрица: ", re.sub(',', '', re.sub('( \[)|(\]\])', '', re.sub('(\[\[)|(\],)', '\n', str(a)))))

while True:
    n = int(input('\nВведите порядковый номер столбца: ')) - 1
    if n <= 0:
        print('Введите значение больше ноля')
    else: break
a = [[a[i][j] * 2 if j == n else a[i][j] for j in range(len(a[0]))] for i in range(len(a))]
print("\nИтоговая матрица:    ", re.sub(',', '', re.sub('( \[)|(\]\])', '', re.sub('(\[\[)|(\],)', '\n', str(a)))))
