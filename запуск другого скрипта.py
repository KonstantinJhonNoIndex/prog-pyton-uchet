#Запуск другого скрипта

from tkinter import * #Импорт модуля tkinter

import subprocess #Подключаем модуль субпроцессов

class button_test:
    def __init__(self):
        self.but = Button(root,
                          text = "вызов скрипта буттон_тест")
        self.but.bind("<Button-1>",self.button_test)
        self.but.grid(row=0,column=0,padx=30,pady=10)
    def button_test(self,event):
        subprocess.run('python button_test.py') #Вызываем субпроцесс

root = Tk() #Создание главного окна надпись
root.title("Проргамма тест") #Шапка окна

obj = button_test()

from menu_top.py import menu_top

root.mainloop() #отобразить окно, данная строчка кода должна быть всегда в конце скрипта

#Конец
