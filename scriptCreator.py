class D(dList):
    def __int__(self,d1,d2,delta):
        self.d1 = dList["d1"]
        self.d2 = dList["d1"]
        self.delta = dList["delta_D"]
    def d_to_str(self):
        dim1 = self.d1.split(".")
        dim2 = self.d2.split(".")
        dim_delta = self.delta.split(".")
        return [dim1,dim2,dim_delta]
    
x={"d1":0.1,"d2":0.2"delta_D":0.1}

d=D(x)