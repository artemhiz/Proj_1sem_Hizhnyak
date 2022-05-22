import tkinter as tk
from tkinter import ttk
import sqlite3 as sq
from tkinter import messagebox


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.pack(fill=tk.BOTH)
        self.toolbar = Toolbar(self)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)
        self.table = TableView(self)
        self.table.pack(fill=tk.BOTH)


class Toolbar(tk.Frame):
    def __init__(self, root):
        super().__init__(root, bg='#F00')

        self.add_img = tk.PhotoImage(file='./plus.gif')
        self.add_button = tk.Button(self, text='Записать', compound=tk.TOP, image=self.add_img, width=80, height=60)
        self.add_button.grid(column=0, row=0)
        self.add_button.bind('<Button-1>', lambda event: DiaWin(title='Записать', purpose='add'))

        self.edit_img = tk.PhotoImage(file='./edit.gif')
        self.edit_button = tk.Button(self, text='Править', compound=tk.TOP, image=self.edit_img, width=80, height=60)
        self.edit_button.grid(column=1, row=0)
        self.edit_button.bind('<Button-1>', lambda event: DiaWin(title='Править запись', purpose='edit'))

        self.delete_img = tk.PhotoImage(file='./delete.gif')
        self.delete_button = tk.Button(self, text='Удалить', compound=tk.TOP, image=self.delete_img, width=80,
                                       height=60)
        self.delete_button.grid(column=2, row=0)

        def send_delete_to_table():
            root.table.delete_record()

        self.delete_button.bind('<Button-1>', lambda event: send_delete_to_table())

        self.find_img = tk.PhotoImage(file='./find.gif')
        self.find_button = tk.Button(self, text='Найти', compound=tk.TOP, image=self.find_img, width=80, height=60)
        self.find_button.grid(column=3, row=0)
        self.find_button.bind('<Button-1>', lambda event: SearchWin())

        self.refresh_img = tk.PhotoImage(file='./refresh.gif')
        self.refresh_button = tk.Button(self, text='Обновить', compound=tk.TOP, image=self.refresh_img, width=80,
                                        height=60)
        self.refresh_button.grid(column=4, row=0)
        self.refresh_button.bind('<Button-1>', lambda event: root.table.refresh())


