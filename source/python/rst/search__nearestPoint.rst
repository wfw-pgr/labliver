##############################################################
最近傍点の探索 ( Blute-Force Attack )
##############################################################

=========================================================
Blute-Force Attack による最近傍点の探索
=========================================================

* 最近傍点を探す方法は色々とある．

  + k近傍法
  + kd-Tree
  + etc.

* 最も **Primitive** な手法が、総当たりで座標点間の距離を計算し、最小値を捜索するという手法

  + 次元数が増えるほど、データ点数が増えるほど、計算時間が増える．
  + 逆に言うと小さい組み合わせ数なら、速いし問題ない．

    
=========================================================
Blute-Force Attackの最近傍点探索のコード
=========================================================

* コードは以下である．

  .. literalinclude:: ../code/search__nearestPoint.py
     		      :caption:  search__nearestPoint.py
     		      :language: python


=========================================================
サンプル実行結果
=========================================================

* 実行結果は以下．

  + foreach = 2 として設定、vec2(青) の全てについて最近傍のvec1(赤)を探索し、グレーの線分で結んでいる．

  .. image:: ../image/search__nearestPoint_test.png
             :width:  600px
             :align:  center
