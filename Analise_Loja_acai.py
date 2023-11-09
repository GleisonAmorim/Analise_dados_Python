import pandas as pd

dados = pd.read_excel('vendas.xlsx.xlsx')

dados.head()
dados.tail()
dados.shape
dados.dtypes
dados.describe()

dados.head()
dados.loja.value_counts().to_frame()
dados.tamanho.value_counts().to_frame()
dados.forma_pagamento.value_counts().to_frame()

dados.head()
dados.groupby('loja').preco.sum().to_frame()
dados.groupby('loja').preco.mean().to_frame()
dados.head()
dados.groupby(['estado', 'loja']).preco.sum().to_frame()
dados.head()
dados.groupby(['loja', 'tamanho', 'forma_pagamento']).preco.sum().to_frame()

import plotly_express as px

grafico = px.histogram(dados, x='loja', y='preco', text_auto=True, color='tamanho')
grafico.write_html('Gráfico Faturamento.html')
grafico.show()

colunas = ['loja', 'cidade', 'estado', 'regiao', 'tamanho', 'local_consumo']

for coluna in colunas:
    grafico = px.histogram(dados, x=coluna, y='preco', text_auto=True, color='forma_pagamento')
    grafico.write_html(f'Fatumaramento por {coluna}.html')
    grafico.show()