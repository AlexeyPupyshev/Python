from functools import reduce

def func(a, b):
    return a * b

list = [el for el in range(100,1000,2)]

print(list)
print(reduce(func, list))
