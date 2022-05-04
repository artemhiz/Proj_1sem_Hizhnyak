from tkinter import *


def calculate():
    try:
        n = int(entry.get())
        k = 0
        s = 0
        while k <= n:
            s += (n + k) * (n + k)
            k += 1
        answer['text'] = 'n^2 + (n+1)^2 + ... + 2n^2 = '+str(s)
    except ValueError:
        answer['text'] = 'Ошибка ввода данных. \nВведите целое число'


root = Tk()
root.title('n^2 + (n+1)^2 + (n+2)^2 ... 2n^2')
root.geometry('0x0')
root.minsize(width=400, height=100)
root.maxsize(width=500, height=100)

label = Label(root, text='Введите число:', anchor='e', width=15)
entry = Entry(root, width=20)
button = Button(root, text='Calculate!', command=calculate)
answer = Label(root)

label.grid(column=0, row=0)
entry.grid(column=1, row=0)
button.grid(column=1, row=1)
answer.grid(column=1, row=2)

root.mainloop()
