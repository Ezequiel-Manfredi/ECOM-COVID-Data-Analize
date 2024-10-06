import re

PATTERNS = {
  'SEXO': re.compile('M|F'),
  'RANGO_EDAD': re.compile('(\d{2}-\d{2})|((\<|\>)\d{2})'),
  'FECHA': re.compile('\d{4}-\d{2}-\d{2}')
}

validators = [
  {
    'field': 'sexo',
    'validate': [
      lambda value: bool(PATTERNS['SEXO'].match(value))
    ]
  },
  {
    'field': 'grupo_etario',
    'validate': [
      lambda value: bool(PATTERNS['RANGO_EDAD'].match(value))
    ]
  },
  {
    'field': 'fecha_aplicacion',
    'validate': [
      lambda value: bool(PATTERNS['FECHA'].match(value))
    ]
  }
]