=========================================================
python コード Tips
=========================================================


numpyの座標毎データ整列 ( np.lexsort )
=========================================================

e.g.) Data :: [nData,3] ( point 形式 )

.. code-block:: python

   index          = np.lexsort( ( Data[:,xp_], Data[:,yp_], Data[:,zp_]) )
   Data           = Data[index]

   

色付きテキストの出力
=========================================================

print文内での色の変更は、ターミナルと同様の修飾句を前後につける．

e.g.) 

.. code-block:: python

   print( "\033[31m" + "This is red colored text" + "\033[0m" )
   

   
もしくは、nkUtilities.cprintを使う


.. code-block:: python

   import nkUtilities.cprint as cpr
   cpr.cprint( "This is red colored text", color="red"   )
   cpr.cprint( "This is red colored text", color="green" )



カラーコードの一覧表はcprintコード内の辞書を参照のこと．

.. literalinclude:: ../code/cprint.py
   		    :caption:  cprint.py
   		    :language: python


   
