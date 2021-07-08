goods = []
structure = {'Название' : '', 'Цена' : '', 'Количество' : '', 'Ед.измерения' : ''}
database = {'Название' : [], 'Цена' : [], 'Количество' : [], 'Ед.измерения' : []}
i = 0

while True:
    if input('Выход - Q, Далее - Enter ')=='Q':
        break
    i += 1
    for n in structure.keys():
        structure[n] = input(f'Введите {n}: ')
        database[n].append(structure[n])
    goods.append((i, structure.copy()))
    print(f'\n{goods}')
    for key, value in database.items():
        print(key, value)