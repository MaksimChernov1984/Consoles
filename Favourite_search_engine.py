#код, написанный для изучения библиотеки tkinter
from tkinter import *
from tkinter.ttk import Combobox #выпадающий список
from tkinter import messagebox #всплывающее окно
from tkinter import ttk #для кнопки Выход

#окно
window = Tk()
window.title('Любимый поисковик')
window.geometry('600x400')
window['bg']='#2F4F4F'

#верхний отступ
lbl = Label(window, text=' ', bg='#2F4F4F')
lbl.grid(column=1, row=0)

#всплывающее окно
def clicked():
    messagebox.askyesno(title='Вопрос', message='Вы любите искать информацию?')

#кнопка Вопрос
btn_ask = Button(window, text="Вопрос", bg='#CD5C5C', fg='#fff', command=clicked)
btn_ask.grid(column=1, row=2)

#отступ после кнопки Вопрос
lbl = Label(window, text=' ', bg='#2F4F4F')
lbl.grid(column=1, row=3)

#начало текста
lbl = Label(window, text='   Назовите любимый поисковик ', font=(16), fg='#fff', bg='#2F4F4F')
lbl.grid(column=1, row=4)

#выпадающий список
combo = Combobox(window)
combo['values'] = ('(выберите)', 'Google', 'Яндекс', 'Mail.ru', 'Yahoo!', 'Web.de', 'Рамблер')
combo.current(0)
combo.grid(column=2, row=4)

#отступ после выпадающего списка
lbl = Label(window, text=' ', font=(16), fg='#fff', bg='#2F4F4F')
lbl.grid(column=1, row=5)

#надпись
lbl = Label(window, text='   Назовите причину ', font=(16), fg='#fff', bg='#2F4F4F')
lbl.grid(column=1, row=6)

#ввод текста
txt = Entry(window, width=30)
txt.grid(column=2, row=6)
txt.focus()

#отступ после причины
lbl = Label(window, text=' ', font=(16), fg='#fff', bg='#2F4F4F')
lbl.grid(column=1, row=7)

#надпись сколько баллов
lbl = Label(window, text='Сколько баллов из 10', font=(16), fg='#fff', bg='#2F4F4F')
lbl.grid(column=1, row=8)

#количество баллов
spin = Spinbox(window, from_=1, to=10, width=5)
spin.grid(column=2, row=8)
#spin.current(10)

#отступ после баллов
lbl = Label(window, text=' ', font=(16), fg='#fff', bg='#2F4F4F')
lbl.grid(column=1, row=9)

#появляется надпись при клике, и это должно быть перед кнопкой
def clicked():
    res = 'Моя любимая поисковая система - ' + combo.get() + ', \nпотому ' \
        'что ' + txt.get() + '. \nКоличество баллов, которые я бы ему дал - ' + spin.get() + '.'
    lbl.configure(text=res, font='16', fg='#fff', bg='#2F4F4F')
    lbl.grid(columnspan=1+2+3+4, row=12)

#кнопка Проверить
btn_check = Button(window, text='Проверить', bg='#CD5C5C', fg='#fff', command=clicked)
btn_check.grid(column=1, row=10)

#отступ после кнопки Проверить
lbl = Label(window, text=' ', font=(16), fg='#fff', bg='#2F4F4F')
lbl.grid(column=1, row=11)

btn_exit = Button(window, text="Выход", command=window.destroy).grid(column=1, row=13)

window.mainloop()