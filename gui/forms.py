from tkinter import *
from tkinter import messagebox
from lib.models import DataModel


class MainWindow(object):

    def __init__(self):
        self._model = DataModel()
        self._model.load_data()

        self._root = Tk()
        self._img = PhotoImage(file='world.png')
        self._logo = Label(self._root)

        self._label1 = Label(self._root)
        self._label2 = Label(self._root)
        self._entry1 = Entry(self._root)
        self._entry2 = Entry(self._root)

        self._button1 = Button(self._root)
        self._button2 = Button(self._root)
        self._button3 = Button(self._root)
        self._button4 = Button(self._root)

    def config(self):
        self._root.title('Обучающая программа <Страны-Столицы>')
        self._root.geometry('450x270+0+0')
        self._root.resizable(False, False)

        self._label1.config(text='Страна:')
        self._label2.config(text='Столица:')

        self._entry1.config(justify='center')
        self._entry2.config(justify='center')

        self._img = self._img.subsample(2, 2)
        self._logo.config(image=self._img)

        self._button1.config(text='Найти')
        self._button2.config(text='Добавить')
        self._button3.config(text='Удалить')
        self._button4.config(text='Очистить')

    def layout(self):
        self._logo.place(relx=0.02, rely=0.04)

        self._label1.place(relx=0.61, rely=0.06)
        self._label2.place(relx=0.61, rely=0.24)

        self._entry1.place(relx=0.61, rely=0.15, relwidth=0.33)
        self._entry2.place(relx=0.61, rely=0.34, relwidth=0.33)

        self._button1.place(relx=0.61, rely=0.45, relwidth=0.33)
        self._button2.place(relx=0.61, rely=0.55, relwidth=0.33)
        self._button3.place(relx=0.61, rely=0.65, relwidth=0.33)
        self._button4.place(relx=0.61, rely=0.75, relwidth=0.33)

    def search(self, event):
        print(event)
        country = self._entry1.get()
        capital = self._entry2.get()
        if country == '' and capital == '':
            messagebox.showwarning('Предупреждение', 'Вы не ввели страну')
        elif country != '' and capital == '':
            self._entry2.delete(0, END)
            self._entry2.insert(0, self._model.search_rec(country))
        elif country == '' and capital != '':
            self._entry1.delete(0, END)
            self._entry1.insert(0, self._model.search_rec(capital))
        else:
            messagebox.showwarning('Предупреждение', 'Одно из полей должно остаться пустым!')

    def to_add(self, event):
        print(event)
        country = self._entry1.get()
        capital = self._entry2.get()
        if country == '' or capital == '':
            messagebox.showwarning('Предупреждение', 'Вы не ввели всех данных')
        else:
            self._model.add_rec(country, capital)
            messagebox.showinfo('Сообщение', 'Данные успешно добавлены!')

    def to_pop(self, event):
        print(event)
        country = self._entry1.get()
        capital = self._entry2.get()
        if country == '' and capital == '':
            messagebox.showwarning('Предупреждение', 'Вы не ввели всех данных')
        elif country != '' and capital == '':
            if self._model.del_rec(country):
                messagebox.showinfo('Сообщение', 'Данные не найдены!')
            else:
                messagebox.showinfo('Сообщение', 'Данные успешно удалены!')
        elif country == '' and capital != '':
            if self._model.del_rec(capital):
                messagebox.showinfo('Сообщение', 'Данные не найдены!')
            else:
                messagebox.showinfo('Сообщение', 'Данные успешно удалены!')
        else:
            messagebox.showwarning('Предупреждение', 'Одно из полей должно остаться пустым!')

    def clear(self, event):
        print(event)
        self._entry1.delete(0, END)
        self._entry2.delete(0, END)

    def bind(self):
        self._button1.bind('<Button-1>', self.search)
        self._button2.bind('<Button-1>', self.to_add)
        self._button3.bind('<Button-1>', self.to_pop)
        self._button4.bind('<Button-1>', self.clear)

    def run(self):
        self.config()
        self.layout()
        self.bind()
        self._root.mainloop()
