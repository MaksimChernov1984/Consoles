from Gcode_dict import dict
g = input()
while len(g) > 0:
    if g not in dict:
        print('Нет такой команды.')
    else:
        print(dict[g])
    g = input()
