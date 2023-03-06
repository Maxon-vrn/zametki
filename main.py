from tkinter import *
from tkinter.ttk import *


window = Tk()
window.title('Заметки')
w = window.winfo_screenwidth()
h = window.winfo_screenheight()
w = w // 2  # середина экрана
h = h // 2
w = w - 300  # смещение от середины
h = h - 200
#window.minsize(600, 400)
# window.maxsize(550, 350)
window.geometry('600x350+{}+{}'.format(w, h))  # задали размеры окна to center window
window.resizable(False, False)  #отключение возможности раскрыть окно наполную или растянуть
#photo = PhotoImage(file='./data/index.png')  # create object photo
#window.iconphoto(False, photo)
# window.config(bg='#464646')  # цвет фона окна


window.mainloop()
