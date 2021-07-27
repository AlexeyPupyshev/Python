class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                val = int(input('Введите значения и нажимайте Enter - '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f'Недопустимое значение')
                yn = input(f'Попробовать еще раз? Y - да / N - нет')

                if yn == 'Y' or yn == 'y':
                    print(try_except.my_input())
                elif yn == 'N' or yn == 'n':
                    return f'Вы вышли'
                else:
                    return f'Вы вышли'

try_except = Error(1)
print(try_except.my_input())