REPORT_FIELDS = {
  'sexo': {
    'name': 'Distribución por Género',
    'M': 'Masculino',
    'F': 'Femenino'
  },
  'jurisdiccion_residencia': {
    'name': 'Dosis por Jurisdicción de Residencia'
  },
  'vacuna': {
    'name': 'Vacunas Aplicadas por Tipo de Vacuna'
  }
}

PATTERNS = {
  'sexo': {
      'pattern': r'M|F',
      'error': 'solo se aceptan M o F'
  },
  'grupo_etario': {
    'pattern': r'(\d{2}-\d{2})|(<\d{2})',
    'error': 'solo se aceptan DD-DD o <DD'
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
    'error': 'solo se aceptan YYYY-MM-DD'
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
