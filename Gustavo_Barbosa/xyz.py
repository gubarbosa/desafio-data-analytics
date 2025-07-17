import pandas as pd

df_vendas = pd.read_excel("Base-Dados-Desafio-D&A-01.xlsx", sheet_name=0)
df_produtos = pd.read_excel("Base-Dados-Desafio-D&A-01.xlsx", sheet_name=1)

df_xyz = pd.merge(df_vendas, df_produtos, on = "PRODUTO")

#print(df_xyz.head())

# 1. Identificação de perfil demográfico;

perfil_idade = df_xyz[['CLIENTE', 'IDADE']].drop_duplicates()['IDADE'].describe()
perfil_clientes_por_estado = df_xyz[['CLIENTE', 'ESTADO']].drop_duplicates().groupby('ESTADO').count()

# 2. Ranqueamento de categoria

vendas_categoria = df_xyz.groupby("CATEGORIA")["QUANTIDADE_VENDIDA"].sum().sort_values(ascending=False)
mais_vendida = vendas_categoria.idxmax()
menos_vendido = vendas_categoria.idxmin()

print(perfil_idade)
print(perfil_clientes_por_estado)

print(vendas_categoria)
print(mais_vendida)
print(menos_vendido)

