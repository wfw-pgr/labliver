=========================================================
python コード Tips
=========================================================


numpyの座標毎データ整列 ( np.lexsort )
=========================================================

e.g.) Data :: [nData,3] ( point 形式 )

.. code-block:: python

   index          = np.lexsort( ( Data[:,xp_], Data[:,yp_], Data[:,zp_]) )
   Data           = Data[index]

   
