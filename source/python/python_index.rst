##############################################################
pythonの備忘録
##############################################################

=========================================================
pythonとは
=========================================================

* Linux 標準装備のプログラミング言語．
* 科学技術計算分野やソフトウェア作成、WEB、各種処理、と幅広い領域で使用されている．

|
  
---------------------------------------------------------
特徴
---------------------------------------------------------

1. :red:`豊富なライブラリ`
2. :blue:`型付けなしのスクリプト言語` ( :red:`実行は遅い` )．

   - 一方、C/Fortranの型付け言語をライブラリとして簡単に呼べる．
   - :blue:`重い処理をC/Fortranで書き、制御と入出力をpythonが担えば、速さと使いやすさを両立可能．`


.. note::
   
   豊富なライブラリをもつ型付けしないスクリプト型言語であることから、 :red:`コーディングが非常に楽` ．

|
    
=========================================================
Pythonの基礎
=========================================================
  
.. toctree::
   :maxdepth: 1

   basics/pyenv__p1
   basics/tips
   basics/numpy
   basics/search__nearestPoint
   basics/timeMeasure
   basics/digit_control__01
   json_module/json_module__p1
   json_module/json_module__p2
   json_module/json_module__p3
   
   
|


=========================================================
各種ライブラリに関する備忘録
=========================================================

.. toctree::
   :maxdepth: 1

   libraries/scikit_image
   libraries/ezdxf__p1
   libraries/ezdxf__p2
   libraries/reportlab__p1
   libraries/reportlab__p2
   libraries/reportlab__p3

|

=========================================================
プロットに関して
=========================================================
  
.. toctree::
   :maxdepth: 1

   plot/gplot1d__p1
   plot/gplot1d__p2

|

=========================================================
自作関数に関する備忘録
=========================================================

.. toctree::
   :maxdepth: 1

   originals/nkEMSRoutines
   originals/translator__usingGoogleTrans/translator__usingGoogleTrans
   originals/translator__usingGemini/translator__usingGemini
   originals/gemini__summary/gemini__summary
   originals/generate__html/generate__html
   originals/make__scanParameterFile/make__scanParameterFile
   originals/precompile__parameterFile/precompile__parameterFile
   originals/command__postProcess/command__postProcess
   originals/retrieveData__afterStatement/retrieveData__afterStatement
   originals/synonymize__keywords/synonymize__keywords

|
   
=========================================================
Reference
=========================================================

* 時間計測 ( https://yumarublog.com/python/func-speed/ )
