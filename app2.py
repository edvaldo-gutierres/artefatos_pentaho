import pandas as pd
from controllers.merger_data import compare_data

pasta_xls = 'assets/trusted/pentaho.xlsx'
pasta_xls_new = 'assets/trusted/dados_banco.xlsx'

# Ler os arquivos Excel como DataFrames
existing_data = pd.read_excel(pasta_xls)
new_data = pd.read_excel(pasta_xls_new)

# Comparar os dados e imprimir os registros novos
new_records = compare_data(existing_data, new_data)
print(new_records)