class TableView(ttk.Treeview):
    def __init__(self, root):
        with sq.connect('./DataBase.db') as self.con:
            self.cur = self.con.cursor()
            self.cur.execute("""CREATE TABLE IF NOT EXISTS Data (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        master_name TEXT NOT NULL,
                        client_name TEXT NOT NULL,
                        gender TEXT NOT NULL DEFAULT Ж,
                        service_type TEXT NOT NULL,
                        cost INTEGER NOT NULL
                        )""")
        self.cur.execute("""SELECT * FROM Data""")
        super().__init__(root, columns=('id', 'master_name', 'client_name', 'gender', 'service_type', 'cost'),
                         height=30, show='headings')

        self.column('id', width=50, anchor=tk.CENTER)
        self.column('master_name', width=150, anchor=tk.CENTER)
        self.column('client_name', width=150, anchor=tk.CENTER)
        self.column('gender', width=80, anchor=tk.CENTER)
        self.column('service_type', width=200, anchor=tk.CENTER)
        self.column('cost', width=100, anchor=tk.CENTER)

        self.heading('id', text='ID')
        self.heading('master_name', text='Имя мастера')
        self.heading('client_name', text='Имя клиента')
        self.heading('gender', text='Пол')
        self.heading('service_type', text='Услуга')
        self.heading('cost', text='Стоимость')

        self.pack()
        self.refresh()

    def refresh(self):
        self.cur.execute("""SELECT * FROM Data""")
        [self.delete(i) for i in self.get_children()]
        [self.insert('', 'end', values=row) for row in self.cur.fetchall()]

    def add_record(self, client, master, gender, service, cost):
        self.cur.execute("""INSERT INTO Data(master_name, client_name, gender, service_type, cost) 
                VALUES (?, ?, ?, ?, ?)""", (master, client, gender, service, cost))
        self.con.commit()
        self.refresh()

    def delete_record(self):
        for sel_item in self.selection():
            self.cur.execute("""DELETE FROM Data WHERE id = ?""", (self.set(sel_item, '#1')))
        self.con.commit()
        self.refresh()

    def update_record(self, master_name, client_name, gender, service_type, cost, identificator):
        self.cur.execute("""UPDATE Data SET master_name = ?, client_name = ?, gender = ?, service_type = ?, cost = ?
        WHERE id = ?""", (master_name, client_name, gender, service_type, cost, identificator))
        self.con.commit()
        self.refresh()

    def find_record(self, condition, value, condition_range='='):
        if condition == 'ID':
            if condition_range == '<':
                self.cur.execute("""SELECT * FROM Data WHERE id <:id""", {"id": value})
            elif condition_range == '≤':
                self.cur.execute("""SELECT * FROM Data WHERE id <=:id""", {"id": value})
            elif condition_range == '=':
                self.cur.execute("""SELECT * FROM Data WHERE id =:id""", {"id": value})
            elif condition_range == '≥':
                self.cur.execute("""SELECT * FROM Data WHERE id >=:id""", {"id": value})
            elif condition_range == '>':
                self.cur.execute("""SELECT * FROM Data WHERE id >:id""", {"id": value})
        elif condition == 'Имя клиента':
            self.cur.execute("""SELECT * FROM Data WHERE client_name LIKE:client""", {"client": value.capitalize()+'%'})
        elif condition == 'Имя мастера':
            self.cur.execute("""SELECT * FROM Data WHERE master_name LIKE:master""", {"master": value.capitalize()+'%'})
        elif condition == 'Пол клиента':
            self.cur.execute("""SELECT * FROM Data WHERE gender LIKE:gen""", {"gen": value.capitalize()+'%'})
        elif condition == 'Услуга':
            self.cur.execute("""SELECT * FROM Data WHERE service_type LIKE:service""",
                             {"service": value.capitalize()+'%'})
        elif condition == 'Стоимость':
            if condition_range == '<':
                self.cur.execute("""SELECT * FROM Data WHERE cost <:cost""", {"cost": value})
            elif condition_range == '≤':
                self.cur.execute("""SELECT * FROM Data WHERE cost <=:cost""", {"cost": value})
            elif condition_range == '=':
                self.cur.execute("""SELECT * FROM Data WHERE cost =:cost""", {"cost": value})
            elif condition_range == '≥':
                self.cur.execute("""SELECT * FROM Data WHERE cost >=:cost""", {"cost": value})
            elif condition_range == '>':
                self.cur.execute("""SELECT * FROM Data WHERE cost >:cost""", {"cost": value})

        [self.delete(i) for i in self.get_children()]
        [self.insert('', 'end', values=row) for row in self.cur.fetchall()]


