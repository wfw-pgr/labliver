##############################################################
RI製造量計算コードの使い方
##############################################################

=========================================================
コードの使い方
=========================================================

---------------------------------------------------------
コードの準備
---------------------------------------------------------

* git clone https://github.com/wfw-pgr/RIproduction.git

|

---------------------------------------------------------
実行方法
---------------------------------------------------------

* 入力ファイルの準備 ( dat/parameters.json, dat/fluence_energy_phitsin.dat )

  - PHITSを実行し、  :red:`光子フラックスを評価` する
  - 例えば、"dat/fluence_energy.dat" として保存．
  - :red:`dat/parameters.json を編集`
    
* コードの実行 ( :red:`pyt/estimate__RIproduction.py` )
* "dat/results.dat" に結果が保存される．
* 必要に応じて、製造効率 ( YieldRate [atoms/s] or efficiency [Bq(Ac)/(Bq(Ra) uA h)] ) を使用して、 estimate__time_vs_yield.py で時系列を計算する．

  
::

   $ cd estimate__RIproduction/
   $ python pyt/estimate__RIproduction.py

   
|

---------------------------------------------------------
パラメータの設定
---------------------------------------------------------

.. csv-table::
   :header: "Name", "Type", "Description"
   :widths: 10, 10, 40
   :width:  700px
   
   "target.activity.Bq", "float", "ターゲット物質の放射能 (Bq)"
   "target.halflife", "dict", "ターゲット物質の半減期 value（値）とunit(単位)で指定．"
   "target.area.type", "string", "面積タイプ：'direct' / 'cylinder'"
   "target.thick.type", "string", "'Bq', 'direct', 'fluence' ( Bqは面積と放射能から厚みを決定、directは直接厚みを指定する、fluenceは厚みはPHITS側の光子フラックスから厚みを換算する． )"
   "photon.filetype", "string", "'energy-fluence'：エネルギーと光子束の２列データ / 'phits-out'：e-lower e-upper photon_flux error"
   "photon.filename", "string", "光子フラックスファイルのパス"
   "photon.fit.method", "string", "光子フラックスのフィッティング関数 (linear, gaussian, etc. )"
   "photon.fit.p0", "null / array of float", "光子フラックスのフィッティング初期パラメータ"
   "photon.beam.current.sim", "float", "PHITSシミュレーションでの電流量（光子フラックスを電流量で規格化する）"
   "photon.beam.current.use", "float", "製造量予測での電流量"
   "photon.beam.duration", "float", "ビーム照射時間"
   "xsection.filename", "string", "反応断面積ファイルのパス"
   "xsection.fit.method", "string", "反応断面積のフィッティング関数 (linear, gaussian, etc. )"
   "xsection.fit.p0", "null / array of float", "反応断面積のフィッティング初期パラメータ"
   "plot.norm.auto", "true/false", "エネルギー分布のグラフを自動で規格化する"
   
|
   
=========================================================
コードの実装
=========================================================

---------------------------------------------------------
python コード ( estimate__RIproduction.py )
---------------------------------------------------------

.. literalinclude:: pyt/estimate__RIproduction.py
   		    :language: python

                               
---------------------------------------------------------
パラメータファイル ( parameters.json )
---------------------------------------------------------

.. literalinclude:: dat/parameters.json


---------------------------------------------------------
PHITS計算した光子束分布 ( fluence_energy_phitsin.dat )
---------------------------------------------------------

.. literalinclude:: dat/fluence_energy_phitsin.dat


---------------------------------------------------------
出力ファイル ( results.dat )
---------------------------------------------------------

.. literalinclude:: dat/results.dat
