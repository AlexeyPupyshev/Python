def my_func(x, y):
    x, y = float(x), int(y)
    if x <=0 or y > 0:
        return 'Ошибка! X: д.б. положительное число, а Y: д.б. отрицательное'
    else:
        exp = 1
        for _ in range(abs(y)):
            exp *= 1 / x
        return f'{x} в степени {y} равно {exp}'

print(my_func(5, -3))