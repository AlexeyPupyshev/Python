def int_func(word):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    return word.title() if not set(word).difference(alpha) else False

sw = input('Введите слова через пробел (допускается маленькие латинские буквы) ').split()
for x in sw:
    result = int_func(sw)
    if result:
        print(int_func(sw), ' ')
