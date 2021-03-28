import datetime as dt

 
class Calculator:
    def __init__(self, limit):
        self.limit = limit


class CaloriesCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)
        self.limit = limit


class CashCalculator(Calculator):
    def __init__(self, limit, currency):
        super().__init__(limit)
        self.currency = currency

    def get_today_cash_remained(self):
        USD_RATE = 75.66
        EURO_RATE = 89.24
        
        #if self.limit


class Record(Calculator):
    def __init__(self, amount, comment, date):
        self.amount = amount
        self.comment = comment
        self.date = date

    def show(self):
        print(f'потрачено {self.amount} на {self.comment} дата {self.date}')


cash_calculator = Record(amount=3000, comment='бар в Танин др', date='08.11.2019')

cash_calculator.show()

# создадим калькулятор денег с дневным лимитом 1000
cash_calculator = CashCalculator(1000)

# дата в параметрах не указана,
# так что по умолчанию к записи
# должна автоматически добавиться сегодняшняя дата
cash_calculator.add_record(Record(amount=145, comment='кофе'))
# и к этой записи тоже дата должна добавиться автоматически
cash_calculator.add_record(Record(amount=300, comment='Серёге за обед'))
# а тут пользователь указал дату, сохраняем её


print(cash_calculator.get_today_cash_remained('rub'))
# должно напечататься
# На сегодня осталось 555 руб 