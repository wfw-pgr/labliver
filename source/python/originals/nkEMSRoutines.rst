##############################################################
nkEMSRoutines
##############################################################

=========================================================
merge__bintegField.py
=========================================================

---------------------------------------------------------
引数
---------------------------------------------------------

.. csv-table:: **merge__bintegField.py**
   :header: "argument", "type", "default", "Comment"
   :widths: 10, 10, 10, 20
   :width:  800px
   
   "inpFiles", "list of strings", "", ""
   "outFile", "strings", "ems_merged", ""
   "vtsFile", "strings", "None", "ファイル名を指定したら保存"
   "structured", "logical", "True", "structured gridにするか否か"
   "x1MinMaxNum", "list of floats", "", "structured grid の最小値・最大値、及び、分割数"
   "x2MinMaxNum", "list of floats", "", ""
   "x3MinMaxNum", "list of floats", "", ""
   "digit", "integer", "5", "xyz軸の値を判別する際の桁数指定"


---------------------------------------------------------
コマンドライン実行
---------------------------------------------------------

pythonからの実行コマンド例 ::

  $ python merge__bintegField.py --inpFiles ems_pst_*.out --outFile bfield.dat --x1MinMaxNum -1.2 +1.2 101 --x2MinMaxNum -1.2 +1.2 101 --x3MinMaxNum -0.010 +0.010 11 --vtsFile bfield.vts


または、パスを通しておいて、::

  $ merge__bintegField.py --inpFiles ems_pst_*.out --outFile bfield.dat --x1MinMaxNum -1.2 +1.2 101 --x2MinMaxNum -1.2 +1.2 101 --x3MinMaxNum -0.010 +0.010 11 --vtsFile bfield.vts

  
