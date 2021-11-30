# Программа выводит текст b, введенный между первым и последним пробелами данной строки string
from random import randint
symbols = [' ']
for i in range(65, 91):
    symbols.append(chr(i))

string = ''
for i in range(randint(30, 119)):
    string += symbols[randint(0, len(symbols) - 1)]
print(string)

b = ''
firstSp = int
lastSp = int
for i in range(len(string)):
    if string[i] == ' ' and firstSp == int:
        firstSp = i
    elif string[i] == ' ':
        lastSp = i

b = string[firstSp + 1:lastSp] if firstSp != int and lastSp != int else '[нет текста]'
print(b)
