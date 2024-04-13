##############################################################
intel compiler を用いたelmerのインストール
##############################################################

=========================================================
elmerの運用について
=========================================================

* Elmer-CSCのHPにおけるインストールのインスラクションはGNU Compilerについてのみ記載．
* 現状、one-APIにおいて、intel C/C++ Compiler, intel Fortran Compilerが無料で使用可能なので、使用してコンパイルできるかを挑戦してみる．


|

=========================================================
intel C/C++ Compiler , intel Fortran Compiler 
=========================================================

* インストールについては、別ページにて記載済み．


|
  
=========================================================
ソースのダウンロード 
=========================================================

* Elmer-CSC のダウンロードページ、もしくは、githubのページからクローンしてくる． ::

  $ mkdir -p ~/elmer
  $ cd elmer
  $ mkdir -p build
  $ git clone https://github.com/ElmerCSC/elmerfem.git

  
|
  
=========================================================
cMakeList.txt の編集
=========================================================

* intel Compiler をインストールしても、デフォルトのコンパイラとして認識されない．
* cmakeの設定として、 以下をcMakeList.txt に追加し、使用するコンパイラを指定する． ::

    set(CMAKE_C_COMPILER "/opt/intel/oneapi/compiler/2023.0.0/linux/bin/icx")
    set(CMAKE_CXX_COMPILER "/opt/intel/oneapi/compiler/2023.0.0/linux/bin/icpx")
    set(CMAKE_Fortran_COMPILER "/opt/intel/oneapi/compiler/2023.0.0/linux/bin/intel64/ifort")
    set(MPI_C_COMPILER "/opt/intel/oneapi/compiler/2021.8.0//bin/mpiicc")
    set(MPI_Fortran_COMPILER "/opt/intel/oneapi/compiler/2021.8.0//mpiifort")

  
  
* ここで、setの第２変数のコマンドの場所は which コマンドを使って調べることができる． ::

    $ which icx
    $ which mpiifort
    etc.


  
* その他、コンパイル時に出る **warning** を無視するため、以下のオプションを付けてもよい． ::

    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wno-parentheses-equality")
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wno-deprecated-non-prototype")


.. note::

   高速化オプションを追加していないがよいのか？ 上記だと、単にコンパイラをインテルにしたのみであり、高速化オプションによるアドバンスな高速化を入れていないのでは？ MPI_Fortran_FLAGSに高速化オプション -O4 -ipo 等を入れるべきでは？


|

=========================================================
cmake ( makefileの作成 )
=========================================================

* 以下のオプションを追加して、cmakeする．

  
.. csv-table:: **cmake コマンド**
   :header: "Option", "Description"
   :widths: 50, 50
   :width:  800px

   "-DWITH_ELMERGUI:BOOL=FALSE", "elmer-GUIをインストールしない：Linux"
   "-DCMAKE_INSTALL_PREFIX=../install", "インストールするディレクトリの指定"
   "-DWITH_MPI:BOOL=TRUE", "MPIを使用する"
   "-DWITH_OpenMP:BOOL=TRUE", "OpenMPを使用する"
   "-DWITH_MKL:BOOL=TRUE", "intel MKL (Math Kernel Library)を使用する"

   
* developer 向けエラーメッセージを消すために、cmakeに -Wno-dev をつけてもよい．

  + 非本質なエラーメッセージに重要なメッセージを埋もれさせないために．

    
* cmake コマンドは結局、以下のコマンドとなる． ::

    $ cmake -DWITH_ELMERGUI:BOOL=FALSE -DWITH_MPI:BOOL=TRUE -DWITH_OpenMP:BOOL=TRUE -DWITH_MKL:BOOL=TRUE -DCMAKE_INSTALL_PREFIX=../install -Wno-dev ../elmerfem/

  
* コンパイラ・ライブラリ類の検出・テストが成功するかどうかに注目する．


|
  
