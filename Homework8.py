import pandas as pd
import numpy as np

# ## Описание колонок
#
# `Rank` - Общий рейтинг продаж
#
# `Name` - Название игры
#
# `Platform` - Платформа, на которой выпущена игра (например, PC, PS4 и т.д.)
#
# `Year` - Год выпуска игры
#
# `Genre` - Жанр игры
#
# `Publisher` - Издатель игры
#
# `NA_Sales` - Продажи в Северной Америке (в миллионах)
#
# `EU_Sales` - Продажи в Европе (в миллионах)
#
# `JP_Sales` - Продажи в Японии (в миллионах)
#
# `Other_Sales` - Продажи в остальном мире (в миллионах)
#
# `Global_Sales` - Общемировые продажи.

# загрузите датасет
file_name = 'vgsales.csv'
df = pd.read_csv(file_name)  # ваш код здесь

# после того датасет корректно загрузился, можно посмотреть на данные глазами
df.head()
df_clean = df[['Name',
            'Platform',
            'Year',
            'Genre',
            'Publisher',
            'NA_Sales',
            'EU_Sales',
            'JP_Sales',
            'Other_Sales',
            'Global_Sales']]
# соберем данные по имени и удалим пустые строки, если они имеются
df_clean = df_clean.dropna()
# Вопрос 1: Найдите количество уникальных игр в датасете.
# скопируем исходный дата-сет
game_df = df_clean.copy()
game_df = pd.unique(game_df['Name'])
print(f'кол-во уникальных игр = {len(game_df)}')
print()

game_df = df_clean.copy()
quantity_unique_game = game_df['Name'].nunique()
print(f'кол-во уникальных игр = {quantity_unique_game}')
print()

# вопрос 2: Какова общая величина продаж игр в Японии?
jp_total_sales = df_clean['JP_Sales'].sum()
print(f'общая величина продаж в Японии = {jp_total_sales}')
print()

# вопрос 3: Какие три жанра игр самые популярные в Северной Америке (по количеству продаж)?
na_df = df_clean.groupby('Genre')['NA_Sales'].sum()
na_df = na_df.sort_values(axis=0,
                          ascending=False,
                          inplace=False,
                          kind='quicksort',
                          na_position='last',
                          ignore_index=False,
                          key=None)[:3]
top_NA_genre = na_df.index.tolist()
print(f'Три самых популярных жанра в Северной Америке по количеству продаж = {top_NA_genre}')
print()

na_df = df_clean.groupby('Genre')['NA_Sales'].sum()
sorted_dict = dict(sorted(na_df.items(), key=lambda item: item[1], reverse=True)[:3])
top_NA_genre = list(sorted_dict.keys())
print(f'Три самых популярных жанра в Северной Америке по количеству продаж = {top_NA_genre}')
print()

# вопрос 4: Какая платформа была самой популярной (по количеству выпущенных игр) в 2000 году? А в 2015?
some_value = 2000
some_df = df_clean.loc[df_clean['Year'] == some_value]
print('Самая популярная платформа по количеству выпущенных игр в {} - {}'.format(some_value,some_df['Platform']. value_counts(). idxmax()))

some_value = 2015
some_df = df_clean.loc[df_clean['Year'] == some_value]
print('Самая популярная платформа по количеству выпущенных игр в {} - {}'.format(some_value,some_df['Platform']. value_counts(). idxmax()))
print()

# вопрос 5: Какой издатель выпустил больше всего игр в период 2012-2015 оба конца включительно?
year_start = 2012
year_finish = 2015
some_df = df_clean.loc[(df_clean['Year'] >= year_start) & (df['Year'] <= year_finish)]

print('{} выпустил больше всего игр в период {}-{}'.format(some_df['Publisher'].value_counts().idxmax(), year_start, year_finish))
print()

# вопрос 6: Какой процент игр в жанре спорт был продан в Европе?
genre = 'Sports'
some_df = df_clean[['Genre', 'EU_Sales']]
some_df_genre = some_df.loc[df_clean['Genre'] == genre]
genre_sales = round((some_df_genre['EU_Sales'].sum()/some_df['EU_Sales'].sum())*100)
print('В Европе продано игр в жанре {} {}% от общего количества'.format(genre, genre_sales))
print()

some_df = df_clean.groupby('Genre')['EU_Sales'].sum()
genre_sales = round((some_df['Sports']/some_df.sum())*100)
print('В Европе продано игр в жанре {} {}% от общего количества'.format(genre, genre_sales))
print()

array = np.array([71, 1, 10, 0, 128])
print(array)
print(array.mean())