# import pandas as pd

# # Загрузка данных
# df = pd.read_csv('Pokemon.csv')

# # Определение уникальных значений в столбце
# unique_values = df['Type 1'].unique()

# # Создание новых столбцов для каждого уникального значения
# for value in unique_values:
#     df[value] = (df['Type 1'] == value).astype(int)

# # Удаление исходного столбца 'Type 1'
# df.drop(columns=['Type 1'], inplace=True)

# # Вывод первых строк преобразованного DataFrame
# print(df.head())


import csv

# Чтение данных из CSV файла
with open('Pokemon.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

# Определение уникальных значений в столбце 'Type 1'
unique_values = list({row['Type 1'] for row in data})

# Преобразование данных в one-hot вид
one_hot_data = []
for row in data:
    one_hot_row = {value: 0 for value in unique_values}
    one_hot_row.update(row)
    one_hot_row[row['Type 1']] = 1
    one_hot_data.append(one_hot_row)

# Удаление исходного столбца 'Type 1'
for row in one_hot_data:
    del row['Type 1']

# Запись преобразованных данных обратно в CSV файл или вывод на экран
with open('Pokemon_one_hot.csv', 'w', newline='') as csvfile:
    fieldnames = list(one_hot_data[0].keys())
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in one_hot_data:
        writer.writerow(row)

# Вывод первых строк преобразованных данных
for row in one_hot_data[:5]:
    print(row)