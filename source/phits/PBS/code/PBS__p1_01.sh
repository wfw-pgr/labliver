#!/bin/bash
#PBS -N phits                       ### ジョブ名
#PBS -l select=2:ncpus=8:mpiprocs=8 ### 2ノード、各ノード8コア (適宜変更)
#PBS -l walltime=72:00:00           ### 実行時間の上限 ( 72時間 )
#PBS -j oe                          ### 標準出力とエラー出力を統合
#PBS -o stdout                      ### 標準出力ファイル名
#PBS -q queue_001                   ### 使用するキュー名 (各キューシステム参照)


### --- Beginning of job  --- ###
echo
echo "job started at $(date)"
echo

### --- PATH settings     --- ###
export PHITSPATH=/common1/hpclocal/PHITS/phits321/phits
export PATH=${PATH}:/common1/hpclocal/PHITS/phits321/phits/bin
export PATH=${PATH}:/common1/hpclocal/PHITS/phits321/phits/dchain-sp/bin

### --- MPI settings      --- ###
MPI_PATH="/common1/hpclocal/ENV_SET/INTEL19.0/IntelMPI/00-IntelMPI2018.4.sh"
source $MPI_PATH

### --- Preparation       --- ###
cd $PBS_O_WORKDIR                   ### ジョブ投入したディレクトリに移動 ( PBS 予約の環境変数)
PHITS_EXEC=/common1/hpclocal/PHITS/phits321/phits/bin/phits.sh     ### 実行MPIプログラムのパス

### --- Execution         --- ###
INPUT_FILE="inp/execute_phits.inp"
$PHITS_EXEC $PBS_O_WORKDIR/$INPUTFILE

### --- end statement     --- ###
echo 
echo "job finished at $(date)"
echo
