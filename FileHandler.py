import os, sys

class FilesHandler:
  def __init__(self):
    self.inputFilePath = ''
    self.outputFilePath = os.path.normpath(os.path.join(os.getcwd(),os.path.basename('registros_erroneos.csv')))
    self.outputFile = None
  
  def start(self):
    if (len(sys.argv) > 1):
      return self.reader(sys.argv[1])
    else:
      
      while True:
        print('No se proporciono una ruta como argumento al ejecutar.')
        print('Por favor, ingresa una ruta:')
        try:
          userPath = input('>>> ')
          return self.reader(userPath)
        except KeyboardInterrupt:
          exit()
  
  def reader(self,relativePath):
    try:
      if not relativePath:
        relativePath = 'modelo_muestra.csv'
      workPath = os.getcwd()
      if os.path.isabs(relativePath):
        path = os.path.normpath(relativePath)
      else:
        path = os.path.normpath(os.path.join(workPath,relativePath))
      self.inputFilePath = path
    except :
      print(f'La ruta {relativePath} no existe o no se tiene permisos')
      exit()
    if (os.path.isfile(self.inputFilePath)):
      if (self.inputFilePath.endswith('.csv')):
        return self.getContent(self.inputFilePath)
      else:
        print(f'El archivo {self.inputFilePath} no es un archivo .csv')
    else:
      print(f'La ruta {self.inputFilePath} no corresponde a un archivo .csv')
  
  def getContent(self,filePath):
    with open(filePath, 'r', encoding='utf-8') as file:
      while True:
        line = file.readline()
        if not line:
          break
        yield line
  
  def isThereOutput(self):
    return bool(self.outputFile)
  
  def setOutput(self):
    self.outputFile = open(self.outputFilePath, 'w', encoding='utf-8')
  
  def closeOutput(self):
    self.outputFile.close()
  
  def writer(self,content):
    if not self.outputFile:
      self.setOutput()
    
    self.outputFile.write(content)

if __name__ == '__main__':
  fileHandler = FilesHandler()
  content = fileHandler.start()
  print(">>> ",content.__next__())
  for line in content:
    print(line)