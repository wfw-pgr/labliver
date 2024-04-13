##############################################################
numpy について
##############################################################

=========================================================
loadtxt / genfromtext 
=========================================================

---------------------------------------------------------
入力形式について
---------------------------------------------------------

* 公式．

::

   Parameters: fname: file, str, pathlib.Path, list of str, generator
   File, filename, list, or generator to read. If the filename extension is .gz or .bz2, the file is first decompressed. Note that generators must return bytes or strings. The strings in a list or produced by a generator are treated as lines.

* 入力としてとれるのは、

  + ファイル名
  + ファイルディスクリプタ ( open( xxx.dat, "r" ) の返り値のやつ )
  + pathlib.path ( ファイルパス )
  + string のリスト ( f.readlines() の返り値など )
  + generator

* つまり、自分で編集した文字列等を loadtxt / genfromtxtから、数字を読むことができる．
* 好きな行を 正規表現などで抜き出して、そこから、ある行まで書くなども可能である


.. code-block:: python
   
   inpFile = "aaa"
   expr1   = "x-variable\s*y-variable"
   expr2   = "end"
   with open( inpFile, "r" ) as f:
     lines = f.readlines()
   for il,line in enumerate( lines ):
     match1 = re.match( expr1, line )
     if ( match1 ):
       iS = il + 1
       break
   for il,line in enumerate( lines[iS] ):
     match2 = re.match( expr2, line )
     if ( match2 ):
       iE = iS + il
       break
   Data = np.loadtxt( lines[iS:iL+1] )



   
