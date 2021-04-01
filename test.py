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

    def get_week_stats(self):
        sum = 0
        today = dt.date.today()
        week = dt.timedelta(days=7)
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
            return 'Сегодня можно съесть что-нибудь ещё, '\
            f'но с общей калорийностью не более {balance} кКал'
        else:
            return f'Хватит есть!'


class CashCalculator(Calculator):
    EURO_RATE = 89.06
    USD_RATE = 75.88
    RUB = 1

    def get_today_cash_remained(self, currency):
        balance = self.limit - self.get_today_stats()
        self.currency = currency
        
        if self.currency == 'USD':
            name_currency = 'USD'
            value_currency = self.USD_RATE
        elif self.currency == 'Euro':
            name_currency = 'Euro'
            value_currency = self.EURO_RATE
        else:
            name_currency = 'руб'
            value_currency = 1

        if balance > 0:
            return 'На сегодня осталось '\
                f'{round((balance / value_currency), 2)} {name_currency}'
        elif balance < 0:
            return 'Денег нет, держись: твой долг - '\
                f'{abs(round((balance / value_currency), 2))} {name_currency}'
        else:
            return 'Денег нет, держись'
        

#cash
cash_calculator = CashCalculator(1000)
cash_calculator.add_record(Record(amount=145, comment='кофе'))
cash_calculator.add_record(Record(amount=500, comment='Серёге за обед'))
cash_calculator.add_record(Record(amount=100, comment='бар в Танин др'))
print(cash_calculator.get_today_stats())
print(cash_calculator.get_week_stats())
print(cash_calculator.get_today_cash_remained('rub'))
print(cash_calculator.get_today_cash_remained('USD'))
#calories
calories_calculator = CaloriesCalculator(2000)
calories_calculator.add_record(Record(500, 'завтрак', '24.03.2021'))
calories_calculator.add_record(Record(500, 'завтрак', '25.03.2021'))
calories_calculator.add_record(Record(900, 'обед', '25.03.2021'))
calories_calculator.add_record(Record(400, 'ужин', '25.03.2021'))

calories_calculator.add_record(Record(500, 'завтрак'))
calories_calculator.add_record(Record(900, 'обед'))
calories_calculator.add_record(Record(400, 'ужин'))

print(calories_calculator.get_today_stats())
print(calories_calculator.get_week_stats())
print(calories_calculator.get_calories_remained())
