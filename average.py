import sys
import os
import datetime
import scriptCreator

task = input("What is the task? (a)submit, (b)resubmit, (c)cancel Jobs: : \n")
print(task)
# parameterlist = {"Spin":None,"L1":None,"L2":None,"delta_L":None,"J1":None,"J2":None,"delta_J":None,\
#                  "D1":None,"D2":None,"delta_D":None,"Pdis":None,"bondDim":None,"initialSampleNumber":None,\
#                  "finalSampleNumber":None,"sampleDelta":None,"check_Or_Not":None}

parameterlist = {"Spin":None,"L":{"L1":None,"L2":None,"delta_L":None},"J":{"J1":None,"J2":None,"delta_J":None},\
                 "D":{"D1":None,"D2":None,"delta_D":None},"seed":{"s1":None,"s2":None,"delta_s":None},\
                 "BC":None,"Pdis":None,"bondDim":None,"dx":None,"check_Or_Not":None}
Ncore = input("Ncore : \n")
partition = input("partition : \n")
print("key in parameter in the following format : \n\
ex : Spin, L1, L2, delta_L, J1, J2, delta_J, D1, D2, delta_D, Pdis, bondDim, initialSampleNumber, finalSampleNumber, sampleDelta, check_Or_Not\n\
ex : 15(Spin) 64(L) 1.1(J) 0.1(D) 10(Pdis) 40(bondDim) 1(initialSampleNumber) 20(finalSampleNumber) 5(sampleDelta), Y(check_Or_Not)\n")

Spin=parameterlist["Spin"]=input("Spin : ")

L1=parameterlist["L"]["L1"]=input("L1 : ")
L2=parameterlist["L"]["L2"]=input("L2 : ")
dL=parameterlist["L"]["delta_L"]=input("delta_L : ")

J1=parameterlist["J"]["J1"]=input("J1 : ")
J2=parameterlist["J"]["J2"]=input("J2 : ")
dJ=parameterlist["J"]["delta_J"]=input("delta_J : ")

D1=parameterlist["D"]["D1"]=input("D1 : ")
D2=parameterlist["D"]["D2"]=input("D2 : ")
dD=parameterlist["D"]["delta_D"]=input("delta_D : ")

s1=parameterlist["seed"]["s1"]=int(input("initialSampleNumber : "))
s2=parameterlist["seed"]["s2"]=int(input("finalSampleNumber : "))
ds=parameterlist["seed"]["delta_s"]=int(input("sampleDelta : "))

Pdis=parameterlist["Pdis"]=input("Pdis : ")
dx=parameterlist["dx"]=input("dx : ")
bondDim=parameterlist["bondDim"]=input("bondDim : ")
BC=parameterlist["BC"]=input("BC : ")

# parameterlist["initialSampleNumber"]=int(input("initialSampleNumber : "))
# parameterlist["finalSampleNumber"]=int(input("finalSampleNumber : "))
# parameterlist["sampleDelta"]=int(input("sampleDelta : "))

# mark = parameterlist["check_Or_Not"]
# while mark != "Y" or mark != "N":
parameterlist["check_Or_Not"]=input("check_Or_Not(Y/N) : ")

# for j in 
# print(tSDRG_path)

print(parameterlist,"\n")
for s in parameterlist:
    print(s," : ",parameterlist[s])


L=scriptCreator.Lpara("L",parameterlist["L"])
# L=Lpara("L",parameterlist["L"])

L_num = L.toL()
L_str = L.toStr()

S=scriptCreator.Spara("Seed",parameterlist["seed"])
# S=Spara("Seed",parameterlist["seed"])

S_num = S.toS()
S_str = S.toStr()

J=scriptCreator.paraList("Jdis",parameterlist["J"])
# J=paraList("Jdis",parameterlist["J"])

J_num = J.toFlo()
J_str = J.toStr()

D=scriptCreator.paraList("Dim",parameterlist["D"])
# D=paraList("Dim",parameterlist["D"])

D_num = D.toFlo()
D_str = D.toStr()

tSDRG_path="/home/aronton/tSDRG_random"
# tSDRG_record=tSDRG_path + "/tSDRG" + "/Main_" + str(Spin) + "/submit_record"
# fileName="/tSDRG_Spin=" + str(Spin) + ";BC=" + str(BC) + ";P="+ str(Pdis) + ";B=" + str(bondDim) \
#     + ";L=" + str(L1) + "_" + str(L2) + "(" + str(dL) + ");J=" + str(J1) + "_" + str(J2) +"(" + str(dJ) + ");D="\
#     + str(D1) + "_" + str(D2) + "(" + str(dD) +");"\
#     + "seed1=" + str(s1) + "_seed2=" + str(s2) + ";Partition=" + str(partition) + ";Number_of_core=" + str(Ncore)
# print(fileName)
# nt=datetime.datetime.now()
# now_date = "/" + str(nt.year) + "/" + str(nt.month) + "_" + str(nt.day)
# now_time = "/" + str(nt.hour) + "_" + str(nt.minute)
# fileDir=tSDRG_record + now_date + now_time
# print(fileDir)

# if os.path.exists(fileDir):
#     print(fileDir)
# else:
#     os.makedirs(fileDir)

