from datetime import datetime

# row values extracted to a list 
lineToList = lambda x: x.replace('\n','').split(',')

REPORT_FIELDS = {
  'sexo': {
    'name': 'Distribución por Género (sexo)',
    'M': 'Masculino',
    'F': 'Femenino'
  },
  'jurisdiccion_residencia': {
    'name': 'Dosis por Jurisdicción de Residencia (jurisdiccion_residencia)'
  },
  'vacuna': {
    'name': 'Vacunas Aplicadas por Tipo de Vacuna (vacuna)'
  }
}

def extraAgeValidation(value):
  elements = value.split('-')
  if len(elements) > 1 and int(elements[1]) - int(elements[0]) < 0:
    return False
  return True
def extraDateValidation(value):
  recordDate = datetime.strptime(value, "%Y-%m-%d")
  return recordDate.date() < datetime.now().date()

PATTERNS = {
  'sexo': {
      'pattern': r'M|F',
      'error': 'solo se aceptan M o F'
  },
  'grupo_etario': {
    'pattern': r'(\d{2}-\d{2})|(<\d{2})',
    'extra': extraAgeValidation,
    'error': 'solo se aceptan mm-MM o <MM'
  },
  'jurisdiccion_residencia': {
    'pattern': r'[A-Za-zÀ-ÖØ-öø-ÿ\s\.]+',
    'error': 'solo se aceptan palabras y espacios'
  },
  'jurisdiccion_residencia_id': {
    'pattern': r'\d+',
    'error': 'solo se aceptan enteros positivos'
  },
  'depto_residencia': {
    'pattern': r'[A-Za-zÀ-ÖØ-öø-ÿ\s\.\d]+',
    'error': 'solo se aceptan palabras enteros positivos y espacios'
  },
  'depto_residencia_id': {
    'pattern': r'\d+',
    'error': 'solo se aceptan enteros positivos'
  },
  'jurisdiccion_aplicacion': {
    'pattern': r'[A-Za-zÀ-ÖØ-öø-ÿ\s\.]+',
    'error': 'solo se aceptan palabras y espacios'
  },
  'jurisdiccion_aplicacion_id': {
    'pattern': r'\d+',
    'error': 'solo se aceptan enteros positivos'
  },
  'depto_aplicacion': {
    'pattern': r'[A-Za-zÀ-ÖØ-öø-ÿ\s\.\d]+',
    'error': 'solo se aceptan palabras enteros positivos y espacios'
  },
  'depto_aplicacion_id': {
    'pattern': r'\d+',
    'error': 'solo se aceptan enteros positivos'
  },
  'fecha_aplicacion': {
    'pattern': r'\d{4}-\d{2}-\d{2}',
    'extra': extraDateValidation,
    'error': 'solo se aceptan YYYY-MM-DD antes del presente'
  },
  'vacuna': {
    'pattern': r'[A-Za-zÀ-ÖØ-öø-ÿ\s\.\d]+',
    'error': 'solo se aceptan palabras enteros positivos y espacios'
  },
  'cod_dosis_generica': {
    'pattern': r'\d+',
    'error': 'solo se aceptan enteros positivos'
  },
  'nombre_dosis_generica': {
    'pattern': r'[A-Za-zÀ-ÖØ-öø-ÿ\s\.\d]+',
    'error': 'solo se aceptan palabras y espacios'
  },
  'condicion_aplicacion': {
    'pattern': r'[A-Za-zÀ-ÖØ-öø-ÿ\s\.\d]+',
    'error': 'solo se aceptan palabras enteros positivos y espacios'
  },
  'orden_dosis': {
    'pattern': r'\d+',
    'error': 'solo se aceptan enteros positivos'
  },
  'lote_vacuna': {
    'pattern': r'\w+\-?\w+',
    'error': 'solo se aceptan letras enteros positivos y un "-" opcional '
  },
  'id_persona_dw': {
    'pattern': r'\d+\.\d+',
    'error': 'solo se aceptan reales positivos con separador "."'
  }
}
