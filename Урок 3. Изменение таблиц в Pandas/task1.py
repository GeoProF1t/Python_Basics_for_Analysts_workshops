import pandas as pd
df = pd.read_csv('kc_house_data.csv', sep=',')
stroki = df.head()
avg = df['price_per_sq_lot'] = df['price'] / df['sqft_lot']
df['delta_renovared'] = df['yr_renovated'] - df['yr_built']
renv = df['delta_renovared'] = df['delta_renovared'].apply(lambda x: x if x > 0 else 0)
year_ch = df['year'] = df['date'].apply(lambda x: int(x[:4]))
month_ch = df ['month']=df['date'].apply(lambda x: int(x[4:6]))
new = df.drop(columns=['date','zipcode', 'lat', 'long'], inplace=True)
