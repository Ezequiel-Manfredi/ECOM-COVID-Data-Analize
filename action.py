class CountBy:
  def __init__(self,fields):
    self.selectedFields = {
      field : {}
      for field in fields
    }
  
  def process(self,record):
    for key in self.selectedFields.keys():
      self.selectedFields[key][record[key]] = self.selectedFields.get(key, 0).get(record[key], 0) + 1
  
  def show(self):
    print(self.selectedFields)
