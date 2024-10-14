class SpecialsOrders:
  def __init__(self):
    self.specialOrders = [
      {
        'count': 0,
        'msj': 'Personas mayores de 60 que recibieron dosis de refuerzo',
        'do': self.processAgeGroupOver60AndBoosterDose
      },
      {
        'count': {},
        'msj': 'Personas con 2da dosis por jurisdiccion de aplicación',
        'do': self.processSecondDocePerJurisdiction
      }
    ]
  
  def process(self,record):
    """
    - process all special orders on a record

    Args:
        record (dict): row information
    """
    for order in self.specialOrders:
      order['do'](order,record)
  
  def show(self):
    """
    - display the counter of all orders
    """
    for order in self.specialOrders:
      if (isinstance(order['count'], int)):
        print(f'{order['msj']}: {order['count']}')
      elif (isinstance(order['count'], dict)):
        print(f'{order['msj']}: ')
        for key,value in order['count'].items():
          print(f'  {key:<27}'+f'{value}'.rjust(10))

  def processAgeGroupOver60AndBoosterDose(self,order,record):
    """
    - validating a record on grupo_etario (>60) and nombre_dosis_generica (refuerzo) field requirements

    Args:
        order (dict): special order information
        record (dict): row information
    """
    ageGroup = record['grupo_etario'].split('-')
    doceName = record['nombre_dosis_generica']
    ageRange = len(ageGroup) > 1 and (60 < int(ageGroup[0]) or int(ageGroup[0]) <= 60 <= int(ageGroup[1]))
    ageLimit = len(ageGroup) == 1 and 60 <= int(ageGroup[0][1:])
    if (ageRange or ageLimit) and doceName.lower() == 'refuerzo':
      order['count'] += 1

  def processSecondDocePerJurisdiction(self,order,record):
    """
    - validating a record on nombre_dosis_generica (2da) for each jurisdiccion_aplicacion

    Args:
        order (dict): special order information
        record (dict): row information
    """
    doceName = record['nombre_dosis_generica']
    if doceName.lower() == '2da':
      order['count'][record['jurisdiccion_aplicacion']] = order['count'].get(record['jurisdiccion_aplicacion'],0) + 1

if __name__ == '__main__':
  specials = SpecialsOrders()
  specials.process({'grupo_etario': '<70','nombre_dosis_generica': 'Refuerzo'})
  specials.show()
