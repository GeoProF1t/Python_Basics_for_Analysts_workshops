import pandas as pd
df = pd.read_csv('kc_house_data.csv', sep=',')

# 1. Средняя стоимость домов в зависимости от количества спален (отсортирована от меньшей к большей)
avg = df.groupby('bedrooms').agg({'price':'mean'}).sort_values('price')

# 2. Минимальная, средняя и максимальная стоимости домов в зависимости от состояния дома
price = df.groupby('condition').agg({'price':['min', 'mean', 'max']})

# 3. Таблица с подсчетом количества домов в зависимости от видов на набережную и оценок вида
view_waterfront = df.pivot_table(index='waterfront', columns='view', values='condition', aggfunc='count', fill_value=0)

# 4. Таблица с подсчетом количества домов в зависимости от этажности и количества спален
bedrooms_floors = pd.crosstab(index=df['floors'], columns=df['bedrooms'])

# 5. Таблица с медианной стоимостью домов в зависимости от состояния дома и оценки дома
median_price = df.pivot_table(index='condition', columns='grade', values='price', aggfunc='median', fill_value=0)

