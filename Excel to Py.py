import pandas as pd

# Lee el archivo de Excel y carga los datos en un DataFrame de pandas
df = pd.read_excel('C:/Users/End User/Desktop/wha.xlsx', sheet_name='Hoja1')

# Crea un diccionario vacío para cada celda en el archivo
data_dict = {}

# Itera sobre cada fila y columna del DataFrame
for index, row in df.iterrows():
    for column in df.columns:
        # Obtiene el valor de la celda actual
        cell_value = row[column]
        # Crea un diccionario único para la celda actual
        cell_dict = {}
        # Agrega el valor de la celda al diccionario
        cell_dict['valor'] = cell_value
        # Agrega el diccionario de la celda al diccionario general de datos
        data_dict[(index, column)] = cell_dict

# Imprime el diccionario de datos
print(data_dict)
