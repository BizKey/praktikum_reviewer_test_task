import datetime as dt
# неиспользуемый импорт
import json
# PEP8: E302 отсутствует 2 пустых строки перед классом
class Record:
    def __init__(self, amount, comment, date=''):
        # PEP8: E225 Пропущены пробелы перед и после оператора
        self.amount=amount
        # PEP8: E501 длина строки первышает 79 символов
        self.date = dt.datetime.now().date() if not date else dt.datetime.strptime(date, '%d.%m.%Y').date()
        # PEP8: E225 Пропущены пробелы перед и после оператора
        self.comment=comment
# PEP8: E302 отсутствует 2 пустых строки перед классом
class Calculator:
    def __init__(self, limit):
        self.limit = limit
        # PEP8: E225 Пропущены пробелы перед и после оператора
        self.records=[]
    # PEP8: E301 отсутствует 1 пустая строка перед методом
    def add_record(self, record):
        self.records.append(record)
    # PEP8: E301 отсутствует 1 пустая строка перед методом
    def get_today_stats(self):
        # PEP8: E225 Пропущены пробелы перед и после оператора
        today_stats=0
        # имя переменной Record совпадает с именем класса Record
        for Record in self.records:
            if Record.date == dt.datetime.now().date():
                today_stats = today_stats+Record.amount
        return today_stats
    # PEP8: E301 отсутствует 1 пустая строка перед методом
    def get_week_stats(self):
        # PEP8: E225 Пропущены пробелы перед и после оператора
        week_stats=0
        today = dt.datetime.now().date()
        for record in self.records:
            # Можно упростить до двойного неравенства и пропушены пробелы до и
            # после операторов и PEP8: E501 длина строки первышает 79 символов
            if (today -  record.date).days <7 and (today -  record.date).days >=0:
                # PEP8: E225 Пропущены пробелы перед и после оператора
                week_stats +=record.amount
        return week_stats
# PEP8: E302 отсутствует 2 пустых строки перед классом
class CaloriesCalculator(Calculator):
    # PEP8: E261 должно быть 2 пробела перед однострочным комментарием в коде
    def get_calories_remained(self): # Получает остаток калорий на сегодня
        # PEP8: E225 Пропущены пробелы перед и после оператора
        x=self.limit-self.get_today_stats()
        if x > 0:
            # PEP8: E501 длина строки первышает 79 символов
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {x} кКал'
        else:
            return 'Хватит есть!'
# PEP8: E302 отсутствует 2 пустых строки перед классом
class CashCalculator(Calculator):
    # PEP8: E225 Пропущены пробелы перед и после оператора
    USD_RATE=float(60) #Курс доллар США.
    # PEP8: E225 Пропущены пробелы перед и после оператора
    EURO_RATE=float(70) #Курс Евро.
    # PEP8: E301 отсутствует 1 пустая строка перед методом
    # PEP8: E501 длина строки первышает 79 символов
    def get_today_cash_remained(self, currency, USD_RATE=USD_RATE, EURO_RATE=EURO_RATE):
        # PEP8: E225 Пропущены пробелы перед и после оператора
        currency_type=currency
        cash_remained = self.limit - self.get_today_stats()
        # PEP8: E225 Пропущены пробелы перед и после оператора
        if currency=='usd':
            cash_remained /= USD_RATE
            # PEP8: E225 Пропущены пробелы перед и после оператора
            currency_type ='USD'
        # PEP8: E225 Пропущены пробелы перед и после оператора
        elif currency_type=='eur':
            cash_remained /= EURO_RATE
            # PEP8: E225 Пропущены пробелы перед и после оператора
            currency_type ='Euro'
        # PEP8: E225 Пропущены пробелы перед и после оператора
        elif currency_type=='rub':
            # Конвертировать рубли в рубли нет смысла, тем более что нужно
            # использовать так '/=' а не так '=='
            cash_remained == 1.00
            # PEP8: E225 Пропущены пробелы перед и после оператора
            currency_type ='руб'
        if cash_remained > 0:
            # В f-строках должны отсутствовать вызовы функций, логические и
            # арифметические операции
            # PEP8: E501 длина строки первышает 79 символов
            return f'На сегодня осталось {round(cash_remained, 2)} {currency_type}'
        elif cash_remained == 0:
            return 'Денег нет, держись'
        elif cash_remained < 0:
            # Нет единого стиля составления строк, либо f-строки,
            # либо format и PEP8: E501 длина строки первышает 79 символов
            return 'Денег нет, держись: твой долг - {0:.2f} {1}'.format(-cash_remained, currency_type)
    # это переопределение функции не имеет смысла
    def get_week_stats(self):
        super().get_week_stats()
