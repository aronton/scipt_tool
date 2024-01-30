#!/bin/bash
#SBATCH --partition=replace1
#SBATCH --ntasks=1
#SBATCH --job-name=replace2
#SBATCH --cpus-per-task=replace3
#SBATCH --output=replace4

date

echo -e "current dir:"
pwd

output=${13}

if [ -d "${output}" ]; then
    # 目錄 /path/to/dir 存在
    echo -e "${output}"
else
    # 目錄 /path/to/dir 不存在
    echo -e "mkdir""${output}"
    mkdir -p "${output}"
fi

get_script_dir () {
     SOURCE="${BASH_SOURCE[0]}"
     # While $SOURCE is a symlink, resolve it
     while [ -h "$SOURCE" ]; do
          DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
          SOURCE="$( readlink "$SOURCE" )"
          # If $SOURCE was a relative symlink (so no "/" as prefix, need to resolve it relative to the symlink base directory
          [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE"
     done
     DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
     echo "$DIR"
}

echo "script_directory"
echo "$(get_script_dir)"

Spin=${1}

L=${2}

J=${3}

D=${4}

BC=${5}

bonDim=${6}

Pdis=${7}

s1=${8}

s2=${9}

CheckOrNot=${10}

Ncore=${11}

tSDRG_path=${12}

echo "Spin         ==> $Spin"
echo "L         ==> $L"
echo "J         ==> $J"
echo "D         ==> $D"
echo "BC        ==> $BC"
echo "bonDim        ==> $bonDim"
echo "Pdis        ==> $Pdis"
echo "s1        ==> $s1"
echo "s2        ==> $s2"
echo "CheckOrNot        ==> $CheckOrNot"
echo "Ncore        ==> $Ncore"
echo "tSDRG_path        ==> $tSDRG_path"

# for (( s=0; s<${numOfinterval}; s=s+1 ))
# do
#      echo "tSDRG_path/tSDRG/Main/Spin${spin}_random.exe $L $bonDim $Pdis $J $D $BC $s1 $s2 $CheckOrNot"
# done
echo $tSDRG_path"/tSDRG/Main_"$Spin"/Spin"$Spin"_random.exe $L $bonDim $Pdis $J $D $BC $s1 $s2 $CheckOrNot"

date
