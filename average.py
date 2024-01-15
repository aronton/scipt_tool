import sys
import scriptCreator

task = input("What is the task? (a)submit, (b)resubmit, (c)cancel Jobs: : ")
print(task)
# parameterlist = {"Spin":None,"L1":None,"L2":None,"delta_L":None,"J1":None,"J2":None,"delta_J":None,\
#                  "D1":None,"D2":None,"delta_D":None,"Pdis":None,"bondDim":None,"initialSampleNumber":None,\
#                  "finalSampleNumber":None,"sampleDelta":None,"check_Or_Not":None}

parameterlist = {"Spin":None,"L":[None,None,None],"J":[None,None,None],\
                 "D":[None,None,None],"Pdis":None,"bondDim":None,"initialSampleNumber":None,\
                 "finalSampleNumber":None,"dx":None,"sampleDelta":None,"check_Or_Not":None}

print("key in parameter in the following format : \n\
ex : Spin, L1, L2, delta_L, J1, J2, delta_J, D1, D2, delta_D, Pdis, bondDim, initialSampleNumber, finalSampleNumber, sampleDelta, check_Or_Not\n\
ex : 15(Spin) 64(L) 1.1(J) 0.1(D) 10(Pdis) 40(bondDim) 1(initialSampleNumber) 20(finalSampleNumber) 5(sampleDelta), Y(check_Or_Not)\n")

parameterlist["Spin"]=input("Spin : ")

parameterlist["L"][0]=input("L1 : ")
parameterlist["L"][1]=input("L2 : ")
parameterlist["L"][2]=input("delta_L : ")

parameterlist["J"][0]=input("J1 : ")
parameterlist["J"][1]=input("J2 : ")
parameterlist["J"][2]=input("delta_J : ")

parameterlist["D"][0]=input("D1 : ")
parameterlist["D"][1]=input("D2 : ")
parameterlist["D"][2]=input("delta_D : ")

parameterlist["Pdis"]=input("Pdis : ")
parameterlist["dx"]=input("dx : ")
parameterlist["bondDim"]=input("bondDim : ")
parameterlist["initialSampleNumber"]=int(input("initialSampleNumber : "))
parameterlist["finalSampleNumber"]=int(input("finalSampleNumber : "))
parameterlist["sampleDelta"]=int(input("sampleDelta : "))

# mark = parameterlist["check_Or_Not"]
# while mark != "Y" or mark != "N":
mark = input("check_Or_Not(Y/N) : ")
parameterlist["check_Or_Not"]=mark

# for j in 
print(tSDRG_path)

print(parameterlist,"\n")
for s in parameterlist:
    print(s," : ",parameterlist[s])