# file = fileDir + fileName
# print(file)
# if [ -d "${fileDir}" ]; then
#     # 目錄 /path/to/dir 存在
#     echo -e "${fileDir}"
# else
#     # 目錄 /path/to/dir 不存在
#     echo -e "mkdir -p ""${fileDir}"
#     mkdir -p "${fileDir}"
# fi

# file=${fileDir}${fileName}

# echo -e "\n\ntSDRG_Spin="${Spin}";BC=${BC}"";P="${P}";B="${bonDim}";""\n""L="${L1}"_"${L2}"("${space_L}");""\n""J="${J1dis}"_"${J2dis}"("${space_J_100}");""\n""D="${dim1}"_"${dim2}"("${space_D_100}");""\n""seed1="${s1}"_seed2="${s2}";""\n""Partition="${partition}";Number_of_core="${Ncore}"\n\n" >> "${file}.txt"

# echo -e "\n\ntSDRG_Spin="${Spin}";BC=${BC}"";P="${P}";B="${bonDim}";""\n""L="${L1}"_"${L2}"("${space_L}");""\n""J="${J1dis}"_"${J2dis}"("${space_J_100}");""\n""D="${dim1}"_"${dim2}"("${space_D_100}");""\n""seed1="${s1}"_seed2="${s2}";""\n""Partition="${partition}";Number_of_core="${Ncore}"\n\n"

# date >> "${file}.txt"

def submut(parameterlist, Ncore, partition, tSDRG_path):

    Spin=parameterlist["Spin"]
    L1=parameterlist["L"]["L1"]
    L2=parameterlist["L"]["L2"]
    dL=parameterlist["L"]["delta_L"]

    J1=parameterlist["J"]["J1"]
    J2=parameterlist["J"]["J2"]
    dJ=parameterlist["J"]["delta_J"]

    D1=parameterlist["D"]["D1"]
    D2=parameterlist["D"]["D2"]
    dD=parameterlist["D"]["delta_D"]

    s1=parameterlist["seed"]["s1"]
    s2=parameterlist["seed"]["s2"]
    ds=parameterlist["seed"]["delta_s"]

    Pdis=parameterlist["Pdis"]=input("Pdis : ")
    dx=parameterlist["dx"]=input("dx : ")
    bondDim=parameterlist["bondDim"]=input("bondDim : ")
    BC=parameterlist["BC"]=input("BC : ")
    mark=parameterlist["check_Or_Not"]

    L=scriptCreator.Lpara("L",parameterlist["L"])
    L_num = L.toL()
    L_str = L.toStr()

    S=scriptCreator.Spara("Seed",parameterlist["seed"])
    S_num = S.toS()
    S_str = S.toStr()

    J=scriptCreator.paraList("Jdis",parameterlist["J"])
    J_num = J.toFlo()
    J_str = J.toStr()

    D=scriptCreator.paraList("Dim",parameterlist["D"])
    D_num = D.toFlo()
    D_str = D.toStr()

    tSDRG_record=tSDRG_path + "/tSDRG" + "/Main_" + str(Spin) + "/submit_record"

    fileName="/tSDRG_Spin=" + str(Spin) + ";BC=" + str(BC) + ";P="+ str(Pdis) + ";B=" + str(bondDim) \
        + ";L=" + str(L1) + "_" + str(L2) + "(" + str(dL) + ");J=" + str(J1) + "_" + str(J2) +"(" + str(dJ) + ");D="\
        + str(D1) + "_" + str(D2) + "(" + str(dD) +");"\
        + "seed1=" + str(s1) + "_seed2=" + str(s2) + ";Partition=" + str(partition) + ";Number_of_core=" + str(Ncore)

    nt=datetime.datetime.now()
    now_date = "/" + str(nt.year) + "/" + str(nt.month) + "_" + str(nt.day)
    now_time = "/" + str(nt.hour) + "_" + str(nt.minute) + "_" + str(nt.second)
    
    fileDir=tSDRG_record + now_date + now_time

    if os.path.exists(fileDir):
        print(fileDir)
    else:
        os.makedirs(fileDir)

    file = fileDir + fileName

    for l_i,l in enumerate(L_str):
        for j_i,j in enumerate(J_str):
            for d_i,d in enumerate(D_str):
                for s_i in range(len(S_num)):
                    for s in S_str[s_i]:
                        fh = open("run.sh",r)
                        context = fh.readlines()
                        scriptName = str(Spin) + "_" + "L" + str(l) + "_" + j + "_" + d + \
                            "_" + "P" + str(Pdis) + "_" + "BC=" + str(BC) + "_Ncore=" + Ncore \
                                + "_seed1=" + str(s1) + "_seed2=" + str(s2) + "_" + now_time
                # print(f"{m}_{n}_{o}_{s}")
def resubmit(L_str,J_str,D_str,S_num):
    for l_i,l in enumerate(L_str):
        for j_i,j in enumerate(J_str):
            for d_i,d in enumerate(D_str):
                for s_i in range(len(S_num)):
                    for s in S_str[s_i]:
def cancel(L_str,J_str,D_str,S_num):
    job_list = os.popen("squeue -u aronton -o \"%%.12i %%.12P %%.90j %%.8T\"")
    del job_list[0]
    for l_i,l in enumerate(L_str):
        for j_i,j in enumerate(J_str):
            for d_i,d in enumerate(D_str):
                for s_i in range(len(S_num)):
                    for s in S_str[s_i]: