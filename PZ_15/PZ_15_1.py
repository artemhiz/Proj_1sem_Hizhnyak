# Программа меняет все элементы последней строки матрицы на 0
from random import randint as random
l = [[random(0, 9) for i in range(0, 20)] for e in range(0, random(2, 4))]
print("Изначальная матрица: ", l)
l[-1] = [0 for s in l[-1]]
print("Итоговая матрица:    ", l)
