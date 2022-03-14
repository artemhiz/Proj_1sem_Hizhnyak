from random import randint as random
a = [[random(0, 9) for i in range(0, 20)] for e in range(0, random(2, 4))]
print("Изначальная матрица: ", a)
n = int(input("Введите номер столбца: "))
a[(e for e in range(len(a)))][(n - 1)] *= 2
print("Итоговая матрица:    ", a)