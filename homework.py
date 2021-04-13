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
            if TODAY >= record.date > week:
                stats += record.amount
        return stats


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        balance = self.limit - self.get_today_stats()
        if balance > 0:
            return ('Сегодня можно съесть что-нибудь ещё, '
                    f'но с общей калорийностью не более {balance} кКал')
        return 'Хватит есть!'


class CashCalculator(Calculator):
    EURO_RATE = 92.14
    USD_RATE = 77.39

    def get_today_cash_remained(self, currency):
        balance = self.limit - self.get_today_stats()
        self.currency = currency
        if self.currency == 'usd':
            name_currency = 'USD'
            value_currency = self.USD_RATE
        elif self.currency == 'eur':
            name_currency = 'Euro'
            value_currency = self.EURO_RATE
        elif self.currency == 'rub':
            name_currency = 'руб'
            value_currency = 1.0

        balance_in_currency = abs(round((balance / value_currency), 2))

        if balance == 0:
            return 'Денег нет, держись'
        elif balance > 0:
            return ('На сегодня осталось '
                    f'{balance_in_currency} {name_currency}')
        return ('Денег нет, держись: твой долг - '
                    f'{balance_in_currency} {name_currency}')
