# Программа переводит все символы верхнего регистра в нижний
a = "Я ОБОжАЮ ИНТЕРНЕТ И РОСсИЮ РОССИЯ ВПеРДЕ УРа УрА уРА УрА УРа УрА уРА УрА УРа УрА"
print("Оригинал:       ", a)
def aaa():
    yield from [i.lower() if i.isupper() else i for i in a]

print("Итоговый текст: ", "".join(aaa()))
