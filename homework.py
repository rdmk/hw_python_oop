import datetime as dt
from typing import List

DATE_FORMAT = '%d.%m.%Y'


class Record:
    """Класс Record предназначен для создания записей."""

    amount: int
    comment: str
    date: dt.date

    def __init__(self, amount: int, comment: str, date: str = None) -> None:
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, DATE_FORMAT).date()


class Calculator:
    """Класс Калькулятор предназначен для подсчёта калорий и денег."""

    limit: int
    record: List[Record] 

    def __init__(self, limit: int) -> None:
        """Конструктор класса."""
        self.limit = limit
        self.records = []

    def add_record(self, record) -> None:
        """Добавление записей."""
        self.records.append(record)

    def get_today_stats(self) -> int:
        """Подсчёт дневной статистики."""
        today = dt.date.today()
        return sum(record.amount for record in self.records
                   if record.date == today)

    def get_week_stats(self) -> int:
        """Подсчёт недельной статистики."""
        today = dt.date.today()
        week = dt.date.today() - dt.timedelta(days=7)
        return sum(record.amount for record in self.records
                    if week < record.date <= today)

    def get_balance(self) -> int:
        """Подсчёт остатка."""
        return self.limit - self.get_today_stats()


class CaloriesCalculator(Calculator):
    """Дочерний класс Калькулятора - Калькулятор калорий.
    Предназначен для определения калорий, которые можно получить сегодня."""

    def get_calories_remained(self) -> str:
        """Метод предназначен для определения калорий,
        которые можно получить сегодня."""
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

    def get_today_cash_remained(self, currency: str) -> str:
        """Метод получает на вход название валюты и выводит количество
        денег, которые можно потратить в этой валюте"""
        balance = self.get_balance()

        currencies = {'eur': ('Euro', self.EURO_RATE),
                      'usd': ('USD', self.USD_RATE),
                      'rub': ('руб', self.RUB_RATE)}

        if currency not in currencies:
            raise ValueError('Нет такой валюты. Попробуйте ещё раз.')

        if balance == 0:
            return 'Денег нет, держись'

        currency_name, currency_rate = currencies[currency]
        balance_in_currency = abs(round((balance / currencies[currency][1]), 2))

        if balance > 0:
            return (f'На сегодня осталось {balance_in_currency} {currency_name}')

        return (f'Денег нет, держись: твой долг - {balance_in_currency} {currency_name}')
