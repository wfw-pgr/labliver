=========================================================
Fortranの文法
=========================================================

namelistについて
=========================================================

namelist の読み込み方
----------------------------------------------------

.. code-block:: fortran

   namelist /parameters/ file1, var1, var2, flag1, ....

   open (lun,file=trim("namelist.lst"),status="old",form="formatted")
   read (lun,nml=parameters)
   close(lun)

   
                
namelist の書き方
----------------------------------------------------

.. code-block::
   
   &parameters
   file1 = "dat/some_file.dat"
   var1  = 0.2
   flag1 = True
   etc.
   /

namelist の注意点
----------------------------------------------------

* namelist 名 ( /xxx/ と &xxx の部分 :: parameters(上) ) )は任意、わかりやすさでグルーピングすべし．
* read(nml=parameters)
* character型は""で囲う方が無難. じゃないと、ドット(.)やスラッシュ(/)で終わってしまう．
* 記法(エラー出力)は残念ながらコンパイラ依存の部分あり．
* 行末カンマが必須な処理系もあるらしい．
* & と namelist名の間に空白を許さない系もあるらしい（gfortran?）．

  
