import pandas as pd
import matplotlib.pyplot as plt

# Leitura dos dados
df_vendas = pd.read_excel("Base-Dados-Desafio-D&A-01.xlsx", sheet_name=0)
df_produtos = pd.read_excel("Base-Dados-Desafio-D&A-01.xlsx", sheet_name=1)

# Merge das tabelas
df_xyz = pd.merge(df_vendas, df_produtos, on="PRODUTO")

# 1. Perfil demográfico
perfil_idade = df_xyz[['CLIENTE', 'IDADE']].drop_duplicates()['IDADE'].describe()
perfil_clientes_por_estado = df_xyz[['CLIENTE', 'ESTADO']].drop_duplicates().groupby('ESTADO').count().sort_values(by='CLIENTE', ascending=False)

# Gráfico: Quantidade de Clientes por Estado
perfil_clientes_por_estado.plot(kind='bar', legend=False, figsize=(8, 5))
plt.title('Quantidade de Clientes por Estado')
plt.xlabel('Estado')
plt.ylabel('Número de Clientes')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Gráfico: Distribuição de Idade
df_xyz[['CLIENTE', 'IDADE']].drop_duplicates()['IDADE'].plot(kind='hist', bins=10, color='skyblue', edgecolor='black', figsize=(8, 5))
plt.title('Distribuição de Idade dos Clientes')
plt.xlabel('Idade')
plt.ylabel('Quantidade de Clientes')
plt.tight_layout()
plt.show()

# 2. Ranqueamento de categorias
vendas_categoria = df_xyz.groupby("CATEGORIA")["QUANTIDADE_VENDIDA"].sum().sort_values(ascending=False)
mais_vendida = vendas_categoria.idxmax()
menos_vendido = vendas_categoria.idxmin()

# Gráfico: Vendas por Categoria
vendas_categoria.plot(kind='bar', color='green', figsize=(8, 5))
plt.title('Vendas por Categoria')
plt.xlabel('Categoria')
plt.ylabel('Quantidade Vendida')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Relação entre vendas e época do ano
df_xyz['MES'] = df_xyz['DATA'].dt.month
vendas_mensais = df_xyz.groupby('MES')['QUANTIDADE_VENDIDA'].sum()

# Gráfico: Vendas por Mês
vendas_mensais.plot(kind='line', marker='o', figsize=(8, 5))
plt.title('Vendas por Mês do Ano')
plt.xlabel('Mês')
plt.ylabel('Quantidade Vendida')
plt.xticks(range(1, 13))
plt.grid(True)
plt.tight_layout()
plt.show()

# 4. Tendência de vendas por estado
vendas_por_estado = df_xyz.groupby("ESTADO")["QUANTIDADE_VENDIDA"].sum().sort_values(ascending=False)

# Gráfico: Vendas por Estado
vendas_por_estado.plot(kind='bar', figsize=(10, 6))
plt.title('Quantidade de Vendas por Estado')
plt.xlabel('Estado')
plt.ylabel('Número de Vendas')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 5. Correlação entre idade e categoria
idade_categoria = df_xyz.groupby("CATEGORIA")["IDADE"].mean().sort_values()

idade_categoria.plot(kind='barh', figsize=(10, 6))
plt.title('Idade Média dos Clientes por Categoria de Produto')
plt.xlabel('Idade Média')
plt.ylabel('Categoria')
plt.tight_layout()
plt.show()