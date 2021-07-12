def sum_num():
    sum = 0
    while True:
        string_num =input('Введите числа через пробел. Для выхода нажмите Q. ').split()
        for x in string_num:
            if x == 'q':
                return sum
            else:
                sum += int(x)
        print(f'Сумма чисел равна {sum}')

sum_num()