
### Задача 1
### Ошибка в затратах на рекламу
[task1.py](https://github.com/vadvad81/Python_Basics_for_Analysts_workshops/blob/78f2ff9e31f76d6b6e1fdabf3052f88bc05ba12c/%D0%A3%D1%80%D0%BE%D0%BA%201.%20%D0%9E%D1%84%D0%BE%D1%80%D0%BC%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%BD%D0%BE%D1%83%D1%82%D0%B1%D1%83%D0%BA%D0%B0%20%D0%B8%20%D0%B7%D0%B0%D0%BA%D1%80%D0%B5%D0%BF%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B9%20%D0%B8%20%D0%B3%D0%B5%D0%BD%D0%B5%D1%80%D0%B0%D1%82%D0%BE%D1%80%D0%BE%D0%B2/task1.py)

[task1GB.py](https://github.com/vadvad81/Python_Basics_for_Analysts_workshops/blob/78f2ff9e31f76d6b6e1fdabf3052f88bc05ba12c/%D0%A3%D1%80%D0%BE%D0%BA%201.%20%D0%9E%D1%84%D0%BE%D1%80%D0%BC%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%BD%D0%BE%D1%83%D1%82%D0%B1%D1%83%D0%BA%D0%B0%20%D0%B8%20%D0%B7%D0%B0%D0%BA%D1%80%D0%B5%D0%BF%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B9%20%D0%B8%20%D0%B3%D0%B5%D0%BD%D0%B5%D1%80%D0%B0%D1%82%D0%BE%D1%80%D0%BE%D0%B2/task1GB.py)

Дан список adv с затратами на рекламу.
Но в данных есть ошибки, некоторые затраты имеют отрицательную величину.
Удалите такие значения из списка и посчитайте суммарные затраты.
Запишите их в переменную x.
Используйте list comprehensions.

### Пример:

На входе:
```
adv = [100, 125, -90, 345, 655, -1, 0, 200]
```
На выходе:
```
1425
```
-----------------------------------
### Задача 2
### Склад с фруктами

[task2.py](https://github.com/vadvad81/Python_Basics_for_Analysts_workshops/blob/4f3d6787683cae632e248a62ebca94a28fff7b20/%D0%A3%D1%80%D0%BE%D0%BA%201.%20%D0%9E%D1%84%D0%BE%D1%80%D0%BC%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%BD%D0%BE%D1%83%D1%82%D0%B1%D1%83%D0%BA%D0%B0%20%D0%B8%20%D0%B7%D0%B0%D0%BA%D1%80%D0%B5%D0%BF%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B9%20%D0%B8%20%D0%B3%D0%B5%D0%BD%D0%B5%D1%80%D0%B0%D1%82%D0%BE%D1%80%D0%BE%D0%B2/task2.py)

[task2GB.py](https://github.com/vadvad81/Python_Basics_for_Analysts_workshops/blob/4f3d6787683cae632e248a62ebca94a28fff7b20/%D0%A3%D1%80%D0%BE%D0%BA%201.%20%D0%9E%D1%84%D0%BE%D1%80%D0%BC%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%BD%D0%BE%D1%83%D1%82%D0%B1%D1%83%D0%BA%D0%B0%20%D0%B8%20%D0%B7%D0%B0%D0%BA%D1%80%D0%B5%D0%BF%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B9%20%D0%B8%20%D0%B3%D0%B5%D0%BD%D0%B5%D1%80%D0%B0%D1%82%D0%BE%D1%80%D0%BE%D0%B2/task2GB.py)

На складе лежат разные фрукты в разном количестве.
Нужно написать функцию total_fruits, которая на вход принимает любое количество названий фруктов и их количество, а возвращает общее количество фруктов на складе.

можно решить через *kwargs

### Пример:

После вашего кода будет добавлена следующая строка:
```
print(total_fruits(apples=10, bananas=5, oranges=8))
```
На выходе:
```
23
```
-----------------------------------
### Задача 3
### Сумма покупок в ноябре

[task3.py](https://github.com/vadvad81/Python_Basics_for_Analysts_workshops/blob/4f3d6787683cae632e248a62ebca94a28fff7b20/%D0%A3%D1%80%D0%BE%D0%BA%201.%20%D0%9E%D1%84%D0%BE%D1%80%D0%BC%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%BD%D0%BE%D1%83%D1%82%D0%B1%D1%83%D0%BA%D0%B0%20%D0%B8%20%D0%B7%D0%B0%D0%BA%D1%80%D0%B5%D0%BF%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B9%20%D0%B8%20%D0%B3%D0%B5%D0%BD%D0%B5%D1%80%D0%B0%D1%82%D0%BE%D1%80%D0%BE%D0%B2/task3.py)

[task3GB.py](https://github.com/vadvad81/Python_Basics_for_Analysts_workshops/blob/4f3d6787683cae632e248a62ebca94a28fff7b20/%D0%A3%D1%80%D0%BE%D0%BA%201.%20%D0%9E%D1%84%D0%BE%D1%80%D0%BC%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%BD%D0%BE%D1%83%D1%82%D0%B1%D1%83%D0%BA%D0%B0%20%D0%B8%20%D0%B7%D0%B0%D0%BA%D1%80%D0%B5%D0%BF%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B9%20%D0%B8%20%D0%B3%D0%B5%D0%BD%D0%B5%D1%80%D0%B0%D1%82%D0%BE%D1%80%D0%BE%D0%B2/task3GB.py)

Даны два списка: дата покупки dates, суммы покупок по датам income.
Найти итоговую сумму всех покупок в ноябре и сохранить ее в переменную x.
Используйте list comprehensions.

### Пример:

На входе:
```
dates = ['2021-11-01']
income = [100]
```
На выходе:
```
100
```
-----------------------------------
### Задача 4
### Найдите выручку компании

[task4.py](https://github.com/vadvad81/Python_Basics_for_Analysts_workshops/blob/4f3d6787683cae632e248a62ebca94a28fff7b20/%D0%A3%D1%80%D0%BE%D0%BA%201.%20%D0%9E%D1%84%D0%BE%D1%80%D0%BC%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%BD%D0%BE%D1%83%D1%82%D0%B1%D1%83%D0%BA%D0%B0%20%D0%B8%20%D0%B7%D0%B0%D0%BA%D1%80%D0%B5%D0%BF%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B9%20%D0%B8%20%D0%B3%D0%B5%D0%BD%D0%B5%D1%80%D0%B0%D1%82%D0%BE%D1%80%D0%BE%D0%B2/task4.py)

[task4GB.py](https://github.com/vadvad81/Python_Basics_for_Analysts_workshops/blob/4f3d6787683cae632e248a62ebca94a28fff7b20/%D0%A3%D1%80%D0%BE%D0%BA%201.%20%D0%9E%D1%84%D0%BE%D1%80%D0%BC%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%BD%D0%BE%D1%83%D1%82%D0%B1%D1%83%D0%BA%D0%B0%20%D0%B8%20%D0%B7%D0%B0%D0%BA%D1%80%D0%B5%D0%BF%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B9%20%D0%B8%20%D0%B3%D0%B5%D0%BD%D0%B5%D1%80%D0%B0%D1%82%D0%BE%D1%80%D0%BE%D0%B2/task4GB.py)


Найдите выручку компании в зависимости от месяца Для этого напишите функцию calc_income_by_month(), которая на вход принимает список с датами и список с выручкой, а на выходе словарь, где ключи - это месяцы, а значения - это выручка. Используйте аннотирование типов.

### Пример:

На входе:
```
dates = ['2021-11-01']
incomes = [100]
```
После вашего кода будет автоматически добавлено:
```
print(calc_income_by_month(dates = ['2021-11-01'], incomes = [100]))
```
На выходе:
```
{'11': 100}
```