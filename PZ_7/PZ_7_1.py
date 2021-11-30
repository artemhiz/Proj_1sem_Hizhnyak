# Программа подставляет в строку S перед искомой буквой C заданую строку S0
from random import randint
c = chr(randint(65, 90))
print('Искомая буква: ' + c)

s0 = ' ' + chr(randint(65, 90)) + ' '
print('К искомой букве приписывается "' + s0 + '"')

n = randint(5, 119)
s = ''
while n:
    s += chr(randint(65, 90))
    n -= 1
print('Данный текст: ' + s)

ans = ''
for i in range(len(s)):
    if s[i] == c:
        ans += s0
    ans += s[i]
print('Итог-й текст: ' + ans)
