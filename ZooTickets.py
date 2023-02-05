print("""Стоимость билетов в зоопарк
взрослые - 350 р.
дети от 3 до 18 лет - 150 р.
льготные категории - 150 р.
дети до 3 лет - бесплатно.""")
print()

y = int(input("Укажите количество посетителей  "))
print()
z = int(input("Укажите количество льготников  "))
print()
print("Укажите возраст каждого посетителя")
total = 0
x = 0
while x < y:
	age = int(input())
	if 3 <= age < 18:
		total += 150
	elif age >= 18:
		total += 350
	x += 1

total1 = 0
w = 0	
while w < z:
	if age >= 18:
		total1 +=200
	w += 1
print()
print("Стоимость билетов")
print(total - total1)
