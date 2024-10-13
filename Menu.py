import os 

class Menu:
  def __init__(self,fields):
    self.showOp = False
    self.fieldOptions = [{'name': field}for field in fields]
    self.countFields = []
    self.persentageFields = []
    self.actionOptions = [
      {
        'name': 'seleccionar campos para sacar totales',
        'do': lambda: self.__showOptions(
          'Seleccione de cuales contabilizar',
          self.fieldOptions,
          self.countFields
        )
      },
      {
        'name': 'seleccionar campos para sacar porcentajes',
        'do': lambda: self.__showOptions(
          'Seleccione de cuales sacar porcentajes',
          self.fieldOptions,
          self.persentageFields
        )
      },
    ]
  
  def showMenu(self):
    """
    - shows available actions to process file
    """
    self.__showOptions('Elija una accion',self.actionOptions,action = True)
    os.system('cls')
  
  def __showOptions(self,msj,options,listSelected = [],action = False):
    """
    - list on screen the options and manage the selected option

    Args:
        msj (str): message displayed on screen for the current action
        options (list): option list of dictionaries with name (str) field and do (lambda) optional
        listSelected (list, optional): selected fields by menu. Defaults to [].
        action (bool, optional): mark that options have the field do (lambda) to execute. Defaults to False.
    """
    while True:
      os.system('cls')
      if listSelected:
        print('lista: ',listSelected)
      print('0 - Terminar')
      for index,op in enumerate(options):
        print(f'{index+1} - {op.get('name')}')
      
      try:
        print(msj, end=' ')
        selection = int(input('>>> '))
        if selection == 0:
          break
        if options[selection-1] and action:
          options[selection-1].get('do',lambda: None)()
        else:
          listSelected.append(options[selection-1]['name'])
      except Exception as error:
        print('Error: opcion invalida intente de nuevo')
