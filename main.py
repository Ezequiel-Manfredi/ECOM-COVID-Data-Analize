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

from validator import validators
from action import actions

# row values extracted to a list 
lineToList = lambda x: x.replace('\n','').split(',')

filePath = './datos/modelo_muestra.csv'

with open(filePath,'r',encoding='utf-8') as file:
  fields = lineToList(file.readline())

  for line in file:
    values = lineToList(line)
    record = {field: values[index] for index,field in enumerate(fields)}
  # for field_to_validate in validators:
  #   value = record[field_to_validate['field']]
  #   validations = field_to_validate['validate']
    
  #   l = list(map(lambda check: check(value),validations))
    
  #   print(l)
  # print(i)
  # i += 1
