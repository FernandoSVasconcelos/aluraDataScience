import pandas as pd
MAXIMO = 100

dados_residenciais = pd.read_csv('aluguel_residencial.csv', sep = ';')

faixas = [0, 2, 4, 6, MAXIMO]
quartos = pd.cut(dados_residenciais.Quartos, faixas)

labels = ['1-2 Quartos', '3-4 Quartos', '5-6 Quartos', '7+ Quartos']
quartos = pd.cut(dados_residenciais.Quartos, faixas, labels = labels, include_lowest = True)
print(f"{pd.value_counts(quartos)}")