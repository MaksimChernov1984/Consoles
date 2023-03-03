z = input('Выберите:\nстарт/запись/конец/экзамен\n')
f = open('solar.py', 'a')
if z == 'старт':
	f.write('dic = { ')
elif z == 'запись':
	x = input('Название:  ')
	y = input('Тип:  ')
	while len(x)>0:
		f.write('"'+x+'": "'+y+'",\n')
		x = input('Название:  ')
		y = input('Тип:  ')
elif z == 'конец':
	f.write('None:None}')
elif z == 'экзамен':
	pass
f.close()
if z == 'экзамен':
	from solar import *
	x = input('Спрашивайте.\n')
	while len(x)>0:
		try:
			print('это '+dic[x]+'.')
		except:
			print('Не знаю...')
		x = input()