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
        #return sum(record.amount for record in self.records)
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

#class CaloriesCalculator:
#    ...

class CashCalculator(Calculator):

    ...

# создадим калькулятор денег с дневным лимитом 1000
cash_calculator = CashCalculator(1000)

# дата в параметрах не указана,
# так что по умолчанию к записи
# должна автоматически добавиться сегодняшняя дата
cash_calculator.add_record(Record(amount=145, comment='кофе'))
# и к этой записи тоже дата должна добавиться автоматически
cash_calculator.add_record(Record(amount=300, comment='Серёге за обед'))
# а тут пользователь указал дату, сохраняем её
cash_calculator.add_record(Record(amount=3000,
                                  comment='бар в Танин др',
                                  date='31.03.2021'))

print(cash_calculator.get_today_stats())
print(cash_calculator.get_weeks_stats())
#print(cash_calculator.get_today_cash_remained('rub'))
# должно напечататься
# На сегодня осталось 555 руб
