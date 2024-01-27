#!/bin/bash
#SBATCH --partition=replace1
#SBATCH --ntasks=1
#SBATCH --job-name=replace2
#SBATCH --cpus-per-task=replace3
#SBATCH --output=.replace4

date

echo -e "current dir:"
pwd

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

echo "L         ==> ${1}"
echo "J         ==> ${2}"
echo "D         ==> ${3}"
echo "P        ==> ${4}"
echo "s1        ==> ${5}"
echo "s2        ==> ${6}"
echo "spin        ==> ${7}"
echo "bonDim        ==> ${8}"
echo "BC        ==> ${9}"
echo "Ncore        ==> ${10}"
echo "CheckOrNot        ==> ${11}"

L=${1}

P=${4}

s1=${5}

s2=${6}

spin=${7}

bonDim=${8}

BC=${9}

Ncore=${10}

CheckOrNot=${11}

numOfinterval="10000"


for (( s=0; s<${numOfinterval}; s=s+1 ))
do
     echo "tSDRG_pathm/tSDRG/Main/Spin${spin}_random.exe ${L} ${bonDim} ${P} ${2} ${3} ${BC} ${s1} ${s2} ${CheckOrNot}"
done

date
