def divide():
    a = float(input('Введите числитель: '))
    b = float(input('Введите знаменатель: '))
    if b == 0:
        print('На ноль делить нельзя!')
    else:
        c = a / b
        print(f'Частное от деления {a} на {b} равно: {c}')

divide()