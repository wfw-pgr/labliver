=========================================================
fortranにおけるライブラリ指定の仕方
=========================================================

自作ライブラリの作成
=========================================================

まずは普通にプログラムを作成する．それをコンパイル．

::

   gfortran -c test_source.f90

ar(archive)コマンドを使ってライブラリ化する．

::

  ar cr testlib.a *.o

ちなみにcは作成(create)で,rは置換(Replacement)で古いファイルを置換する．
ライブラリ使用時は直接指定

::

  gfortran -o trylib.f90  ./testlib/testlib.a

もしくは-l及び-Lオプションを使う．-lオプションを使うにはlib~~~.aという名前でなければならないから，

::

  mv testlib.a libtest.a  

を行ってから，

::

  gfortran -o trylib.f90 -Ltestlib -ltest

とすれば良い．


Links : https://docs.oracle.com/cd/E19205-01/820-1203/aeudl/index.html




python ライブラリでの blas 、他ライブラリの 使用
=========================================================

* python ライブラリで blasをリンクしておかないと、blasが使えない．
* gfortran などで、blasを陽に指定する際は、以下のような **makefile** を書くと良い.

.. literalinclude:: ../code/makefile_python_fortran_sample
   :caption: python-fortran library example of makefile
   :language: make
   :linenos:
   :emphasize-lines: 12,23

* 基本的には、 libopenblas.a etc. をフルパスで与えれば良い．
