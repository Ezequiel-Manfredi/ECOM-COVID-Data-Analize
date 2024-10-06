# resultado_por_genero = [0,0]
# resultado_por_tipo_vacuna = []
# total_registros = 0

# segunda_dosis = []
# mayores_60_refuerzo = 0

# sexo
# vacuna
# jurisdiccion_residencia,jurisdiccion_residencia_id

# cod_dosis_generica,nombre_dosis_generica
# grupo_etario

import csv
from validator import validators
from action import actions

filePath = './datos/modelo_muestra.csv'

with open(filePath,'r',encoding='utf-8') as file:
  records = csv.DictReader(file, delimiter=',')
  for record in records:
    for field_to_validate in validators:
      value = record[field_to_validate['field']]
      validations = field_to_validate['validate']
      
      l = list(map(lambda check: check(value),validations))
      
      print(l)
