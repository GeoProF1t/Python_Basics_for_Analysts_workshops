#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

#dates = ['2021-11-01']
#incomes = [100]

# Введите ваше решение ниже
def calc_income_by_month(dates, incomes):
    income_by_month = {}

    for i in range(len(dates)): 
        month = dates[i].split('-')[1]
        if month in income_by_month:
            income_by_month[month] += incomes[i]
        else:
            income_by_month[month] = incomes[i]

    return income_by_month

#print(calc_income_by_month(dates = ['2021-11-01'], incomes = [100]))