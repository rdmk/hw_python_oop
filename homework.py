import datetime as dt


DATE_FORMAT = '%d.%m.%Y'
TODAY = dt.date.today()


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date == None:
            self.date = TODAY
        else:
            self.date = dt.datetime.strptime(date, DATE_FORMAT).date()


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        stats = 0
        for record in self.records:
            if record.date == TODAY:
                stats += record.amount
        return stats

    def get_week_stats(self):
        stats = 0
        week = TODAY - dt.timedelta(days=7)
        for record in self.records:
            if week < record.date <= TODAY:
                stats += record.amount
        return stats

    def get_balance(self):
        return self.limit - self.get_today_stats()


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        balance = self.get_balance()
        if balance > 0:
            return ('Сегодня можно съесть что-нибудь ещё, '
                    f'но с общей калорийностью не более {balance} кКал')
        return 'Хватит есть!'


class CashCalculator(Calculator):
    EURO_RATE = 92.14
    USD_RATE = 77.39
    RUB_RATE = 1

    def get_today_cash_remained(self, currency):
        balance = self.get_balance()
        currencies = {'eur': ['Euro', self.EURO_RATE],
                      'usd': ['USD', self.USD_RATE],
                      'rub': ['руб', self.RUB_RATE]}

        try:
            balance_in_currency = abs(round((balance / currencies[currency][1]), 2))

            if balance == 0:
                return 'Денег нет, держись'
            elif balance > 0:
                return ('На сегодня осталось '
                        f'{balance_in_currency} {currencies[currency][0]}')
            return ('Денег нет, держись: твой долг - '
                    f'{balance_in_currency} {currencies[currency][0]}')

        except:
            raise ValueError('Вы неверно ввели название валюту. Попробуйте ещё раз.')
