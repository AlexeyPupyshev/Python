def my_func():
    num_1 = int(input('Введите число №1: '))
    num_2 = int(input('Введите число №2: '))
    num_3 = int(input('Введите число №3: '))
    if num_1 + num_2 + num_3 == 3*min(num_1, num_2, num_3):
        print(f'Все значения равны!')
    else:
        sum = num_1 + num_2 + num_3 - min(num_1, num_2, num_3)
        print(f'Сумма наибольших двух аргументов равна {sum}')

my_func()