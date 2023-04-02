#import xlsxwriter

#xs = [{'x': 2,   'y': 1,  'z': 1}, 
#      {'x': 3,   'y': 15, 'z': 41},
#      {'x': 22,  'y': 10, 'z': 40},
#      {'x': 132, 'y': 89, 'z': 1}]

#workbook = xlsxwriter.Workbook('ejemplo2.xlsx')
#worksheet = workbook.add_worksheet()

#headers = ['x', 'y', 'z']

#for row, _dict in enumerate(xs):
#    for col, key in enumerate(headers):
#        worksheet.write(row, col, _dict[key])
#workbook.close()

import xlsxwriter

xs = [{'x': 100, 'y': 30, 'z': 66},  #19.8
      {'x': 100, 'y': 20, 'z': 80},  #16
      {'x': 100, 'y': 10, 'z': 91},  #9.1
      {'x': 100, 'y': 40, 'z': 75}]  #30

workbook = xlsxwriter.Workbook('ejemplo5.xlsx')
worksheet = workbook.add_worksheet()

headers = ['x', 'y', 'z']

for row, _dict in enumerate(xs):
    b_value = (_dict['z'] * _dict['y']) / _dict['x']  # calcular la suma de 'x' y 'y'
    worksheet.write(row, 3, b_value)  # escribir el resultado en la columna 'z'

    for col, key in enumerate(headers[:3]):  # escribir los valores de 'x' y 'y' en las primeras dos columnas
        worksheet.write(row, col, _dict[key])

workbook.close()