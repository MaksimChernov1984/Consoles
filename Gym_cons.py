y = input('Выберите:\nстарт/запись/чтение/сумма\n')
if y == 'старт':
	f = open('gym.py', 'w')
	f.write('x = ')
elif y == 'запись':
	f = open('gym.py', 'a')
	gym = int(input('Я отжался столько раз:  '))
	f.write(str(gym)+'+')
elif y == 'чтение':
	f = open('gym.py')
	for line in f:
		print(line)
elif y == 'сумма':
	f = open('gym.py', 'a')
	f.write('0')
f.close()
if y == 'сумма':
	from gym import x
	print(x)