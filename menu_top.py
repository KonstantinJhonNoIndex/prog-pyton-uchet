#Модуль меню
from tkinter import *

class menu_top:
    def __init__(self):
        menu = Menu(root)
        root.config(menu = menu)
        file_menu = Menu(menu)
        menu.add_cascade(label="Фаил", menu=file_menu)
        file_menu.add_command(label="Новый")
        file_menu.add_command(label="Открыть")
        file_menu.add_separator()
        file_menu.add_command(label="Выход", command=root.destroy)
        edit_menu = Menu(menu)
        menu.add_cascade(label="Редактировать", menu=edit_menu)
        edit_menu.add_command(label="До <-")
        edit_menu.add_separator()
        edit_menu.add_command(label="Вырезать")
        edit_menu.add_command(label="Копировать")
        edit_menu.add_command(label="Вставить")
root = Tk()
obj = menu_top()
#root.mainloop()
