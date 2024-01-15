import re
import os

tSDRG_path = os.system("pwd")

# class paraList:
#     def __init__(self,title,numlist):
#         print(list)
#         self.x1 = float(numlist[0])
#         self.x2 = float(numlist[1])
#         self.dx = float(numlist[2])
#         self.title = title
#         self.floatlist = [ round(self.x1 + i*self.dx,2)  for i in range(round((self.x2 - self.x1)/self.dx + 1))]
#         self.floatlist = list(self.floatlist)
#     def toStr(self):
#         strlist = []
#         for x in self.floatlist:
#             self.s = str(x)
#             self.s = re.sub("\.", "", self.s)
#             if x > 0:
#               self.s = self.title + self.s.ljust(3,"0")
#               self.s = str(self.s)
#             else:
#               self.s = re.sub("\-", "", self.s)
#               self.s = self.s.ljust(3,"0")
#               self.s = self.title + "N" + str(self.s)
#             strlist.append(self.s)
#         return strlist
#     def toFlo(self):
#         return self.floatlist
#     def __repr__(self):
#         return f'Point({self.x1}, {self.x2}, {self.dx})'

# import re

class paraList:
    def __init__(self,title,numlist):
        self.x1 = float(numlist[0])
        self.x2 = float(numlist[1])
        self.dx = float(numlist[2])
        self.title = title
        self.floatlist = [ round(self.x1 + i*self.dx,2)  for i in range(round((self.x2 - self.x1)/self.dx + 1))]
        self.floatlist = list(self.floatlist)
    def toStr(self):
        strlist = []
        for x in self.floatlist:
            self.s = str(x)
            self.s = re.sub("\.", "", self.s)
            if x > 0:
              self.s = self.title + self.s.ljust(3,"0")
              self.s = str(self.s)
            else:
              self.s = re.sub("\-", "", self.s)
              self.s = self.s.ljust(3,"0")
              self.s = self.title + "N" + str(self.s)
            strlist.append(self.s)
        return strlist
    def toFlo(self):
        return self.floatlist
    def __repr__(self):
        return f'Point({self.x1}, {self.x2}, {self.dx})'