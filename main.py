# segunda_dosis = []
# mayores_60_refuerzo = 0

# cod_dosis_generica,nombre_dosis_generica
# grupo_etario

from utils import lineToList,inputPath,outputPath
from Menu import Menu
from validator import recordIsValid
from CountBy import CountBy

errorsFile = None

# file read line by line, transforming it into dictionaries to validate and process it
with open(inputPath,'r',encoding='utf-8') as file:
  fields = lineToList(file.readline())
  
  menu = Menu(fields)
  menu.showMenu()
  
  totalizer = CountBy(menu.countFields, menu.persentageFields)
  
  # limit = 0
  for line in file:
    # if limit == 10000:
    #   break
    # limit += 1
    values = lineToList(line)
    record = {field: values[index] for index,field in enumerate(fields)}
    
    totalizer.count()
    
    errors = recordIsValid(record)
    if (len(errors) > 0):
      if (not errorsFile):
        errorsFile = open(outputPath,'w',encoding='utf-8')
        errorsFile.write(','.join(fields + ['observación'])+'\n')
      
      observations = ['|'.join(list(map(lambda dicc: dicc['error'],errors)))]
      errorsFile.write(','.join(values + observations)+'\n')
      continue
    
    totalizer.process(record)
  
  totalizer.show()

if (errorsFile):
  errorsFile.close()