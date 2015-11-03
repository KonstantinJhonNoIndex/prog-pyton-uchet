
#-------------------------------------------
# объектно-ориентированный подход

from tkinter import * #Импорт модуля tkinter

class But_print: #создали класс бут_принт для ООП (объектно-ориентированное программирование)
     def __init__(self):
          self.but = Button(root,
                            text = "текст кнопки в окне на пайтон", #надпись на кнопке
                            width = 30, height=5, #ширина и высота
                            bg = "white", fg= "blue") #цвет фона и надписи виджета
          self.but.bind("<Button>",self.printer) #Событие нажатия левой кнопкой мыши выглядит так: <Button-1>.
                                                 #Требуется связать это событие с обработчиком (функцией printer)
                                                 #Для связи предназначен метод bind
          self.but.grid(row=0,column=1,padx=20,pady=10)
     def printer(self,event): #печать на экран будет оформлена в виде функции printer функцию обязательно размещать в начале кода, параметр event – это какое-либо событие
          print ("Как всегда очередной 'Hello World!'")

class text_window:
    def __init__(self):
        self.lab = Label(root,
                         font = "Arial 25") #шрифт и размер букв в надписи
        self.lab["text"] = "Это метка  !!!!!!!!!!!!!!!!!!!!!!!!!!! \n Из двух строк . \n из 3-х строк" #просто строка с тремя строчками
        self.lab.grid(row = 0,
                      column = 2,
                      padx = 20,
                      pady = 10) #отобразить надпись в окне

class text_input: #создали класс для поля ввода текста
    def __init__(self):
        self.ent = Entry(root,
                         width = 20, bd = 3) #текстовое поле сокращение от borderwidth (ширина границы)
        self.ent.grid(row=0,column=3,padx=20,pady=10)

class text_more_input: #Многострочное текстовое поле
    def __init__(self):
        self.tex = Text(root,
                        width = 40,
                        font = "Verdana 12",
                        wrap = WORD)
        self.tex.grid(row=3,column=2,padx=20,pady=10)
 
root = Tk() #Создание главного окна надпись tk
obj = But_print() #задействовать объект бут_принт
obj = text_window() #задействовать объект окно_с_текстом
obj = text_input()
obj = text_more_input()
root.mainloop() #отобразить окно, данная строчка кода должна быть всегда в конце скрипта

#---------------------------------------------
#конец 
#
#
