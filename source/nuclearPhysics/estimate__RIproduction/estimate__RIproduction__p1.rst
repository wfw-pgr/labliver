##############################################################
RI製造量計算コード (1)
##############################################################

パラメータ等書式に変更があったため、2024/07/11 時点でのコードの使用方法を改めて、記載．

=========================================================
コードの使い方
=========================================================

---------------------------------------------------------
コードの準備 ( 最新は nkScripts 内に )
---------------------------------------------------------

* git clone https://github.com/wfw-pgr/nkScripts.git

|

---------------------------------------------------------
実行方法
---------------------------------------------------------

1. 入力ファイルの準備 ( dat/ri_prod.json, out/fluence_energy.dat, xs/xs__JENDL5_Au197_gn_Au196_gs.dat )

  - PHITSを実行し、  :red:`光子フラックスを評価` する
  - 例えば、"out/fluence_energy.dat", など、として保存．

2. :red:`dat/ri_prod.json を編集`
3. コードの実行 ( :red:`pyt/estimate__RIproduction.py` )
4. "dat/summary.dat" に結果が保存される．
5. 必要に応じて、製造効率 ( YieldRate [atoms/s] or efficiency [Bq(Ac)/(Bq(Ra) uA h)] ) を使用して、 estimate__time_vs_yield.py で時系列を計算する．

  
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
   :width:  800px
   
   "target.activity.Bq", "float", "ターゲット物質の放射能 (Bq) ターゲットの厚み指定を放射能(Bq) の指定する場合に使用． "
   "target.halflife", "dict", "ターゲット物質の半減期 value（値）とunit(単位)で指定．"
   "target.area.type", "string", "面積タイプ：'direct' / 'disk' (thick.type=fluenceでは表示のみ)"
   "target.thick.type", "string", "'Bq', 'direct', 'fluence-mass', 'fluence-Bq' ( Bqは面積と放射能から厚みを決定、directは直接厚みを指定する．fluence-xxx モードは、等価厚みがPHITSのタリー情報に既に含まれており、タリー内の反応数はターゲット原子の密度 (atoms/cm3) がわかればよいため、厚みを計算しなくても良い．参考・検算のために、計算する．fluence-Bq / fluence-mass は放射能、質量からそれぞれ厚みを換算する )"
   "photon.filetype", "string", "'energy-fluence'：エネルギーと光子束の２列データ / 'phits-out'：e-lower e-upper photon_flux error"
   "photon.filename", "string", "光子フラックスファイルのパス"
   "photon.bin2point.convert", "string", "PHITSのbin ( E_low - E_high photon error ) 表記から１対１の関数になおす．[ edge,  ]"
   "photon.fit.method", "string", "光子フラックスのフィッティング関数 (linear, gaussian, etc. )"
   "photon.fit.p0", "null / array of float", "光子フラックスのフィッティング初期パラメータ"
   "photon.fit.Eth", "float", "光子フラックスの閾値．"
   "photon.beam.current.sim", "float", "PHITSシミュレーションでの電流量（光子フラックスを電流量で規格化する）"
   "photon.beam.current.use", "float", "製造量予測での電流量"
   "photon.beam.duration", "float", "ビーム照射時間"
   "xsection.filename", "string", "反応断面積ファイルのパス"
   "xsection.database", "string", "データベースによって単位系がことなる．JENDL (eV-barn) or TENDL (MeV-mb)"
   "xsection.fit.method", "string", "反応断面積のフィッティング関数 (linear, gaussian, etc. )"
   "xsection.fit.p0", "null / array of float", "反応断面積のフィッティング初期パラメータ"
   "xsection.fit.Eth", "float", "反応断面積の閾値"
   "plot.norm.auto", "true/false", "エネルギー分布のグラフを自動で規格化する"
   
|
   
=========================================================
計算結果
=========================================================

* コードは次ページに．


  
---------------------------------------------------------
出力ファイル ( summary.dat )
---------------------------------------------------------

.. literalinclude:: dat/summary.dat


                    
---------------------------------------------------------
生成量に関する注釈
---------------------------------------------------------

.. csv-table::
   :header: "Name", "Notation", "Description"
   :widths: 8, 15, 45
   :width:  800px
   
   "YieldRate", ":math:`Y_0`", "単位時間あたりに核反応で生成される原子数、収率（原子数収率） (atoms/s)"
   "Y_product", ":math:`Y_A=Y_0/\lambda`", "単位時間あたりに核反応で生成される放射能、収率（放射能収率） (Bq/s)"
   "A_product", ":math:`A(t=t_e)`", "パラメータファイルで設定した照射時間で生成された放射能 (Bq)"
   "N_product", ":math:`N(t=t_e)`", "パラメータファイルで設定した照射時間で生成された原子数 (atoms)"
   "An_product_wt", ":math:`A_n^{(mg)}= \dfrac{ A(t=t_e)}{ m I_b \Delta t }`", "重量と電流、照射時間で規格化した製造量 (Bq/mg/uA/s) "
   "Yn_product_Bq", ":math:`Y_n^{(bq)}= \dfrac{ Y_A }{ A_0 I_b \Delta t }`", "放射能と電流で規格化した規格化収率 (Bq/Bq/uA/s)"

   
   
---------------------------------------------------------
飽和製造量、飽和係数に関する注釈
---------------------------------------------------------

.. csv-table::
   :header: "Name", "Notation", "Description"
   :widths: 8, 15, 45
   :width:  800px
   
   "N_saturate", ":math:`N_{sat}=Y_0/\lambda=Y_A`", "生成される最大飽和原子数 (atoms)"
   "A_saturate", ":math:`A_{sat}=N_{sat}/\lambda`", "生成される最大飽和放射能 (Bq)"
   "t_max", ":math:`T_{max}`", "崩壊生成核種の製造量が最大となる時刻 (s)"
   "ratio", ":math:`R=A_B/A_A`", "崩壊生成核種とビーム製造核種の放射能の比 (a.u.)"
   "lambda_t", ":math:`\lambda t`", "線形でビーム製造した際の値 (a.u.)"
   "saturation", ":math:`1-exp(-\lambda t)`", "飽和係数．(a.u.)"
   "F_saturate", ":math:`F_{sat}=\dfrac{1-exp(-\lambda t)}{\lambda t}`", "飽和係数の線形からのずれの度合い (a.u.)"
