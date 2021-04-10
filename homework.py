import datetime as dt


class Record:
    def __init__(self, amount, comment, date=''):
        self.amount = amount
        self.comment = comment
        if date == '':
            self.date = dt.datetime.now().date()
        else:
            self.date = dt.datetime.strptime(date, "%d.%m.%Y").date()


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        sum = 0
        for record in self.records:
            if record.date == dt.datetime.now().date():
                sum += record.amount
        return sum

    def get_week_stats(self):
        sum = 0
        today = dt.datetime.now().date()
        week = today - dt.timedelta(days=7)
        for record in self.records:
            date_from_record = record.date
            if today >= date_from_record > week:
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
    EURO_RATE = 92.14
    USD_RATE = 77.39

    def get_today_cash_remained(self, currency):
        balance = self.limit - self.get_today_stats()
        self.currency = currency
        
        if self.currency == 'usd':
            name_currency = 'USD'
            value_currency = CashCalculator.USD_RATE
        elif self.currency == 'eur':
            name_currency = 'Euro'
            value_currency = CashCalculator.EURO_RATE
        elif self.currency == 'rub':
            name_currency = 'руб'
            value_currency = 1.0

        balance_in_currency = abs(round((balance / value_currency), 2))

        if balance > 0:
            return 'На сегодня осталось '\
                f'{balance_in_currency} {name_currency}'
        elif balance < 0:
            return 'Денег нет, держись: твой долг - '\
                f'{balance_in_currency} {name_currency}'
        else:
            return 'Денег нет, держись'