# Программа меняет все элементы последней строки матрицы на 0
from random import randint as random
import re
l = [[random(0, 9) for i in range(0, 5)] for e in range(0, random(2, 4))]
print("Изначальная матрица: ", re.sub(',', '', re.sub('( \[)|(\]\])', '', re.sub('(\[\[)|(\],)', '\n', str(l)))))
l[-1] = [0 for s in l[-1]]
result = re.sub(',', '', re.sub('( \[)|(\]\])', '', re.sub('(\[\[)|(\],)', '\n', str(l))))
print("\nИтоговая матрица:    ", result)