class DiaWin(tk.Toplevel):
    def __init__(self, title, purpose):
        super().__init__()
        self.title(title)
        link = main

        if purpose == 'edit':
            self.id_frame = tk.Frame(self)
            self.id_label1 = tk.Label(self.id_frame, text='ID', anchor='e', width=10)
            self.id_label2 = tk.Label(self.id_frame, anchor='w', width=30)
            self.id_frame.pack()
            self.id_label1.grid(column=0, row=0)
            self.id_label2.grid(column=1, row=0)

        self.name = LabEntry(self, 'Имя Клиента')
        with open(file='Employees.txt', mode='r') as file:
            self.master_name = LabSelect(self, 'Мастер', file.read().split('\n'))
        self.gender = LabSelect(self, 'Пол Клиента', ['Мужской', 'Женский'])
        with open(file='Services.txt', mode='r') as file:
            self.service = LabSelect(self, 'Услуга', file.read().split('\n'))
        self.cost = LabEntry(self, 'Стоимость')

        if purpose == 'edit':
            try:
                for sel_item in link.table.selection():
                    link.table.cur.execute("""SELECT * FROM Data WHERE id = ?""", (link.table.set(sel_item, '#1')))
                self.person = link.table.cur.fetchone()

                self.id_label2['text'] = self.person[0]
                self.name.entry.insert(0, self.person[2])
                self.master_name.entry.insert(0, self.person[1])
                self.gender.entry.insert(0, self.person[3])
                self.service.entry.insert(0, self.person[4])
                self.cost.entry.insert(0, self.person[5])
            except TypeError:
                messagebox.showinfo('Info', 'Вы не выбрали запись к изменению')
                self.destroy()

        self.button_frame = tk.Frame(self)
        self.button_frame.pack()
        self.cancel = tk.Button(self.button_frame, text='Отмена', command=self.destroy)
        self.cancel.grid(column=0, row=0)

        def send_add_to_table():
            link.table.add_record(self.name.entry.get(),
                                  self.master_name.entry.get(),
                                  self.gender.entry.get(),
                                  self.service.entry.get(),
                                  self.cost.entry.get())
            self.destroy()

        def send_edit_to_table():
            link.table.update_record(self.master_name.entry.get(),
                                     self.name.entry.get(),
                                     self.gender.entry.get(),
                                     self.service.entry.get(),
                                     self.cost.entry.get(),
                                     self.id_label2['text'])
            self.destroy()

        self.ok = tk.Button(self.button_frame, text='ОК')
        if purpose == 'add':
            self.ok.bind('<Button-1>', lambda event: send_add_to_table())
        elif purpose == 'edit':
            self.ok.bind('<Button-1>', lambda event: send_edit_to_table())
        self.ok.grid(column=1, row=0)

        self.grab_set()
        self.focus_set()
        self.mainloop()


class LabEntry(tk.Frame):
    def __init__(self, root, name):
        super().__init__(root)
        self.label = tk.Label(self, text=name, width=10, anchor='e')
        self.entry = tk.Entry(self, width=30)
        self.label.grid(column=0, row=0)
        self.entry.grid(column=1, row=0)
        self.pack()


class LabSelect(tk.Frame):
    def __init__(self, root, name, list_of_values):
        super().__init__(root)
        self.label = tk.Label(self, text=name, width=10, anchor='e')
        self.entry = ttk.Combobox(self, width=30, values=list_of_values)
        self.label.grid(column=0, row=0)
        self.entry.grid(column=1, row=0)
        self.pack()


class SearchWin(tk.Toplevel):
    def __init__(self):
        super().__init__()
        link = main

        self.title('Найти')
        self.condframe = tk.Frame(self)
        self.condframe.pack()
        self.condlabel = tk.Label(self.condframe, text='Условие поиска', width=20, anchor='e')
        self.condlabel.grid(column=0, row=0)
        self.condition = ttk.Combobox(self.condframe, values=['ID', 'Имя клиента', 'Имя мастера',
                                                              'Пол клиента', 'Услуга', 'Стоимость'],
                                      width=30)
        self.condition.grid(column=1, row=0)

        self.symbframe = tk.Frame(self)
        self.symbframe.pack()
        self.symblabel = tk.Label(self.symbframe, text='Диапазон значений', width=20, anchor='e')
        self.symblabel.grid(column=0, row=0)
        self.range = ttk.Combobox(self.symbframe, values=['<', '≤', '=', '≥', '>'], width=10)
        self.range.grid(column=1, row=0)

        self.entframe = tk.Frame(self)
        self.entframe.pack()
        self.entlabel = tk.Label(self.entframe, text='Значение', width=10, anchor='e')
        self.entlabel.grid(column=0, row=0)
        self.entry = tk.Entry(self.entframe, width=30)
        self.entry.grid(column=1, row=0)

        self.butframe = tk.Frame(self)
        self.butframe.pack()
        self.cancel = tk.Button(self.butframe, text='Отмена', command=self.destroy)
        self.cancel.grid(column=0, row=0)

        def send_find_to_table():
            link.table.find_record(self.condition.get(),
                                   self.entry.get(),
                                   self.range.get())
            self.destroy()

        self.ok = tk.Button(self.butframe, text='Искать!', command=send_find_to_table)
        self.ok.grid(column=1, row=0)


if __name__ == '__main__':
    app = tk.Tk()
    app.geometry('800x600')
    app.title('Парикмахерская')
    main = Main(app)
    app.mainloop()
