import sys


task = input("What is the task? (a)submit, (b)resubmit, (c)cancel Jobs: : ")
print(task)
parameterlist = {"Spin":None,"L1":None,"L2":None,"delta_L":None,"J1":None,"J2":None,"delta_J":None,\
                 "D1":None,"D2":None,"delta_D":None,"Pdis":None,"bondDim":None,"initialSampleNumber":None,\
                 "finalSampleNumber":None,"sampleDelta":None,"check_Or_Not":None}
print("key in parameter in the following format : \n\
ex : Spin, L1, L2, delta_L, J1, J2, delta_J, D1, D2, delta_D, Pdis, bondDim, initialSampleNumber, finalSampleNumber, sampleDelta, check_Or_Not\n\
ex : 15(Spin) 64(L) 1.1(J) 0.1(D) 10(Pdis) 40(bondDim) 1(initialSampleNumber) 20(finalSampleNumber) 5(sampleDelta), Y(check_Or_Not)\n")

parameterlist["Spin"]=input("Spin : ")

parameterlist["L1"]=input("L1 : ")
parameterlist["L2"]=input("L2 : ")
parameterlist["delta_L"]=input("delta_L : ")

parameterlist["J1"]=input("J1 : ")
parameterlist["J2"]=input("J2 : ")
parameterlist["delta_J"]=input("delta_J : ")

parameterlist["D1"]=input("D1 : ")
parameterlist["D2"]=input("D2 : ")
parameterlist["delta_D"]=input("delta_D : ")

parameterlist["Pdis"]=input("Pdis : ")
parameterlist["bondDim"]=input("bondDim : ")
parameterlist["initialSampleNumber"]=int(input("initialSampleNumber : "))
parameterlist["finalSampleNumber"]=int(input("finalSampleNumber : "))
parameterlist["sampleDelta"]=int(input("sampleDelta : "))

mark = parameterlist["check_Or_Not"]
while mark != "Y" or mark != "N":
    mark = input("check_Or_Not(Y/N) : ")
    parameterlist["check_Or_Not"]=mark

print(parameterlist,"\n")
for s in parameterlist:
    print(s," : ",parameterlist[s])
