x = input("Напишите любую цифру, а я напишу её на испанском.  ")
d = {'1': 'Uno', 
'2': 'Dos', 
'3': 'Tres', 
'4': 'Quatro', 
'5': 'Cinco', 
'6': 'Seis', 
'7': 'Siete', 
'8': 'Ocho', 
'9': 'Nueve', 
'0':'Cero'}
while len(x)>0:
    print(d[x])
    x = input("А ещё!?  ")
