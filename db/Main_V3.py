import tkinter as tk
from tkinter import ttk
import sqlite3 as sq


class Main(tk.Frame):

    """Класс для главного окна"""

    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#a0dea0', bd=4)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="./plus.gif")
        self.btn_open_dialog = tk.Button(toolbar, text='Добавить игрока', command=self.open_dialog, bg='#5da130', bd=0,
                                    compound=tk.TOP, image=self.add_img)
        self.btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file="./edit.gif")
        btn_edit_dialog = tk.Button(toolbar, text="Править", command=self.open_update_dialog, bg='#5da130',
                                    bd=0, compound=tk.TOP, image=self.update_img)
        btn_edit_dialog.pack(side=tk.LEFT)

        self.find_img = tk.PhotoImage(file="./Find.gif")
        btn_find_dialog = tk.Button(toolbar, text="Искать", command=self.open_find_dialog, bg='#5da130',
                                    bd=0, compound=tk.TOP, image=self.find_img)
        btn_find_dialog.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('user_id', 'name', 'sex', 'old', 'score'), height=15, show='headings')

        self.tree.column('user_id', width=50, anchor=tk.CENTER)
        self.tree.column('name', width=180, anchor=tk.CENTER)
        self.tree.column('sex', width=140, anchor=tk.CENTER)
        self.tree.column('old', width=140, anchor=tk.CENTER)
        self.tree.column('score', width=140, anchor=tk.CENTER)

        self.tree.heading('user_id', text='ID')
        self.tree.heading('name', text='Имя игрока')
        self.tree.heading('sex', text='Пол игрока')
        self.tree.heading('old', text='Возраст игрока')
        self.tree.heading('score', text='Результат игрока')

        self.tree.pack()

    def records(self, user_id, name, sex, old, score):
        self.db.insert_data(user_id, name, sex, old, score)
        self.view_records()

    def update_record(self, user_id, name, sex, old, score):
        self.db.cur.execute("""UPDATE users SET user_id=?, name=?, sex=?, old=?, score=? WHERE user_id=?""",
                            (user_id, name, sex, old, score, self.tree.set(self.tree.selection()[0], '#1')))
        self.db.con.commit()

        self.view_records()

    def view_records(self):
        self.db.cur.execute("""SELECT * FROM users""")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def open_dialog(self):
        Child(root, app)

    def open_update_dialog(self):
        Update()

    def open_find_dialog(self):
        Find()


class Child(tk.Toplevel):

    """Класс для дочернего окна"""

    def __init__(self, root, app):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить игрока')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_description = tk.Label(self, text='Номер')
        label_description.place(x=50, y=25)
        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=110, y=25)

        label_name = tk.Label(self, text='Имя')
        label_name.place(x=50, y=50)
        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=110, y=50)

        label_sex = tk.Label(self, text='Пол')
        label_sex.place(x=50, y=75)
        self.combobox = ttk.Combobox(self, values=[u'Мужской', u'Женский'])
        self.combobox.current(0)
        self.combobox.place(x=110, y=75)

        label_old = tk.Label(self, text='Возраст')
        label_old.place(x=50, y=100)
        self.entry_old = ttk.Entry(self)
        self.entry_old.place(x=110, y=100)

        label_score = tk.Label(self, text='Результат')
        label_score.place(x=50, y=125)
        self.entry_score = ttk.Entry(self)
        self.entry_score.place(x=110, y=125)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=170)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_description.get(),
                                                                       self.entry_name.get(),
                                                                       self.combobox.get(),
                                                                       self.entry_old.get(),
                                                                       self.entry_score.get()))

        self.grab_set()
        self.focus_set()


class Update(Child):
    def __init__(self):
        super().__init__(root, app)
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title("Редактировать запись")
        btn_edit = ttk.Button(self, text="Редактировать")
        btn_edit.place(x=205, y=170)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_description.get(),
                                                                          self.entry_name.get(),
                                                                          self.combobox.get(),
                                                                          self.entry_old.get(),
                                                                          self.entry_score.get()))
        self.btn_ok.destroy()


class Find(tk.Toplevel):

    """Класс окна поиска"""

    def __init__(self):
        super().__init__(root)
        self.init_find()
        self.view = app

    def init_find(self):
        self.title("Найти игрока")
        self.geometry('400x150')
        find_label = tk.Label(self, text='Поиск')
        find_label.place(x=50, y=50)
        self.find_entry = ttk.Entry(self, width=25)
        self.find_entry.place(x=100, y=50)
        btn_find = ttk.Button(self, text="Искать")
        btn_find.place(x=100, y=100)
        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=200, y=100)


class DB:
    def __init__(self):

        with sq.connect('./saper.db') as self.con:
            self.cur = self.con.cursor()
            self.cur.execute("""CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                sex INTEGER NOT NULL DEFAULT 1,
                old INTEGER,
                score INTEGER
                )""")

    def insert_data(self, user_id, name, sex, old, score):
        self.cur.execute("""INSERT INTO users(user_id, name, sex, old, score) VALUES (?, ?, ?, ?, ?)""",
                             (user_id, name, sex, old, score))
        self.con.commit()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Работа с базой данных Сапер")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()