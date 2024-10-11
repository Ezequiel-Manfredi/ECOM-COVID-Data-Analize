class CountBy:
  def __init__(self,counterFields,percentageField):
    self.selectedFields = {
      field : {}
      for field in counterFields + percentageField
    }
    self.counterFields = counterFields
    self.percentageField = percentageField
    self.total = 0
  
  def process(self,record):
    """
    - counter of diferent columns values
    - for each column, for each diferent value

    Args:
        record (dict): row information
    """
    self.total += 1
    for key in self.selectedFields:
      self.selectedFields[key][record[key]] = self.selectedFields.get(key, 0).get(record[key], 0) + 1
  
  def show(self):
    """
    - emit counter's report
    """
    print(self.total)
    print(self.selectedFields)
