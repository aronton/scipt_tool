import sys
import os
import datetime
import scriptCreator

task = input("What is the task? (a)submit, (b)resubmit, (c)cancel Jobs: : \n")
print(task)
# parameterlist = {"Spin":None,"L1":None,"L2":None,"delta_L":None,"J1":None,"J2":None,"delta_J":None,\
#                  "D1":None,"D2":None,"delta_D":None,"Pdis":None,"bondDim":None,"initialSampleNumber":None,\
#                  "finalSampleNumber":None,"sampleDelta":None,"check_Or_Not":None}

parameterlist = {"Spin":None,"L":{"L1":None,"L2":None,"dL":None},"J":{"J1":None,"J2":None,"dJ":None},\
                 "D":{"D1":None,"D2":None,"dD":None},"seed":{"s1":None,"s2":None,"ds":None},\
                 "BC":None,"Pdis":None,"bondDim":None,"dx":None,"check_Or_Not":None}
Ncore = input("Ncore : \n")
partition = input("partition : \n")
print("key in parameter in the following format : \n\
ex : Spin, L1, L2, delta_L, J1, J2, delta_J, D1, D2, delta_D, Pdis, bondDim, initialSampleNumber, finalSampleNumber, sampleDelta, check_Or_Not\n\
ex : 15(Spin) 64(L) 1.1(J) 0.1(D) 10(Pdis) 40(bondDim) 1(initialSampleNumber) 20(finalSampleNumber) 5(sampleDelta), Y(check_Or_Not)\n")

parameterlist["Spin"]=input("Spin : ")

parameterlist["L"]["L1"]=input("L1 : ")
parameterlist["L"]["L2"]=input("L2 : ")
parameterlist["L"]["dL"]=input("dL : ")

parameterlist["J"]["J1"]=input("J1 : ")
parameterlist["J"]["J2"]=input("J2 : ")
parameterlist["J"]["dJ"]=input("dJ : ")

parameterlist["D"]["D1"]=input("D1 : ")
parameterlist["D"]["D2"]=input("D2 : ")
parameterlist["D"]["dD"]=input("dD : ")

parameterlist["seed"]["s1"]=int(input("initialSampleNumber : "))
parameterlist["seed"]["s2"]=int(input("finalSampleNumber : "))
parameterlist["seed"]["ds"]=int(input("sampleDelta : "))
parameterlist["BC"] = input("BC : ")
parameterlist["Pdis"] = int(input("Pdis : "))
parameterlist["bondDim"] = int(input("bondDim : "))
parameterlist["dx"] = int(input("dx : "))


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

tSDRG_path="/home/aronton/tSDRG_random"

