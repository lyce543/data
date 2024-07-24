import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('IMDBData.csv')
df = df.dropna()

df['Rating']=df['Rating'].apply(float)
df['Runtime (Minutes)']=df['Runtime (Minutes)'].apply(int)
df['Metascore']=df['Metascore'].apply(float)
print(df.info())
df['Director']=df['Director'].apply(str)
df['Actors']=df['Actors'].apply(str)
df['Rating']=df['Rating'].apply(float)
df['Metascore']=df['Metascore'].apply(float)

print('Середня тривалість фільмів з рейтингом вище 8')
print(df[df['Rating']>=8]['Runtime (Minutes)'].mean())
print('Середня тривалість фільмів з рейтингом вище 80 на Metacritics')
print(df[df['Metascore']>=80]['Runtime (Minutes)'].mean())

print('Найкоротша триввалість фільму з ейтингом більше 8')
print(df[df['Rating']>=8]['Runtime (Minutes)'].min())
print('Найдовша триввалість фільму з ейтингом більше 8')
print(df[df['Rating']>=8]['Runtime (Minutes)'].max())
print('Найкоротша триввалість фільму з ейтингом більше 80 на Metacritics')
print(df[df['Metascore']>=80]['Runtime (Minutes)'].min())
print('Найдовша триввалість фільму з ейтингом більше 80 на Metacritics')
print(df[df['Metascore']>=80]['Runtime (Minutes)'].max())

print('Середній рейтинг фільму тривалість якого більша за 95 та коротша за 180')
print(df[(df['Runtime (Minutes)'] >= 95) & (df['Runtime (Minutes)'] <= 180)]['Rating'].mean())
print('Середня оцінка фільму на Metacritics тривалість якого більша за 66 та коротша за 180')
print(df[(df['Runtime (Minutes)'] >= 66) & (df['Runtime (Minutes)'] <= 180)]['Metascore'].mean())

df.plot(x='Runtime (Minutes)',
        y='Rating',
        kind='scatter')
plt.show()

df.plot(x='Runtime (Minutes)',
        y='Metascore',
        kind='scatter')
plt.show()

df['Actors'] = df['Actors'].apply(lambda x: x.split(', ') and  x.split(','))

df_exploded = df.explode('Actors')
df_exploded.groupby(['Actors', 'Director'])['Metascore'].mean()

max_metascore_row = df_exploded.loc[df_exploded['Metascore'].idxmax()]
print(max_metascore_row['Director']+' '+max_metascore_row['Actors'])