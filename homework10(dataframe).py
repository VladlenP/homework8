import pandas as pd

# Загрузка данных
df = pd.read_csv('Pokemon.csv')

# Определение уникальных значений в столбце
unique_values = df['Type 1'].unique()

# Создание новых столбцов для каждого уникального значения
for value in unique_values:
    df[value] = (df['Type 1'] == value).astype(int)

# Удаление исходного столбца 'Type 1'
df.drop(columns=['Type 1'], inplace=True)

# Вывод первых строк преобразованного DataFrame
print(df.head())