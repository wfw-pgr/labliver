##############################################################
tRK4の使い方 ( パラメータ設定・前処理篇 )
##############################################################


tRK4のファイル・ディレクトリ構成
=========================================================

* src    : Fortran ソースコード群
* pyt    : python プリポストコード群
* dat    : データ類, config類
* png    : 出力画像類
* bpm    : ビームポジションモニタ用出力ファイル
* prb    : 粒子プローブ用出力ファイル
* job    : 保存用 job ディレクトリ
* dev    : 開発中のコード、不要コード仮置き場
* README : メモ
* go.py  : 実行スクリプト


実行例
=========================================================

コンフィグ設定 ( parameter.conf )
---------------------------------------------------------

* parameter.conf を書き換える．
* parameter.confの例は以下の通り．

.. literalinclude:: ../code/parameter.conf
   :caption: コンフィグファイルの例

  
  
電場・磁場の設定
---------------------------------------------------------

* サンプル磁場・電場の生成
  
.. code-block:: shell

   $ python pyt/generate__bFieldSample.py
   $ python pyt/generate__eFieldSample.py


   
電場・磁場ファイルリストの作成
---------------------------------------------------------

* 全ての磁場・電場リスト、及びその使い方をリスト表記する．
* リストファイルのサンプルは以下.

.. literalinclude:: ../code/fieldlist.conf
   :caption: 磁場・電場ファイルリストの作成

* 各項目の説明
  
  + FileName - ファイル名 ( e.g. dat/efield_buncher1_opened.dat )
  + EorB - 電場か磁場か ( E or B )
  + Amplitude - 場の振幅 スケール倍する ( e.g. 3.1 (スケール倍), 1.0 (なし)  )
  + Frequency - 変調の周波数 modulation_typeで変調はスイッチ ( e.g. 2.856e9 Hz )
  + Phase - 変調の位相進み ( e.g. 0.0 or 90.0, etc. )
  + xyzshift - 座標のシフト xyz座標の3つの実数で指定 ( e.g. 0 1 0 )
  + modulation_type - 変調のタイプ. ( cos, sin, off から選ぶ )
  + boundary_xyz - 境界条件 axisymm, Neumann, Dirichletから選ぶ ( axisymm, Neumann, Neumann )
  + nRepeat_xyz - 場の反復回数 RFキャビティなど周期構造で使用 xyzの３座標分を記載 ( e.g. 1 1 21 )
  

    
初期粒子情報の準備
---------------------------------------------------------

* dat/particle.confで生成する初期粒子のパラメータを書き換える
* 初期粒子を生成 ( dat/particles.dat ) する．
  
.. code-block:: shell

   $ python pyt/generate__particleSample.py

* dat/particle.confの例は以下．

.. literalinclude:: ../code/particle.conf
   :caption: 初期粒子のパラメータ情報



スクリプトのまとめて実行
---------------------------------------------------------

* 上記の操作をまとめてスクリプト実行
* パラメータファイルを書き換える

  + dat/parameter.conf
  + dat/fieldlist.conf
  + dat/particle.conf


.. code-block:: shell

   $ python go.py
   $ ./main

