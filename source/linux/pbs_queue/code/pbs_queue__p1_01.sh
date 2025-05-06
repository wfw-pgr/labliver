#!/bin/bash
#PBS -N sample                      ### ジョブ名
#PBS -l select=2:ncpus=8:mpiprocs=8 ### 2ノード、各ノード8コア (適宜変更)
#PBS -l walltime=72:00:00           ### 実行時間の上限 ( 72時間 )
#PBS -j oe                          ### 標準出力とエラー出力を統合
#PBS -o stdout                      ### 標準出力ファイル名
#PBS -q queue_001                   ### 使用するキュー名 (各キューシステム参照)


### --- ジョブの開始  --- ###
echo "Job started on $(hostname) at $(date)"


### ---     準備      --- ###
cd $PBS_O_WORKDIR                   ### ジョブ投入したディレクトリに移動 ( PBS 予約の環境変数)
EXEC=./a.out                        ### 実行MPIプログラムのパス
#
# module load mpi                   ### 必要なモジュールをロード
#

### ---     実行      --- ###
mpiexec -np 4 $(EXEC)               ### 総プロセス数 (-np) を指定 (例: 16プロセス)

### --- ジョブの終了  --- ###
echo "Job finished on $(hostname) at $(date)"
