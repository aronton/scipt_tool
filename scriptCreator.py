import re

class paraList:
    def __init__(self,title,list):
        print(list)
        self.x1 = float(list[0])
        self.x2 = float(list[1])
        self.delta = float(list[2])
        self.title = title
        
    def toStr(self):
        self.dim1 = str(self.x1)
        self.dim2 = str(self.x2)
        self.dimDelta = str(self.delta)

        self.dim1 = re.sub("\.", "", self.dim1)
        self.dim2 = re.sub("\.", "", self.dim2)
        self.dimDelta = re.sub("\.", "", self.dimDelta)

        if self.x1 > 0:
          self.dim1 = self.dim1.ljust(3,"0")
          self.dim1 = str(self.dim1)
        else:
          self.dim1 = re.sub("\-", "", self.dim1)
          self.dim1 = self.dim1.ljust(3,"0")
          self.dim1 = "N" + str(self.dim1)

        if self.x2 > 0:
          self.dim2 = self.dim2.ljust(3,"0")
          self.dim2 = str(self.dim2)
        else:
          self.dim2 = re.sub("\-", "", self.dim2)
          self.dim2 = self.dim2.ljust(3,"0")
          self.dim2 = "N" + str(self.dim2)
          
        if self.delta > 0:
          self.dimDelta = self.dimDelta.ljust(3,"0")
          self.dimDelta = str(self.dimDelta)
        else:
          self.dimDelta = re.sub("\-", "", self.dimDelta)
          self.dimDelta = self.dimDelta.ljust(3,"0")
          self.dimDelta = "N" + str(self.dimDelta)

        return [self.title + self.dim1, self.title + self.dim2, self.title + self.dimDelta] 
    def toFlo(self):
        return [self.x1,self.x2,self.dimDelta]
    def __repr__(self):
        return f'Point({self.x1}, {self.x2}, {self.delta})'
