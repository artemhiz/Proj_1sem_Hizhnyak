# Программа показывает уникальные числа в списке и удваивает числа больше пяти
from random import randint as random
l = [random(0, 20) for i in range(20)]
print("Изначальный список:         ", l)

unique = set(l)
unique = list(unique)
print("Кол-во уникальных элементов:", len(unique) + 1)

l = [i * 2 if i > 5 else i for i in l]
print("Удвоенные числа больше пяти:", l)
