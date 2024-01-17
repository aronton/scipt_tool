import sys
import os

# import scriptCreator

task = input("What is the task? (a)submit, (b)resubmit, (c)cancel Jobs: : ")
print(task)
# parameterlist = {"Spin":None,"L1":None,"L2":None,"delta_L":None,"J1":None,"J2":None,"delta_J":None,\
#                  "D1":None,"D2":None,"delta_D":None,"Pdis":None,"bondDim":None,"initialSampleNumber":None,\
#                  "finalSampleNumber":None,"sampleDelta":None,"check_Or_Not":None}

parameterlist = {"Spin":None,"L":{"L1":None,"L2":None,"delta_L":None},"J":{"J1":None,"J2":None,"delta_J":None},\
                 "D":{"D1":None,"D2":None,"delta_D":None},"seed":{"s1":None,"s2":None,"delta_s":None},\
                 "Pdis":None,"bondDim":None,"dx":None,"check_Or_Not":None}

print("key in parameter in the following format : \n\
ex : Spin, L1, L2, delta_L, J1, J2, delta_J, D1, D2, delta_D, Pdis, bondDim, initialSampleNumber, finalSampleNumber, sampleDelta, check_Or_Not\n\
ex : 15(Spin) 64(L) 1.1(J) 0.1(D) 10(Pdis) 40(bondDim) 1(initialSampleNumber) 20(finalSampleNumber) 5(sampleDelta), Y(check_Or_Not)\n")

parameterlist["Spin"]=input("Spin : ")

parameterlist["L"]["L1"]=input("L1 : ")
parameterlist["L"]["L2"]=input("L2 : ")
parameterlist["L"]["delta_L"]=input("delta_L : ")

parameterlist["J"]["J1"]=input("J1 : ")
parameterlist["J"]["J2"]=input("J2 : ")
parameterlist["J"]["delta_J"]=input("delta_J : ")

parameterlist["D"]["D1"]=input("D1 : ")
parameterlist["D"]["D2"]=input("D2 : ")
parameterlist["D"]["delta_D"]=input("delta_D : ")

parameterlist["seed"]["s1"]=int(input("initialSampleNumber : "))
parameterlist["seed"]["s2"]=int(input("finalSampleNumber : "))
parameterlist["seed"]["delta_s"]=int(input("sampleDelta : "))

parameterlist["Pdis"]=input("Pdis : ")
parameterlist["dx"]=input("dx : ")
parameterlist["bondDim"]=input("bondDim : ")
# parameterlist["initialSampleNumber"]=int(input("initialSampleNumber : "))
# parameterlist["finalSampleNumber"]=int(input("finalSampleNumber : "))
# parameterlist["sampleDelta"]=int(input("sampleDelta : "))

# mark = parameterlist["check_Or_Not"]
# while mark != "Y" or mark != "N":
mark = input("check_Or_Not(Y/N) : ")
parameterlist["check_Or_Not"]=mark

# for j in 
# print(tSDRG_path)

print(parameterlist,"\n")
for s in parameterlist:
    print(s," : ",parameterlist[s])


# L=scriptCreator.Lpara("L",parameterlist["L"])
L=Lpara("L",parameterlist["L"])

L_num = L.toL()
L_str = L.toStr()

# S=scriptCreator.Spara("Seed",parameterlist["seed"])
S=Spara("Seed",parameterlist["seed"])

S_num = S.toS()
S_str = S.toStr()

# print(S_num)
# print(S_str)


# J=scriptCreator.paraList("Jdis",parameterlist["J"])
J=paraList("Jdis",parameterlist["J"])

J_num = J.toFlo()
J_str = J.toStr()

# D=scriptCreator.paraList("Dim",parameterlist["D"])
D=paraList("Dim",parameterlist["D"])

D_num = D.toFlo()
D_str = D.toStr()



# for i,m in enumerate(L_str):
#     for j,n in enumerate(J_str):
#         for k,o in enumerate(D_str):
#             for l in range(len(S_num)-1):
#                 samplelist = list(range(S_num[l],S_num[l+1]))
#                 for s in samplelist:
#                     scriptName = m + "_" + n + "_" + o +"_" + str(s)
#                     print(scriptName)
                # print(f"{m}_{n}_{o}_{s}")