with open('Test.txt', 'w', encoding='utf-8') as f:
    while True:
        line = input('Введите стоку данных: ')
        if not line:
            break
        f.write(f'{line}\n')