import pandas as pd
import matplotlib.pyplot as plt

plt.rc('figure', figsize = (20, 10))

dados = pd.read_csv('aluguel.csv', sep = ';')

residencial = ['Quitinete', 'Casa', 'Apartamento', 'Casa de Condominio', 'Casa de Vila']

selecao = dados['Tipo'].isin(residencial)
dados_residenciais = dados[selecao]
dados_residenciais.index = range(dados_residenciais.shape[0])

dados_residenciais.to_csv('aluguel_residencial.csv', sep = ';', index = False)
dados_residenciais = pd.read_csv('aluguel_residencial.csv', sep = ';')

selecao = dados['Tipo'] == 'Apartamento'
n1 = dados[selecao].shape[0]
print(f"Número de apartamentos: {n1}")

selecao = (dados['Tipo'] == 'Casa') | (dados['Tipo'] == 'Casa de Condominio') | (dados['Tipo'] == 'Casa de Vila')
n2 = dados[selecao].shape[0]
print(f"Número de casas: {n2}")

selecao = (dados['Area'] >= 60) & (dados['Area'] <= 100)
n3 = dados[selecao].shape[0]
print(f"Imóveis entre 60 e 100 m²: {n3}")

selecao = (dados['Quartos'] >= 4) & (dados['Valor'] <= 2000.0)
n4 = dados[selecao].shape[0]
print(f"Imóveis com no mínimo 4 quartos e aluguel máximo de R$2000.0: {n4}")
print(f"------------------------------------------------------------------")

#print(f"{dados_residenciais.sort_values('Quartos')}")

dados.dropna(subset = ['Valor'], inplace = True)
selecao = (dados['Tipo'] == 'Apartamento') & (dados['Condominio'].isnull())

dados = dados[~selecao]
dados = dados.fillna({'Condominio' : 0, 'IPTU' : 0})

dados['Valor Bruto'] = dados['Valor'] + dados['Condominio'] + dados['IPTU']
dados['Valor m2'] = (dados['Valor'] / dados['Area']).round(2)
dados['Bruto m2'] = (dados['Valor Bruto'] / dados['Area']).round(2)

casa = ['Casa', 'Casa de Condominio', 'Casa de Vila']
dados['Tipo Agregado'] = dados['Tipo'].apply(lambda x: 'Casa' if x in casa else 'Apartamento')

dados.drop(['Valor Bruto', 'Bruto m2'], axis = 1, inplace = True)

#print(f"{dados.Bairro.unique()}")

bairros = ['Barra da Tijuca','Copacabana','Ipanema','Botafogo', 'Flamengo']
selecao = dados['Bairro'].isin(bairros)
dados = dados[selecao]

grupo_bairro = dados.groupby('Bairro')
print(f"{grupo_bairro[['Valor', 'Condominio']].mean().round(2)}")
print(f"{grupo_bairro['Valor'].describe().round(2)}")
print(f"{grupo_bairro['Valor'].aggregate(['min', 'max']).rename(columns = {'min' : 'Mínimo', 'max' : 'Máximo'})}")

figura = grupo_bairro['Condominio'].mean().plot.bar(color = 'blue')
figura.set_ylabel('Valor do Aluguel')
figura.set_title('Valor Médio do Aluguel por Bairro', {'fontsize': 22})
plt.show()
#print(f"{dados.head(10)}")

#dados.to_csv('aluguel_residencial.csv', sep = ';', index = False)






'''
tipo_imovel = dados['Tipo']
tipo_imovel.drop_duplicates(inplace = True)

tipo_imovel = pd.DataFrame(tipo_imovel)

tipo_imovel.index = range(tipo_imovel.shape[0])
tipo_imovel.columns.name = 'ID
'''