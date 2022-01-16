# Программа создает два файла, а из них - третий, основываясь на условиях, описаных в FfPZ_10_1_3
l = ['12 -8 32 76 -58 -7 123 124']
f1 = open('FfPZ_10_1_1', 'w')
f1.writelines(l)
f1 = open('FfPZ_10_1_1', 'r')

l2 = ['35 64 -65 76 12 -14 68']
f2 = open('FfPZ_10_1_2', 'w')
f2.writelines(l2)
f2 = open('FfPZ_10_1_2', 'r')

f3 = open('FfPZ_10_1_3', 'w')
a = f1.read()
a = a.split()
for i in a:
    i = int(i)
b = f2.read()
b = b.split()
for e in b:
    e = int(e)

c = 0
for i in a:
    for e in b:
        if i == e:
            c += 1

f3.write('All elements together:' + '\n')
for i in a:
    f3.write(i + ' ')
for i in b:
    f3.write(i + ' ')
f3.write('\n' + 'Quantity of elements in each file: ' + '\n' + str(len(a)) + ' ' + str(len(b)))
f3.write('\n' + 'Quantity of elements existing in both files:' + '\n' + str(c))

even = len(a) // 2 if len(a) // 2 != 0 else (len(a) // 2) + 1
odd = len(b) // 2 if len(b) // 2 == 0 else (len(b) // 2) + 1

f3.write('\n' + 'Quantity of even elements in the 1st file: ' + '\n' + str(even))
f3.write('\n' + 'Quantity of odd elements in the 2nd file: ' + '\n' + str(odd))
