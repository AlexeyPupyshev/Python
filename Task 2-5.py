rating = [9, 7, 6, 4, 2, 1]
new_element = int(input('Введите новый элемент рейтинга: '))
rating.append(new_element)
print(sorted((rating), reverse=True))