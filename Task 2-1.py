a = []
n = int(input('Введите количество элементов списка - '))
for i in range(n):
    el = input('Введите элемент списка: ')
    a.append(el)
print(a)
print(list(map(type, a)))