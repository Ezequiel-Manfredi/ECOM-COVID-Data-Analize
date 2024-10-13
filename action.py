from utils import REPORT_FIELDS

class CountBy:
  def __init__(self,counterFields,percentageField):
    self.selectedFields = {
      field : {}
      for field in counterFields + percentageField
    }
    self.counterFields = counterFields
    self.percentageField = percentageField
    self.total = 0
    self.processed = 0
  
  def process(self,record):
    """
    - counter of diferent columns values
    - for each column, for each diferent value

    Args:
        record (dict): row information
    """
    self.processed += 1
    for key in self.selectedFields:
      self.selectedFields[key][record[key]] = self.selectedFields.get(key, 0).get(record[key], 0) + 1
  
  def show(self):
    """
    - emit counter's report and percentage
    """
    print("total de registros procesados: "+f'{self.processed}/{self.total}'.rjust(10))
    self.__iterateDict(
      self.counterFields,
      lambda value : value,
      lambda name,value: f'{name:<27}'+f'{value}'.rjust(10)
    )
    self.__iterateDict(
      self.percentageField,
      lambda value : (value/ self.processed),
      lambda name,value: f'{name:<27}{value:11.2%}'
    )

  def __iterateDict(self, dict, calc, msj):
    """
    - iterate the dictionary estructure and print summary

    Args:
        dict (dict): dictionary estructure
        calc (lambda value): function that operates on a parameter value and returns a result
        msj (lambda func): function that return a formatted string with the parameters name and value
    """
    for field in dict:
      columnName = REPORT_FIELDS.get(field,{'name': field})['name']
      print(f'{columnName}:')
      for value in self.selectedFields[field]:
        valueName = REPORT_FIELDS.get(field,{}).get(value,value)
        calculatedValue = calc(self.selectedFields[field][value])
        print('    '+msj(valueName,calculatedValue))

  def count(self):
    self.total += 1