import datetime as dt


DATE_FORMAT = '%d.%m.%Y'
TODAY = dt.date.today()


class Record:
    """Класс Record предназначен для хранения записей."""

    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date == None:
            self.date = TODAY
        else:
            self.date = dt.datetime.strptime(date, DATE_FORMAT).date()


class Calculator:
    """Класс Калькулятор предназначен для подсчёта калорий и денег."""

    def __init__(self, limit):
        """Конструктор класса."""
        self.limit = limit
        self.records = []

    def add_record(self, record):
        """Добавление записей."""
        self.records.append(record)

    def get_today_stats(self):
        """Подсчёт дневной статистики."""
        return sum([record.amount for record in self.records
                    if record.date == TODAY])

    def get_week_stats(self):
        """Подсчёт недельной статистики."""
        week = TODAY - dt.timedelta(days=7)
        return sum([record.amount for record in self.records
                    if week < record.date <= TODAY])

    def get_balance(self):
        """Подсчёт остатка."""
        return self.limit - self.get_today_stats()


class CaloriesCalculator(Calculator):
    """Дочерний класс Калькулятора - Калькулятор калорий.
    Предназначен для определения калорий, которые можно получить сегодня."""

    def get_calories_remained(self):
        balance = self.get_balance()
        if balance > 0:
            return ('Сегодня можно съесть что-нибудь ещё, '
                    f'но с общей калорийностью не более {balance} кКал')
        return 'Хватит есть!'


class CashCalculator(Calculator):
    """Дочерний класс Калькулятора - Калькулятор денег.
    Определяет, сколько ещё денег можно потратить сегодня в рублях,
    долларах или евро."""

    EURO_RATE = 92.14
    USD_RATE = 77.39
    RUB_RATE = 1

    def get_today_cash_remained(self, currency):
        balance = self.get_balance()
        currencies = {'eur': ['Euro', self.EURO_RATE],
                      'usd': ['USD', self.USD_RATE],
                      'rub': ['руб', self.RUB_RATE]}

        if currency not in currencies:
            raise ValueError('Нет такой валюты. Попробуйте ещё раз.')

        balance_in_currency = abs(round((balance / currencies[currency][1]), 2))

        if balance == 0:
            return 'Денег нет, держись'
        elif balance > 0:
            return ('На сегодня осталось '
                    f'{balance_in_currency} {currencies[currency][0]}')
        return ('Денег нет, держись: твой долг - '
                f'{balance_in_currency} {currencies[currency][0]}')
