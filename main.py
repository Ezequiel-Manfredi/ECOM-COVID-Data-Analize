from utils import lineToList
from Menu import Menu
from validator import recordIsValid
from FileHandler import FilesHandler
from CountBy import CountBy
from Specials import SpecialsOrders

fileHandler = FilesHandler()

inputFile = fileHandler.start()
fields = lineToList(inputFile.__next__())

menu = Menu(fields)
menu.showMenu()

totalizer = CountBy(menu.getCounterFields(),menu.getPersentageFields())
specialOrder = SpecialsOrders()

# limit = 0
for line in inputFile:
  # if limit == 10000:
  #   break
  # limit += 1

  values = lineToList(line)
  record = {field: values[index] for index,field in enumerate(fields)}
  
  totalizer.count()
  
  errors = recordIsValid(record)
  if (len(errors) > 0):
    if not fileHandler.isThereOutput():
      fileHandler.writer(','.join(fields + ['observación'])+'\n')
    
    observations = ['|'.join(list(map(lambda dicc: dicc['error'],errors)))]
    fileHandler.writer(','.join(values + observations)+'\n')
    continue
  
  totalizer.process(record)
  specialOrder.process(record)

totalizer.show()
specialOrder.show()

if (fileHandler.isThereOutput()):
  fileHandler.closeOutput()