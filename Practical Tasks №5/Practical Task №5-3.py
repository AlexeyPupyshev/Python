with open('Incomes.txt', 'r', encoding='utf-8') as f:
    list_new = {line.split()[0] : int(line.split()[1]) for line in f if int(line.split()[1]) < 20000}
    print(list_new)
    sum_income = sum(list_new.values())
    num = len(list_new)
    print(f'Средний доход сотрудников с суммой меньше 20000 равен  {sum_income/num}')

