planets = []
p = input('Привет. Назови мне планеты!\nКогда закончишь, напиши "хватит".\n')
while p != 'хватит':
	planets.append(p)
	p = input()
satellites =[]
sa = input('Теперь напиши спутники.\n')
while sa != 'хватит':
	satellites.append(sa)
	sa = input()
dwarfs = []
d = input('Теперь перечисли мне карликовые планеты.\n')
while d != 'хватит':
	dwarfs.append(d)
	d = input()
asteroids = []
ast = input('Как насчёт астероидов?\n')
while ast != 'хватит':
	asteroids.append(ast)
	ast = input()
stars = []
st = input('А какие звёзды ты мне назовеёшь?\n')
while st != 'хватит':
	stars.append(st)
	st = input()
x = input('Теперь проверь меня. Напиши объект, а я отвечу, что это.\n')
while len(x)>0:
	if x in planets:
		print('Это планета.')
	elif x in satellites:
		print('Это спутник.')
	elif x in dwarfs:
		print('А это карликовая планета.')
	elif x in stars:
		print('Звезда.')
	else:
		print('Такое не знаю.')
	x = input()