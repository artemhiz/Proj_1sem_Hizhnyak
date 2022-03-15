# Программа находит даты, записанные в существующих форматах (ДД.ММ.ГГГГ или ДД/ММ/ГГГГ), считает их количество и
# записывает в новый файл в формате ДД/ММ/ГГГГ
import re

slashfind = re.compile(r'\n([0-9]{2}/02/[0-9]{2})', re.S)
dotfind = re.compile(r'\n([0-9]{2}\.02\.[0-9]{2})', re.S)

with open('dates', 'r') as ori:
    f = ori.read()
    slashdates = slashfind.findall(f)
    print('ДД/ММ/ГГГГ:', len(slashdates))
    dotdates = dotfind.findall(f)
    print('ДД.ММ.ГГГГ:', len(dotdates))

slashdates.extend([re.sub('\.', '/', dotdates.pop(0)) for i in range(len(dotdates))])

with open('result', 'w') as destination:
    destination.write('\n'.join(slashdates))
print('Даты перенесены в файл "result". Содержимое файла ниже:')
with open('result', 'r') as check:
    print(re.sub('\n', ', ', check.read()))
