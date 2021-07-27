class Data:
    def __init__(self, dd_mm_yyyy):
        self.dd_mm_yyyy = str(dd_mm_yyyy)

    @classmethod
    def extract(cls, dd_mm_yyyy):
        date_new = []
        for i in dd_mm_yyyy.split('-'):
            if i != '-':
                date_new.append(i)
        return int(date_new[0]), int(date_new[1]), int(date_new[2])

    @staticmethod
    def valid(dd, mm, yyyy):

        if 1 <= dd <= 31:
            if 1 <= mm <= 12:
                if yyyy >= 1900:
                    return f'All right'
                else:
                    return f'Некорректный год'
            else:
                return f'Ошибка в месяце'
        else:
            return f'Ошибка в дне'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.dd_mm_yyyy)}'


today = Data('26-07-2021')
print(today)
print(today.extract('26-07-2021'))
print(today.valid(26, 17, 2021))

