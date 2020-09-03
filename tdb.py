import os
class tdb:
  def __init__(self, name):
    self.name = name
    if not os.path.exists(self.name):
      open(self.name,"w+").close() # touch file
    self.file = open(self.name, "r+")
    self.db = self.load()

  def commit(self, db=None):
    if db != None: self.db = db
    self.file.truncate(0)
    for key in self.db:
      self.file.write("{};{};\n".format(key,self.db[key]))

  def load(self):
    data = {}
    for line in self.file.readlines():
      line=line.split(";")
      data[line[0]] = line[1]
    return data

  def put(self, key, value):
    self.db[key] = value

  def get(self, key):
    return self.db[key]

  def rm(self, key):
    del self.db[key]