# for l_i,l in enumerate(L_str):
#     for j_i,j in enumerate(J_str):
#         for d_i,d in enumerate(D_str):
#             for s_i in range(len(S_num)):
#                 for s in S_str[s_i]:
#                     parameterlist.append({"Spin":Spin,"L":l,"J":j,"D":d,"P":Pdis,"BC":BC,"seed1":s1,"seed2":s2})
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

    p = parameterlist

    L=scriptCreator.Lpara("L",parameterlist["L"])
    L_num = L.toL()
    L_str = L.toStr()


    S=scriptCreator.Spara("Seed",parameterlist["seed"])
    S_num = S.toS()
    S_str = S.toStr()
    s1 = parameterlist["seed"]["s1"]
    s2 = parameterlist["seed"]["s2"]

    J=scriptCreator.paraList("Jdis",parameterlist["J"])
    J_num = J.toFlo()
    J_str = J.toStr()
    J_100 = J.to100()

    D=scriptCreator.paraList("Dim",parameterlist["D"])
    D_num = D.toFlo()
    D_str = D.toStr()
    D_100 = D.to100()

    Spin=parameterlist["Spin"]
    Pdis=parameterlist["Pdis"]
    dx=parameterlist["dx"]
    bondDim=parameterlist["bondDim"]
    BC=parameterlist["BC"]
    check_Or_Not=parameterlist["check_Or_Not"]

    tSDRG_record = tSDRG_path + "/tSDRG" + "/Main_" + str(Spin) + "/submit_record"
    record_dir = tSDRG_path + "/tSDRG" + "/Main_" + str(Spin) + "/jobRecord" 
    script_dir = record_dir + "/script" + "/" + str(BC) + "/B" + str(bondDim)
    output_dir = record_dir + "/slurmOutput" + "/" + str(BC) + "/B" + str(bondDim)

    tSDRG_fileName="/tSDRG_Spin=" + str(Spin) + ";BC=" + str(BC) + ";P="+ str(Pdis) + ";B=" + str(bondDim) \
        + ";L=" + str(L_num[0]) + "_" + str(L_num[-1]) + "(" + str(L_num[1]-L_num[0])\
        + ");J=" + str(J_num[0]) + "_" + str(J_num[-1]) +"(" + str(J_100[1]-J_100[0]) \
        + ");D=" + str(D_num[0]) + "_" + str(D_num[-1]) + "(" + str(D_100[1]-D_100[0]) +");"\
        + "seed1=" + str(s1) + "_seed2=" + str(s2) + ";Partition=" + str(partition) + ";Number_of_core=" + str(Ncore)

    nt=datetime.datetime.now()
    now_year = str(nt.year)
    now_date = str(nt.year) + "_" + str(nt.month) + "_" + str(nt.day)
    now_time = "H" + str(nt.hour) + "_M" + str(nt.minute) + "_S" + str(nt.second)
    
    tSDRG_fileDir = tSDRG_record + "/" + now_year + "/" + now_date

    if os.path.exists(tSDRG_fileDir):
        print(tSDRG_fileDir)
    else:
        os.makedirs(tSDRG_fileDir)

    tSDRG_filePath = tSDRG_fileDir + tSDRG_fileName + "_" + now_time

    with open(tSDRG_filePath, "wt") as file:
        file.write(tSDRG_fileName)

    os.system( "cd " + tSDRG_path + "/tSDRG/Main_" + Spin)
    print("cd " + tSDRG_path + "/tSDRG/Main_" + Spin)
    print("tSDRG_filePath : ",tSDRG_filePath)
    for l_i,l in enumerate(L_str):
        for j_i,j in enumerate(J_str):
            for d_i,d in enumerate(D_str):
                for s_i in range(len(S_num)):
                    s = S_num[s_i]
                    script_path = script_dir + "/" + l + "/" + j + "/" + d  
                    output_path = output_dir + "/" + l + "/" + j + "/" + d
                    if os.path.exists(script_dir):
                        print("exist : ", script_dir)
                    else:
                        print("not exist : ", script_dir)
                        os.makedirs(fileDir)
                    jobName = "Spin" + str(Spin) + "_" + l + "_" + j + "_" + d + \
                                            "_" + "P" + str(Pdis) + "_" + "BC=" + str(BC) + "_Ncore=" + Ncore \
                                                + "_seed1=" + str(s[0]) + "_seed2=" + str(s[-1])
                    script_name = jobName + "_" + now_time
                    script_path = script_path + "/" + script_name + "_random.sh"
                    output_path = output_path + "/" + script_name + "_random.out"
                    print("jobName : ",jobName)
                    print("script_path : ",script_path)
                    print("output_path : ",output_path)
                    with open("run.sh", "rt") as file:
                        context = file.read()
                    with open(script_path, "wt") as file:
                        context = context.replace("replace1", partition)
                        context = context.replace("replace2", jobName)
                        context = context.replace("replace3", Ncore)
                        context = context.replace("replace4", output_path)
                        file.write(context)
                    submit_cmd_list = ["sbatch",script_path, str(Spin),str(L_num[l_i]),str(J_num[j_i]),str(D_num[d_i])\
                    ,str(bondDim),str(Pdis),str(s[0]),str(s[-1]),check_Or_Not,str(Ncore),tSDRG_path,output_path]

                    submit_cmd = " ".join(submit_cmd_list)
                    # "sbatch" + script_path + " " + str(Spin) + " " + str(L_num[l_i]) + " " + str(J_num[j_i]) + \
                    #     " " + str(D_num[d_i]) + " " + str(bondDim) + " " + str(Pdis) + " " + str(s[0]) + " " + str(s[-1]) + \
                    #         " " + check_Or_Not + " " + str(Ncore) + " " + tSDRG_path
                    print("submit_cmd : ",submit_cmd)
                    # os.system("sbatch " + script_path + )
    return 0
# def resubmit(L_str,J_str,D_str,S_num):
#     for l_i,l in enumerate(L_str):
#         for j_i,j in enumerate(J_str):
#             for d_i,d in enumerate(D_str):
#                 for s_i in range(len(S_num)):
#                     for s in S_str[s_i]:
# def cancel(L_str,J_str,D_str,S_num):
#     job_list = os.popen("squeue -u aronton -o \"%%.12i %%.12P %%.90j %%.8T\"")
#     del job_list[0]
#     for l_i,l in enumerate(L_str):
#         for j_i,j in enumerate(J_str):
#             for d_i,d in enumerate(D_str):
#                 for s_i in range(len(S_num)):
#                     for s in S_str[s_i]:

submut(parameterlist, Ncore, partition, tSDRG_path)
