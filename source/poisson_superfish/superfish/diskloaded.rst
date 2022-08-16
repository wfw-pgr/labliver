=========================================================
ディスク装荷型空洞共振器設計コードの使い方
=========================================================


parameter.confの設定
=========================================================

.. literalinclude:: code/parameter.conf
   :caption: parameter.confの設定例


実行例
=========================================================

.. code-block::

   $ python pyt/make__af.py
   $ python pyt/make__in7.py
   $ open run/diskloaded.af
   $ open run/DISKLOAEDE.T35
   $ open run/diskloaded.in7
   $ python pyt/convert__sf7.py
   $ python pyt/display__sf7.py


境界条件の変更
=========================================================

* 進行波管における境界条件の設定は次．

  + 開放端境界条件 ( [up,low,right,left] = [1,0,1,1] )
  + 固定端境界条件 ( [up,low,right,left] = [1,0,0,0] )
