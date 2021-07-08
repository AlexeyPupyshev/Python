a = input('Введите слова через пробел: ').split()
for i,x in enumerate(a,1):
    print(f'{i} - {x[:10]}')