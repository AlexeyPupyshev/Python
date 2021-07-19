from sys import argv

def zarplata():
    script_name, output_per_hour, rate_per_hour, bonus = argv[]
    print('Выработка в часах: ', int(output_per_hour))
    print('Ставка в час: ', int(rate_per_hour))
    print('Премия: ', int(bonus))
    print(f'Заработная плата равна {output_per_hour * rate_per_hour + bonus}')

zarplata()