=========================================================
MATCのコンパイルに失敗する
=========================================================

* sudo make install にて、インストールする．
  
  + sudo つけないと/usr/local/ に権限なくてダメと言われた．
    

---------------------------------------------------------
matc/src/main.c
---------------------------------------------------------

* OpenMPありでMATCをコンパイルしようとすると、コンパイルエラーがでる．
* エラー内容は、omp_set_num_threadsという関数が定義されていない：本来、ompインクルードファイルが指定されていない、というもの．
* エラー箇所を開いて、コンパイラが言うように omp.hを宣言する．先頭のどこでもよいので、 ::

    #include <omp.h>

    
を記載する．

|


---------------------------------------------------------
elmerfem/fem/src/Load.c
---------------------------------------------------------

* matcのvar_copy_transposeが見えない．
* matc.hを陽に include しても治らない．( Cと内部の書き方には詳しくないが、順番で解決は不可？ )
* これは、暗黙の関数宣言をC99以降はゆるさなくなったため．
* 解決策は、 (i) コンパイルの順序を変更する、 (ii) プロトタイプ宣言する、のどちらか．
* プロトタイプ宣言を入れる． 該当の関数の入出力型を調べてきて、陽にプロトタイプ宣言をする．::

    elmer/elmerfem/matc/src/variable.c
    void var_copy_transpose(char *name,double *values,int nrows,int ncols)

  
とあるので、::

  void var_copy_transpose(char *name,double *values,int nrows,int ncols);

  
とプロトタイプ宣言をする（ターミネータ";"を忘れない）．


|

---------------------------------------------------------
elmerfem/fem/src/umf4_f77wrapper.c 
---------------------------------------------------------

* umfpack_di_defaults などの関数が undecleared として検出される．（プロトタイプ宣言がない）
* 同様に、 #ifdef のマクロを使って、環境毎にどっち使うかを選択するコーディングら式部分で、implicit functionが理由のエラーが生じる． C99は、implicit を許容しない．
* elmerfem/umfpack/src/umfpack/includeにソースがある模様．
* 以下を追加する． ::

    void umfpack_di_defaults();
    void umfpack_di_symbolic();
    etc.

他、エラーとなる関数全てに対して、適用する．おそらく全関数とも引数はなさそう（ざっとみた感じ．ちゃんと確認していない）.


=========================================================
テスト実施について
=========================================================

* build において、下記を実効、テストは動いている模様． ::

    $ ctest -j8

    
* あまり、速いようにはおもえない．．．
* MPIをつけたことでサンプルの仕様が異なっていたりするか？ ( → 今まではそのようなことは感じたことない．)
* 高速化オプションを付けて再度コンパイルが必要かも．
* 92 % がテストを通過．( 失敗は circuits2D, mgdyn2D, radiation, radiator2D/3D, curveboundary, InductionHeating, ShoeboxFsiStatic, etc. )


  
=========================================================
その他
=========================================================

* 間違いで、-DCMAKE_PREFIX を -DDCMAKE_PREFIXと書いてしまっていたようで、PREFIXにインストールされなかった．
* 昔のelmerが残っていて、それを参照していたため、cannot open shared object:  xxx.so  になってしまい、パスをしっかり設定してもエラーになってしまっていた．
* デフォルトでは /usr/local/bin, /usr/local/share 等にインストールされる模様．( なので、いつも不要な "sudo" が make install 時に必要だった模様． )
* パスの設定を取り除いたら、ちゃんと動いた． ( 最後にコピーする先が異なるのみで同じ )

  
=========================================================
結論
=========================================================

* one-API × elmer は、可能．
* そんなに速くならなかった．(高速化オプションのせい？） 
* OpenMPはもともと動いていた模様 ( Elmersolver動かした際にステータスが書かれていた )．
* OMP_NUM_THREADSでスレッド数の変更が可能．
  
=========================================================
Reference
=========================================================

* なし
