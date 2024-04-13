##############################################################
Elmer (FEM)の備忘録
##############################################################

=========================================================
有限要素解析のフリーウェア
=========================================================

* Elmer は、CSCが開発しているOSS有限要素解析ソフトウェア．
* 高機能、拡張性（自由度）が高い．
* GUI機能等もついているが、GUI機能のコンパイルには環境(Qt4)などのグラフィックライブラリの構築が必要であり、クロスプラットフォームとして動作するわけではなく、若干親切ではない．(non-GUIはクロスプラットフォーム)

=========================================================
ソフトウェア構成
=========================================================

* Elmerは元々は力学計算用に作成された有限要素解析ソフトウェア．
* 電磁気・熱・流体等が追加され、現在では総合的な有限要素解析ソフトとして使用できる．
* 流体はOpenFOAMと連成が可能．（元来、OpenFOAMに頼る必要はないため、ソルバや乱流モデル等の機能面で下位互換である可能性あり．）


=========================================================
本解説の構成
=========================================================

以下，有限要素解析ソフトウェア *Elmer* について以下の構成で解説する．


---------------------------------------------------------
基本的な用法
---------------------------------------------------------

.. toctree::
   :maxdepth: 1

   usage/howtoinstall
   usage/install__elmer_with_intelCompiler
   usage/sifGrammer
   usage/notation_MATC
   usage/section__simulation
   usage/section__solver
   usage/section__boundaryCondition

   
---------------------------------------------------------
力学
---------------------------------------------------------

.. toctree::
   :maxdepth: 1
              
   dynamics/stressAnalysis
   dynamics/elasticAnalysis

   
---------------------------------------------------------
電磁気学
---------------------------------------------------------

.. toctree::
   :maxdepth: 1
              
   electromagnetism/line_current
   electromagnetism/circular_coil
   electromagnetism/ring_and_core
   electromagnetism/cshape_magnet
   electromagnetism/hshape_magnet
   electromagnetism/vector_helmholtz.rst
   electromagnetism/waveguide

   
---------------------------------------------------------
熱計算
---------------------------------------------------------

.. toctree::
   :maxdepth: 1

   heat/heatConduction__in_a_bar_XYZ3D
   heat/heatConduction__box_in_water_XYZ3D
   

              
---------------------------------------------------------
流体力学
---------------------------------------------------------

.. toctree::
   :maxdepth: 1

   fluid/fluid__introduction
   fluid/fluid__modelSelection
   fluid/fluid__boundaryCondition
   fluid/flow__around_cylinder_NS_XY2D
   fluid/flow__in_a_curved_pipe_XYZ3D
   fluid/heatConduction__in_a_curved_pipe_XYZ3D
   fluid/k_epsilon_model
   fluid/flow__backStep_keSolver_XY2D
   fluid/thermalFluid__backStep_XY2D
   fluid/heatTransfer__box_in_water_XY2D


=========================================================
References
=========================================================

* Elmer(Non-GUI)の基本事項概説 :: ElmerSolverManual.pdf ( http://www.nic.funet.fi/index/elmer/doc/ElmerSolverManual.pdf )
* Elmer(Non-GUI)のモデルマニュアル :: ElmerModelManual.pdf ( http://www.nic.funet.fi/index/elmer/doc/ElmerModelsManual.pdf )
* Elmer Documentation のページ :: ( https://www.csc.fi/web/elmer/documentation )
