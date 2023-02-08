x = int(input("Напишите любую цифру, а я напишу её на испанском.  "))
while x < 10:
    if x == 1:
        y = "Uno"
    elif x == 2:
        y = "Dos"
    elif x == 3:
        y = "Tres"
    elif x == 4:
        y = "Quatro"
    elif x == 5:
        y = "Cinco"
    elif x == 6:
        y = "Seis"
    elif x == 7:
        y = "Siete"
    elif x == 8:
        y = "Ocho"
    elif x == 9:
        y = "Nueve"
    else:
        y = "Cero"
    print(y)
    x = int(input("А ещё!?  "))