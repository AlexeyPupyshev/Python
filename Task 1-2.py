a = int(input('Введите время в секундах - '))
sec = int(a % 60)
min = int((a - sec) % 3600/60)
hour = int((a - min*60 - sec)/3600)
print(f'{hour:02}:{min:02}:{sec:02}')