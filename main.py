# segunda_dosis = []
# mayores_60_refuerzo = 0

# cod_dosis_generica,nombre_dosis_generica
# grupo_etario

from validator import validators
from action import CountBy

# row values extracted to a list 
lineToList = lambda x: x.replace('\n','').split(',')

filePath = './datos/modelo_muestra.csv'

totalizer = CountBy(['sexo','vacuna'])

with open(filePath,'r',encoding='utf-8') as file:
  fields = lineToList(file.readline())

  for line in file:
    values = lineToList(line)
    record = {field: values[index] for index,field in enumerate(fields)}
    
    totalizer.process(record)
  
  totalizer.show()
