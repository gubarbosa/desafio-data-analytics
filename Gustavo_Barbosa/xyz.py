import pandas as pd

df_vendas = pd.read_excel("Base-Dados-Desafio-D&A-01.xlsx", sheet_name=0)
df_produtos = pd.read_excel("Base-Dados-Desafio-D&A-01.xlsx", sheet_name=1)

df_xyz = pd.merge(df_vendas, df_produtos, on = "PRODUTO")

print(df_xyz.head())

# 1. Identificação de perfil demográfico;

perfil_idade = df_xyz[['CLIENTE', 'IDADE']].drop_duplicates()['IDADE'].describe()
perfil_clientes_por_estado = df_xyz[['CLIENTE', 'ESTADO']].drop_duplicates().groupby('ESTADO').count()

# 2. Ranqueamento de categoria;

vendas_categoria = df_xyz.groupby("CATEGORIA")["QUANTIDADE_VENDIDA"].sum().sort_values(ascending=False)
mais_vendida = vendas_categoria.idxmax()
menos_vendido = vendas_categoria.idxmin()

# 3. Relação entre vendas e época do ano;

df_xyz['MES'] = df_xyz['DATA'].dt.month
vendas_mensais = df_xyz.groupby('MES')['QUANTIDADE_VENDIDA'].sum() 

# 4. Tendência de vendas por regiao geográfica;

vendas_por_estado = df_xyz.groupby("ESTADO")["QUANTIDADE_VENDIDA"].sum().sort_values(ascending=False)

# 5 Correlação entre idade dos clientes e as categorias dos produtos;

idade_categoria = df_xyz.groupby("CATEGORIA")["IDADE"].mean().sort_values()

print(perfil_idade)
print(perfil_clientes_por_estado)

print(vendas_categoria)
print(mais_vendida)
print(menos_vendido)

print(vendas_mensais)

print(vendas_por_estado)

print(idade_categoria)