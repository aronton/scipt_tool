import re
import os

class paraList:
    def __init__(self,title,numlist):
        numlist = list(numlist.values())
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

class Lpara(paraList):
    def __init__(self,title,numlist):
        numlist = list(numlist.values())
        self.x1 = int(numlist[0])
        self.x2 = int(numlist[1])
        self.dx = int(numlist[2])
        self.title = title
    def toL(self):
        numL = [self.x1 + l*self.dx for l in range(int((self.x2-self.x1)/self.dx) + 1)]
        return list(numL)   
    def toStr(self):
        if self.x2>0:
            numL = [ self.title + str(self.x1 + l*self.dx) for l in range(int((self.x2-self.x1)/self.dx) + 1)]
        else:
            numL = [ self.title + "N" + str((self.x1 + l*self.dx)*-1) for l in range(int((self.x2-self.x1)/self.dx) + 1)]    
        return list(numL)    
    def __repr__(self):
        return f'Point({self.x1}, {self.x2}, {self.dx})'

class Spara(paraList):
    def __init__(self,title,numlist):
        numlist = list(numlist.values())
        self.x1 = int(numlist[0])
        self.x2 = int(numlist[1])
        self.dx = int(numlist[2])
        self.title = title
    def toS(self):
        numSeed = []
        for i in list(range(self.x1 ,self.x2, self.dx)):
            a = [j for j in list(range(i,i+5))]
            numSeed.append(a)
        # print(numSeed)
        # numL = [self.x1 + l*self.dx for l in range(int((self.x2-self.x1)/self.dx) + 1)]
        return list(numSeed)   
    def toStr(self):
        if self.x2>0:
            strSeed = []
            for i in list(range(self.x1 ,self.x2,self.dx)):
                a = [self.title + str(j) for j in list(range(i,i+self.dx))]
                strSeed.append(a)
            # numL = [ self.title + str(self.x1 + l*self.dx) for l in range(int((self.x2-self.x1)/self.dx) + 1)]
        else:
            strSeed = []
            for i in list(range(self.x1 ,self.x2,self.dx)):
                a = [self.title + "N" + str(j) for j in list(range(i,i+self.dx))]
                strSeed.append(a)
            # numL = [ self.title + "N" + str((self.x1 + l*self.dx)*-1) for l in range(int((self.x2-self.x1)/self.dx) + 1)]    
        return list(strSeed)    
    def __repr__(self):
        return f'Point({self.x1}, {self.x2}, {self.dx})'

if __name__ == '__main__':
    main(paraList.toStr("Jdis",[0.1,0.5,0.1]))