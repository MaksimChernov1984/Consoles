name01 = input("Здравствуйте. Как Вас зовут? ")
if name01 == "Пэдро":
    print("О Мадонна! Вы мой тёзка!")
else:
    print("Очень приятно,",name01,". А меня Пэдро. ")
print()

name02 = input("Как называется Ваш родной город? ")
if name02 == "Буэнос-Айрес":
    print("Оказывается, мы земляки!")
else:
    print(name02," - прекрасный город! А я из Буэнос-Айреса.")
    print()
    
    
name03 = input("Кем Вы работаете? ")
if name03 == "эколог":
    print(name03," - весьма благородная профессия, а я выращиваю бычков на ферме.")
else:
    print(name03," - весьма благородная профессия, а я работаю экологом.")
print()
    
name04 = int(input("Сколько Вам лет? "))
if name04 < 38:
    print("Получается, Вы младше меня!")
elif name04 == 38:
    print("Значит, мы одногодки.")
else:
    print("Ну и ну, я моложе Вас!")

old = abs(38 - name04)
print("Наша разница в возрасте - ",old)
old1 = [1, 21, 31, 41, 51]
old2 = [2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54]
for old in old1:
	dif = "год."
if old in old2:
	dif = "года."
else:
	dif = "лет."
print(dif)

name05 = input()