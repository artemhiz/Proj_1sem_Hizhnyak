# Программа выводит на экран содержимое файла и переносит его, поместив последнюю строку между второй и третьей, в новый
# файл
f1 = open('text18-29.txt', 'r')
a = f1.read()
print(a)
a = a.split('\n')
b = 0
for i in a:
    b += len(i)
print('Кол-во символов в тексте: ' + str(b))

a.insert(2, a.pop(-1))

f2 = open('FfPZ_10_2', 'w')
for i in a:
    f2.write(str(i) + '\n')
