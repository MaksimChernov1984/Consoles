#код, написанный для изучения библиотеки tkinter
from tkinter import *
from tkinter.ttk import Combobox #выпадающий список


#окно
window = Tk()
window.title('Любимый поисковик')
window.geometry('900x300')
window['bg']='#2F4F4F'

#верхний отступ
lbl = Label(window, text=' ', bg='#2F4F4F')
lbl.grid(column=1, row=0)

#начало текста
lbl = Label(window, text='   Мой любимый поисковик - ', font=(16), fg='#fff', bg='#2F4F4F')
lbl.grid(column=1, row=1)

#выпадающий список
combo = Combobox(window)
combo['values'] = ('(выберите)', 'Google', 'Яндекс')
combo.current(0)
combo.grid(column=2, row=1)

#надпись
lbl = Label(window, text=' , потому что ', font=(16), fg='#fff', bg='#2F4F4F')
lbl.grid(column=3, row=1)

#ввод текста
txt = Entry(window, width=30)
txt.grid(column=4, row=1)
txt.focus()

#промежуток
lbl = Label(window, text=' ', font=(16), fg='#fff', bg='#2F4F4F')
lbl.grid(column=0, row=2)

#появляется надпись при клике, и это должно быть перед кнопкой
def clicked():
    res = 'Моя любимая поисковая система - ' + combo.get() + ', \nпотому что ' + txt.get() + '.'
    lbl.configure(text=res, font='16', fg='#fff', bg='#2F4F4F')
    lbl.grid(row=5, columnspan=1+2+3+4)

#кнопка
btn = Button(window, text='Проверить', bg='#CD5C5C', fg='#fff', command=clicked)
btn.grid(column=1, row=3)

#промежуток
lbl = Label(window, text=' ', font=(16), fg='#fff', bg='#2F4F4F')
lbl.grid(column=1, row=4)

window.mainloop()