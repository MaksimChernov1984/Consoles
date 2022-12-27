#код, написанный для изучения библиотеки tkinter
from tkinter import *
from tkinter.ttk import Combobox #выпадающий список


#окно
window = Tk()
window.title('Любимый поисковик')
window.geometry('600x300')
window['bg']='#2F4F4F'

#верхний отступ
lbl = Label(window, text=' ', bg='#2F4F4F')
lbl.grid(column=1, row=0)

#начало текста
lbl = Label(window, text='   Назовите любимый поисковик ', font=(16), fg='#fff', bg='#2F4F4F')
lbl.grid(column=1, row=1)

#выпадающий список
combo = Combobox(window)
combo['values'] = ('(выберите)', 'Google', 'Яндекс', 'Mail.ru', 'Yahoo!', 'Web.de', 'Рамблер')
combo.current(0)
combo.grid(column=2, row=1)

#промежуток
lbl = Label(window, text=' ', font=(16), fg='#fff', bg='#2F4F4F')
lbl.grid(column=1, row=2)

#надпись
lbl = Label(window, text='   Назовите причину ', font=(16), fg='#fff', bg='#2F4F4F')
lbl.grid(column=1, row=3)

#ввод текста
txt = Entry(window, width=30)
txt.grid(column=2, row=3)
txt.focus()

#промежуток
lbl = Label(window, text=' ', font=(16), fg='#fff', bg='#2F4F4F')
lbl.grid(column=1, row=4)

#надпись сколько баллов
lbl = Label(window, text='Сколько баллов из 10', font=(16), fg='#fff', bg='#2F4F4F')
lbl.grid(column=1, row=5)

#количество баллов
spin = Spinbox(window, from_=1, to=10, width=5)
spin.grid(column=2, row=5)
#spin.current(10)

#промежуток
lbl = Label(window, text=' ', font=(16), fg='#fff', bg='#2F4F4F')
lbl.grid(column=1, row=6)

#появляется надпись при клике, и это должно быть перед кнопкой
def clicked():
    res = 'Моя любимая поисковая система - ' + combo.get() + ', \nпотому ' \
        'что ' + txt.get() + '. \nКоличество баллов, которые я бы ему дал - ' + spin.get() + '.'
    lbl.configure(text=res, font='16', fg='#fff', bg='#2F4F4F')
    lbl.grid(columnspan=1+2+3+4, row=10)

#кнопка
btn = Button(window, text='Проверить', bg='#CD5C5C', fg='#fff', command=clicked)
btn.grid(column=1, row=7)

#промежуток
lbl = Label(window, text=' ', font=(16), fg='#fff', bg='#2F4F4F')
lbl.grid(column=1, row=8)

window.mainloop()