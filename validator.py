import re
from utils import PATTERNS

def recordIsValid(record):
  """
  - validate 

  Args:
      record (dict): row information

  Returns:
      bool: record validity
  """
  errors = []
  for field,value in record.items():
    response = validate(field,value)
    if(not response['ok']):
      errors.append(response)
  
  return errors

def validate(field, value):
  """
  - validating field values with regular expressions and otherwise return error messages

  Args:
      field (str): field name to validate
      value (any): field value to validate

  Returns:
      dict: dictionary with fields ok (bool) and error (str) if necessary
  """
  match = bool(re.fullmatch(PATTERNS.get(field,{}).get('pattern', r'.+'),value,re.UNICODE))
  extra = PATTERNS.get(field,{}).get('extra', None)
  if (match and extra):
    match = extra(value)
  result = {'ok': match}
  if (not result['ok']):
    result['error'] = f'Error en el campo "{field}": {PATTERNS[field]['error']}'
  
  return result

if (__name__ == '__main__'):
  print(validate('depto_residencia','Grl. José de San Martín'))