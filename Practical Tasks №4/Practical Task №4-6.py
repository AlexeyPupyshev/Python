from itertools import count, cycle

first = int(input('Введите начальное число: '))
end = int(input('Введите конечное число: '))

for el in count(first):
    if el > end:
        break
    else:
        print(el)

list = str(input('Введите список для повторения: ')).split()
end = int(input('Введите количество повторений: '))
i = 0
for el in cycle(list):
    if i > end:
        break
    print(el)
    i += 1