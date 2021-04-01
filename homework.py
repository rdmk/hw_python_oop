import datetime as dt


today = dt.date.today().strftime("%d.%m.%Y")


class Record:
    def __init__(self, amount, comment, date=today):
        self.amount = amount
        self.comment = comment
        self.date = date


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []
    def add_record(self, record):
        self.records.append(record)
    def get_today_stats(self):
        sum = 0
        for record in self.records:
            if record.date == today:
                sum += record.amount
        return sum
    def get_weeks_stats(self):
        sum = 0
        today = dt.date.today()
        week = dt.timedelta(weeks=1)
        for record in self.records:
            dateString = record.date
            dateFormatter = "%d.%m.%Y"
            dateRecord = dt.datetime.strptime(dateString, dateFormatter)
            if dateRecord.date() + week >= today:
                sum += record.amount
        return sum


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        balance = self.limit - self.get_today_stats()
        if balance > 0:
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {balance} кКал'
        else:
            return f'Хватит есть!'
        

class CashCalculator(Calculator):
    EURO = 89.06
    USD = 75.88
    RUB = 1
    def get_today_cash_remained(self, currency):
        balance = self.limit - self.get_today_stats()
        self.currency = currency
        if balance == 0:
            return 'Денег нет, держись'
        elif self.currency == 'EURO' and balance > 0:
            return f'На сегодня осталось {round(balance / self.EURO, 2)} Euro'
        elif self.currency == 'EURO' and balance < 0:
            return f'Денег нет, держись: твой долг - {round(balance / self.EURO, 2)} Euro'
        elif self.currency == 'USD' and balance > 0:
            return f'На сегодня осталось {round(balance / self.USD, 2)} USD'
        elif self.currency == 'USD' and balance < 0:
            return f'Денег нет, держись: твой долг - {round(balance / self.USD, 2)} USD'
        elif self.currency == 'rub' and balance > 0:
            return f'На сегодня осталось {balance} руб'
        elif self.currency == 'rub' and balance < 0:
            return f'Денег нет, держись: твой долг - {balance} руб'


# создадим калькулятор денег с дневным лимитом 1000
cash_calculator = CashCalculator(1000)

# дата в параметрах не указана,
# так что по умолчанию к записи
# должна автоматически добавиться сегодняшняя дата
cash_calculator.add_record(Record(amount=145, comment='кофе'))
# и к этой записи тоже дата должна добавиться автоматически
cash_calculator.add_record(Record(amount=500, comment='Серёге за обед'))
# а тут пользователь указал дату, сохраняем её
cash_calculator.add_record(Record(amount=3000,
                                  comment='бар в Танин др',
                                  date='31.03.2021'))

print(cash_calculator.get_today_stats())
print(cash_calculator.get_weeks_stats())

print(cash_calculator.get_today_cash_remained('rub'))
print(cash_calculator.get_today_cash_remained('USD'))
# должно напечататься
# На сегодня осталось 555 руб



calories_calculator = CaloriesCalculator(2000)

calories_calculator.add_record(Record(500, 'завтрак', '24.03.2021'))

calories_calculator.add_record(Record(500, 'завтрак', '25.03.2021'))
calories_calculator.add_record(Record(900, 'обед', '25.03.2021'))
calories_calculator.add_record(Record(400, 'ужин', '25.03.2021'))

calories_calculator.add_record(Record(500, 'завтрак'))
calories_calculator.add_record(Record(900, 'обед'))
calories_calculator.add_record(Record(400, 'ужин'))

print(calories_calculator.get_today_stats())
print(calories_calculator.get_weeks_stats())
print(calories_calculator.get_calories_remained())

