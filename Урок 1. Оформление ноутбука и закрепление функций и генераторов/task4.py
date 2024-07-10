#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

#dates = ['2021-11-01']
#incomes = [100]

# Введите ваше решение ниже
from typing import List, Dict
from datetime import datetime

def calc_income_by_month(dates: List[str], incomes: List[int]) -> Dict[str, int]:
    income_by_month = {}
    for date, income in zip(dates, incomes):
        month = datetime.strptime(date, '%Y-%m-%d').strftime('%m')
        if month in income_by_month:
            income_by_month[month] += income
        else:
            income_by_month[month] = income
    return income_by_month

#print(calc_income_by_month(dates = ['2021-11-01'], incomes = [100]))