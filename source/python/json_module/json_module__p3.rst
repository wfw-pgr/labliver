##############################################################
json モジュール (3) ( json5dumper.py )
##############################################################


=========================================================
自作 json5 用 ファイルダンプクラス ( json5dumper.py )
=========================================================

* json5の形式で、データを保存する．

  + （容量の効率よりも、可読性を重視したい．）

* numpy ndarray をサポートしていないため、データ形式を問わずにdumpするのは難しい．

  + ndarray は np.save を用いてバイナリ保存．ファイルパスのみ jsonファイル内に記載．
  + 他は、json形式として、可読性を保つ．

    
---------------------------------------------------------
使い方
---------------------------------------------------------

* クラス宣言

.. code-block:: python

   import nkUtilities.json5dumper as j5d
   dumper = j5d.json5dumper()
   dumper.dump( outFile=outFile, Data=Data )
   
   Data = dumper.recall( inpFile=outFile )


   
* dumpコマンドを関数ライクに直接呼ぶ．

.. code-block:: python
                
   import nkUtilities.json5dumper as j5d
   dumper = j5d.json5dumper().dump( outFile=outFile, Data=Data )


* recall コマンドを関数ライクに直接呼ぶ．

.. code-block:: python

   import nkUtilities.json5dumper as j5d
   Data = j5d.json5dumper().recall( inpFile=inpFile )


---------------------------------------------------------
実行結果 (dump)
---------------------------------------------------------

.. literalinclude:: dat/output.json


---------------------------------------------------------
実行結果 (recall)
---------------------------------------------------------

.. literalinclude:: dat/recalled.stdout
