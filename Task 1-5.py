Revenue = float(input('Введите сумму выручки: '))
Costs = float(input('Введите сумму издержек: '))
if Revenue > Costs:
    print('Прибыль равна', float(Revenue - Costs))
    print('Рентабельность равна', float((Revenue - Costs) / Revenue))
    Num = int(input('Введите численность: '))
    print('Прибыль в расчете на одного сотрудника', float((Revenue - Costs) / Num))
elif Revenue < Costs:
    print('Убыток равен', float(Revenue - Costs))
else:
    print('Доход равен нулю')