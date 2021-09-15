import pandas as pd
# pd.set_option('display.max_rows', 10)
# pd.set_option('display.max_columns', 1000)

dataset = pd.read_csv('/home/ubuntu/Documentos/aluraDataScience/python-data-science-parte-2-aula-1-completa/Python_Data_Science/Pandas/data/db.csv', sep = ';')

print(f"---------------------------Analise Estatistica-----------------------------------")
print(f"{dataset[['Quilometragem', 'Valor']].describe()}")
print(f"-------------------------------Analise 0:4---------------------------------------")
print(f"{dataset.iloc[0:5]}")

select = (dataset.Motor == 'Motor Diesel') & (dataset.Zero_km == True)
print(f"---------------------------------Diesel 0KM--------------------------------------")
print(dataset.query('Motor == "Motor Diesel" and Zero_km == True'))

for index, row in dataset.iterrows():
    if(2019 - row['Ano'] != 0):
        dataset.loc[index, 'Km_media'] = row['Quilometragem'] / (2019 - row['Ano'])
    else:
        dataset.loc[index, 'Km_media'] = 0
print(f"--------------------------KM Media------------------------------------------------")
print(f"{dataset}")

dataset.fillna(0, inplace = True)
print(f"-------------------------0KM-----------------------------------------------------")
print(dataset.query("Zero_km == True"))