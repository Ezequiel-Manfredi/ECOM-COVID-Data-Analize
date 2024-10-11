# segunda_dosis = []
# mayores_60_refuerzo = 0

# cod_dosis_generica,nombre_dosis_generica
# grupo_etario

from validator import validators
from action import CountBy

# row values extracted to a list 
lineToList = lambda x: x.replace('\n','').split(',')

filePath = './datos/modelo_muestra.csv'
# filePath = './datos/datos_nomivac_parte1.csv'

totalizer = CountBy(counterFields = ['sexo','jurisdiccion_residencia'], percentageField = ['vacuna'])

with open(filePath,'r',encoding='utf-8') as file:
  fields = lineToList(file.readline())
  # limit = 0
  for line in file:
    # if limit == 10000:
    #   break
    # limit += 1
    values = lineToList(line)
    record = {field: values[index] for index,field in enumerate(fields)}
    
    totalizer.process(record)
  
  totalizer.show()
