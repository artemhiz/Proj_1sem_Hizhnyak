# Программа выдает наименьший периметр треугольника, созданного на основе данных точек
import math
import random
X = []
Y = []
A = [X, Y]
P = []


def addpoint(x, y):
    X.append(x)
    Y.append(y)


def perimeter(x1, y1, x2, y2, x3, y3):
    a = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    b = math.sqrt(math.pow(x1 - x3, 2) + math.pow(y1 - y3, 2))
    c = math.sqrt(math.pow(x3 - x2, 2) + math.pow(y3 - y2, 2))

    p = a + b + c
    return p


n = int(input('Введите кол-во элементогв в списке: '))
while n:
    addpoint(random.randint(-15, 15), random.randint(-15, 15))
    n -= 1

print(A)
Min = 0

Min1 = ()
Min2 = ()
Min3 = ()

for i in range(len(A[0])):
    for e in range(len(A[0])):
        for s in range(len(A[0])):
            if A[0][i] != A[0][e] and A[0][i] != A[0][s] and A[0][e] != A[0][s] and A[1][i] != A[1][e] and A[1][i] != A[1][s] and A[1][e] != A[1][s]:
                P.append(perimeter(A[0][i], A[1][i], A[0][e], A[1][e], A[0][s], A[1][s]))
                if P[Min] > P[-1]:
                    Min = len(P)
                    Min1 = (A[0][i], A[1][i])
                    Min2 = (A[0][e], A[1][e])
                    Min3 = (A[0][s], A[1][s])


print('Самый маленький периметр =', P[Min], 'с точками',  Min1, Min2, Min3)
