import re
import os

class paraList:
    def __init__(self,title,inlist):
        # self._numlist = list(numlist.values())
        self.p_list = list(inlist.values())
        self.p_num_list = []
        self.set_p_num_list(title,list(inlist.values()))
        self.p_s100_list = []
        self.set_p_s100_list(title,list(inlist.values()))
        self.p_str_list = []
        self.set_p_str_list(title,self.p_s100_list.copy())

        self.s100_list = []
        self.set_s100_list(title,self.p_s100_list.copy())
        self.num_list = []
        self.set_num_list(title,self.s100_list.copy())
        self.str_list = []
        self.set_str_list(title,self.s100_list.copy())
    def set_p_num_list(self,title,inlist):
        for s in inlist:
            l = [c for c in s if c.isdigit()]
            if "." in s:
                l.insert(1,".")
                x = "".join(l)
                x1 = float("".join(x))
                self.p_num_list.append(x1)
    def set_p_s100_list(self,title,inlist):
        for s in inlist:
            l = [c for c in s if c.isdigit()]
            if len(l) == 2:
                l.append("0")
            elif len(l) == 1:
                l.append("00")
            x = "".join(l)
            # x1 = "".join(x)
            self.p_s100_list.append(x)
    def set_p_str_list(self,title,inlist):
        self.p_str_list = []
        for s in inlist:
            self.p_str_list.append(title + s)
    def set_s100_list(self,title,inlist):
        if inlist[0] == inlist[1]:
            l = []
            l.append(inlist[0])
        else:
            n = int((int(inlist[1]) - int(inlist[0]))/int(inlist[2]))
            l = []
            for i in range(n+1):
                if len(str(int(inlist[0]) + i*int(inlist[2])))==2:
                    l.append("0"+str(int(inlist[0]) + i*int(inlist[2])))
                else:
                    l.append(str(int(inlist[0]) + i*int(inlist[2])))
        self.s100_list = list(l)
    def set_num_list(self,title,inlist):
        print(inlist)
        l = []
        for s in inlist:
            l.append(float(s[0]+"."+s[1]+s[2]))
        self.num_list = list(l)
    def set_str_list(self,title,inlist):
        l = []
        for s in inlist:
            l.append(title + s)
        self.str_list = list(l)
        

# class paraList:
#     def __init__(self,title,numlist):
#         numlist = list(numlist.values())
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
#     def to100(self):
#         list100 = []
#         [list100.append(int(100*a)) for a in self.floatlist]
#         return list(list100)
#     def __repr__(self):
#         return f'Point({self.x1}, {self.x2}, {self.dx})'

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
            a = [j for j in list(range(i,i+self.dx))]
            numSeed.append(a)
        return list(numSeed)   
    def toStr(self):
        if self.x2>0:
            strSeed = []
            for i in list(range(self.x1 ,self.x2,self.dx)):
                a = [self.title + str(j) for j in list(range(i,i+self.dx))]
                strSeed.append(a)
        else:
            strSeed = []
            for i in list(range(self.x1 ,self.x2,self.dx)):
                a = [self.title + "N" + str(j) for j in list(range(i,i+self.dx))]
                strSeed.append(a)
        return list(strSeed)    
    def __repr__(self):
        return f'Point({self.x1}, {self.x2}, {self.dx})'
