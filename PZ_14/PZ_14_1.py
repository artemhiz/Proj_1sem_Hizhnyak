import re

slashdatefind = re.compile(r'\n([0-9]{2}/02/[0-9]{2})', re.S)
dotdatefind = re.compile(r'\n([0-9]{2}\.02\.[0-9]{2})', re.S)
with open('dates', 'r') as ori:
    f = ori.read()
    slashdates = slashdatefind.findall(f)
    print('ДД/ММ/ГГГГ:', len(slashdates))
    dotdates = dotdatefind.findall(f)
    print('ДД.ММ.ГГГГ:', len(dotdates))

    with open('result', 'w') as destination:
        pass