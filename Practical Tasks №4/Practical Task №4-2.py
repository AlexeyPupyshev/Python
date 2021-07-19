list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(list)

list_new = [list[i] for i in range(1, len(list)) if list[i] > list[i-1]]
print(list_new)
