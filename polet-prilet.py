# код, написанный для изучения библиотеки tkinter
from tkinter import *
from tkinter.ttk import Combobox  # выпадающий список


def check():
    resume1.config(text='Цель назначения - ' +
                      destination.get() + '\nКоличество человек - ' +
                      passengers.get() + '\nКоличество груза в тоннах - ' +
                      cargo.get() + '\nТариф - ' + tariff.get())


def priced():
   # коэффициенты
    p = int(passengers.get())  # количество пассажиров
    c = int(cargo.get())  # масса груза в тоннах
    rub = 100_000  # рублей за единичный коэффициент

        # коэффициенты цели назначения
    if destination.get() == 'Луна':
        d = 1
    elif destination.get() == 'Марс':
        d = 2
    elif destination.get() == 'Седна':
        d = 3
    elif destination.get() == 'Ганимед':
        d = 4
    elif destination.get() == 'Титан':
        d = 5

        # коэффициенты тарифа
    if tariff.get() == 'простой':
        t = 1
    elif tariff.get() == 'быстрый':
        t = 2
    elif tariff.get() == 'супербыстрый':
        t = 3

    price = d * p * c * t * rub
    price2 = '{0:,}'.format(price).replace(',', ' ')
    resume2.config(text=price2)

# окно
window = Tk()
window.title('Полетели Прилетели')
window.geometry('500x700')

x = 10  # отступ по х
y = 10  # отступ по у
f = '#fff'  # цвет текста
b = '#002'  # цвет текста

window['bg'] = b

#заголовок
lbl = Label(window, font=16, fg=f, bg=b)
lbl.configure(text='Вас приветствует компания "ПОЛЕТЕЛИ ПРИЛЕТЕЛИ"!')
lbl.grid(columnspan=1+2, row=0, padx=2*x, pady=2*y)


# цель назначения
lbl = Label(window, font=16, fg=f, bg=b)
lbl.configure(text='Куда летим?')
lbl.grid(column=0, row=1, padx=x, pady=y)

destination = Combobox(window, width=11)
destination['values'] = ('(выберите)', 'Луна', 'Марс', 'Седна', 'Ганимед', 'Титан')
destination.current(0)
destination.grid(column=1, row=1, padx=x, pady=y)


# количество пассажиров
lbl = Label(window, font=16, fg=f, bg=b)
lbl.configure(text='Сколько человек? (максимум 20)')
lbl.grid(column=0, row=2, padx=x, pady=y)

passengers = Spinbox(window, from_=1, to=20, width=10)
passengers.grid(column=1, row=2, padx=x, pady=y)


# количество тонн груза
lbl = Label(window, font=16, fg=f, bg=b)
lbl.configure(text='Сколько тонн груза?')
lbl.grid(column=0, row=3, padx=x, pady=y)

cargo = Entry(window, width=11)
cargo.grid(column=1, row=3, padx=x, pady=y)


# выбор тарифа
lbl = Label(window, font=16, fg=f, bg=b)
lbl.configure(text='Тариф')
lbl.grid(column=0, row=4, padx=x, pady=y)

tariff = Combobox(window, width=11)
tariff['values'] = ('(выберите)', 'простой', 'быстрый', 'супербыстрый')
tariff.current(0)
tariff.grid(column=1, row=4, padx=x, pady=y)


# проверка условий
btn_check = Button(window, text='Проверить условия', bg='#DDA0DD', fg='#000', command=check)
btn_check.grid(columnspan=1+2, row=5, padx=x, pady=y*1.5)

resume1 = Label(window, text='Проверка условий.', font='16', fg=f, bg=b)
resume1.grid(columnspan=1+2, row=6, padx=x, pady=y)


# стоимость
btn_check = Button(window, text='Рассчитать стоимость', bg='#DDA0DD', fg='#000', command=priced)
btn_check.grid(columnspan=1+2, row=7, padx=x, pady=y*1.5)

resume2 = Label(window, text='Проверка стоимости.', font='16', fg=f, bg=b)
resume2.grid(columnspan=1+2, row=8, padx=x, pady=y)


# кнопка Полетели
btn_exit = Button(window, text="Полетели!", bg='#f0f', fg='#000', command=window.destroy)
btn_exit.grid(columnspan=1+2, row=9, padx=x, pady=y)

window.mainloop()