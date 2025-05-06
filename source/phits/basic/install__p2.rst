####################################
インストール (2) OneAPI リビルド
####################################

==============================
概要
==============================

* PHITSをIntel OneAPI環境下で再ビルドし、MPIやOpenMPに対応した実行ファイルを構築する．
* PHITSのインストールでは、 (1) ライブラリや反応断面積データベースのディプロイ、(2) コンパイル、 (3) パス設定などを実施しているはず．
* 既存インストールのPHITSで、srcディレクトリ内のMakefileを編集し、再コンパイルすれば、 :blue:`OneAPIコンパイラ（ifx）を用いたPHITSへ変更可能` ．


|
  
==============================
手順概要
==============================

1. OneAPIをインストール（Fortranのページ参照）．
2. phits/src/にて、  :blue:`makefile` を編集．
3. makeを実行．
4. 作成された実行ファイルをphits/bin/へコピーして、phits.shの対象実行ファイルを書き換える．
5. 上記、2-4は、OMP, MPI, 両方なしの３種類で作成する．

|

---------------------------------------------------------
Makefileの編集
---------------------------------------------------------

phits/src/makefile 内のビルド構成を変更する．

- 既存の `LinIfort` セクション (  :blue:`ifeqでマッチしている箇所` )を複製し、`LinuxOneAPI` の新たなセクションを作成する．
- ``FC=mpiifort`` を ``FC=mpiifx`` に，または ``FC=ifort`` を ``FC=ifx`` に変更する．
- LinIfortで検索して、引っかかる部分は、LinuxOneAPIにもマッチするように、適宜複製．(面倒であれば、LinIfortのFCを置き換えても良い．)
- 必要に応じて ``FFLAGS`` も適宜調整する（例：`-O3 -xHost -heap-arrays` など）．

|
  
------------------------------
USEOMP, USEMPI の組み合わせ
------------------------------

以下の3パターンをそれぞれ make 時に定義してビルドする：

- **USEOMP=0 USEMPI=0**：シングルスレッド版（逐次実行用）
- **USEOMP=1 USEMPI=0**：OpenMP並列化版
- **USEOMP=0 USEMPI=1**：MPI並列化版

ビルド例：

.. code-block:: bash

   make -j 8 ENVFLAGS=LinuxOneAPI USEOMP=0 USEMPI=0
   make -j 8 ENVFLAGS=LinuxOneAPI USEOMP=1 USEMPI=0
   make -j 8 ENVFLAGS=LinuxOneAPI USEOMP=0 USEMPI=1

|
  
---------------------------------------------------------
実行ファイルの配置
---------------------------------------------------------

ビルドされた実行ファイルは、`phits/` ディレクトリ下に次のようなファイル名で出力される：

-  `phits_LinuxOneAPI` （シングルスレッド版）
-  `phits_LinuxOneAPI_OMP` （OpenMP版）
-  `phits_LinuxOneAPI_MPI` （MPI版）

これらを `phits/bin` ディレクトリにコピーする．

|

---------------------------------------------------------
phits.sh の修正
---------------------------------------------------------

PHITS起動スクリプト `phits/bin/phits.sh` を編集し、実行対象を以下のように変更する：

.. code-block:: bash

   PHITS_SINGLE_EXE=phits_LinuxOneAPI
   PHITS_OMP_EXE=phits_LinuxOneAPI_OMP
   PHITS_MPI_EXE=phits_LinuxOneAPI_MPI

これにより、`phits.sh` 実行時に OneAPI + MPI 版 PHITS を使用するようになる．

|

==============================
補足
==============================

OneAPI の環境を有効にするには、以下の実行が必要：

.. code-block:: bash

   source /opt/intel/oneapi/setvars.sh

makefileがわかってない場合は、コンパイラの位置として、絶対パスを指定するなどする．

|
