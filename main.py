from tkinter import *
from tkinter.ttk import *
import sqlite3
from sqlite3 import Error
import csv

window = Tk()
window.title('Заметки')
w = window.winfo_screenwidth()
h = window.winfo_screenheight()
w = w // 2  # середина экрана
h = h // 2
w = w - 300  # смещение от середины
h = h - 200
window.geometry('600x350+{}+{}'.format(w, h))  # задали размеры окна to center window
window.resizable(False, False)  #отключение возможности раскрыть окно наполную или растянуть


def newform():  #создание нвой заметки
    window = Tk()
    window.title('Новая заметка')
    w = window.winfo_screenwidth()
    h = window.winfo_screenheight()
    w = w // 2  # середина экрана
    h = h // 2
    w = w - 300  # смещение от середины
    h = h - 200
    window.geometry('600x350+{}+{}'.format(w, h))  # задали размеры окна to center window
    window.resizable(False, False)  # отключение возможности раскрыть окно наполную или растянуть

    Label(window, text="Введите название заметки:").grid(row=0, column=0, columnspan=1,padx=20, pady=20,sticky=W)
    Entry(window).grid(row=0, column=1, columnspan=5)

    Label(window, text='Содержание заметки: ').grid(row=1, column=0, sticky=W, padx=20)
    Text(window,width=80, height=15).grid(row=2, column=0,columnspan=10,rowspan=3,padx=20)

    Button(window, text='Сохранить', command=savenotes).grid(row=11, column=0, sticky=W, padx=20, pady=20)
    window.mainloop()

def savenotes():    #сохранение данный введеных в заметки
    pass

def delform():  # удаление заметки из программы
    pass

def change():  # удаление заметки из программы
    pass

def connection_db():    #create db and connect
    def create_connection(db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)

        return conn

    def create_table(conn, create_table_sql):
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    def main():
        database = r"dictionary_my.db"
        # описание столбцов словаря - id номер, слово и значение
        sql_create_dictionary_table = """ CREATE TABLE IF NOT EXISTS dictionary (
                                            id integer PRIMARY KEY,
                                            word text,
                                            meaning text); """

        # подключение к базе
        conn = create_connection(database)

        # создание таблицы dictionary
        if conn is not None:
            create_table(conn, sql_create_dictionary_table)
        else:
            print("Ошибка: не удалось подключиться к базе.")

    if __name__ == '__main__':
        main()

 #def get_words():
 #       query = 'SELECT * FROM dictionary ORDER BY word DESC'
 #       db_rows = self.run_query(query)
 #       # формирование словаря из перемешанных в случайном порядке слов и их значений
 #       lst_left, lst_right = [], []
 #       for row in db_rows:
 #           lst_left.append(row[1])
 #           lst_right.append(row[2])
 #       dic = dict(zip(lst_left, lst_right))
 #       # заполнение правой и левой колонок
 #       for k, v in dic.items():
 #           self.left.insert(END, k)
#          self.right.insert(END, v)


def dbase():
    #если это первый запуск, то создать базу днных файл и поместить туда первую запись как образец
    #если это второй старт базаданных уже создана, то прочитать и выгрузить на страницу
    #добавить возможность внесения записи и сохранения
    #добавить воможность удаления записи
    pass

button = Button(window, text='New', command=newform)
button.grid(row=1, column=0)

button = Button(window, text='Delete', command=delform)
button.grid(row=1, column=1)

button = Button(window, text='Change', command=change)
button.grid(row=2, column=0,columnspan=2,sticky=E+W+N)

left_box = Listbox(height = 16, exportselection=False).grid(row=3, column=0, columnspan=2)
right_box = Text(window,width=53, height=25).grid(row=0, column=2,columnspan=6,rowspan=10,padx=20)  #сам текст заметок
#right_box.bind("<<ListboxSelect>>", callback_right)
#left_box.bind("<<ListboxSelect>>", callback_left)


connection_db()
window.mainloop()
