##############################################################
放射能から試料厚みへの換算
##############################################################

=========================================================
前提
=========================================================

* PHITSシミュレーション等、進める際に、放射能から定量したRIを有限体積のモデルに置き換える必要がある．
* 体積中にどの程度の原子数が含まれるか、または、放射能からどの程度の体積かを同定する．


=========================================================
換算
=========================================================

---------------------------------------------------------
記号と単位
---------------------------------------------------------

* :red:`長さの単位は "cm" を使用することに注意` (密度やモル質量がcgsで記載されることが多いため．)

.. csv-table:: 
   :header: "記号", "説明", "単位", "RaCl2の参考値"
   :widths: 10, 20, 10, 10
   :width:  800px
   
   ":math:`N_A`", "アボガドロ数", "atoms/mol", "6.02*10^23"
   ":math:`\rho`", "質量密度", "g/cm3", "4.9"
   "M", "モル質量（分子量/原子量）", "g/mol", "297"
   "n", "原子数密度", "atoms/cm3", "1.0*10^22"
   "N", "原子数", "atoms", ""
   "V", "体積", "cm3", ""
   "S", "体積モデルの面積 (厚み方向には一様を仮定)", "cm2", ""
   "t", "体積モデルの厚み", "cm", ""
   "D", "例として円筒形をモデルとする場合の直径", "cm", ""
   ":math:`\lambda`", "崩壊定数", "s^-1", ""
   "T", "半減期", "s", "1622*365*24*3600=5.05*10^10"
   "Q", "放射能", "Bq", ""
   

---------------------------------------------------------
原子数密度 n
---------------------------------------------------------

モル質量と質量密度より、１モルあたりの体積が :math:`M/\rho` として得られ、体積あたりの原子数密度 n を以下で求められる．

.. math::

   n &= \dfrac{ N_A }{ M/\rho } \\
   &= \dfrac{ N_A \rho }{ M }


---------------------------------------------------------
崩壊定数 λ
---------------------------------------------------------

.. math::

   \lambda = \dfrac{ln2}{T}


---------------------------------------------------------
体積モデル
---------------------------------------------------------

面積S、厚みtの単純なモデルを仮定して、

.. math::

   V= S \times t

例えば、直径Dの円筒形の場合、

.. math::

   V= \dfrac{\pi}{4} D^2 t


---------------------------------------------------------
原子数 N
---------------------------------------------------------

.. math::

   N &= nV \\
   &= \dfrac{ N_A \rho }{ M } S \times t
   
   
---------------------------------------------------------
放射能
---------------------------------------------------------


.. math::
   
   Q &= \lambda N \\
   &= \dfrac{ln2}{T} \dfrac{ N_A \rho }{ M } S \times t


---------------------------------------------------------
厚み
---------------------------------------------------------

結局、上記式より、与えられた放射能Q, 面積S, 厚みtの物質の厚みは、

.. math::

   t = \dfrac{ Q T M }{ ln2 N_A \rho S }


=========================================================
計算例 
=========================================================

---------------------------------------------------------
Ra-226 Cl2 ( 100 kBq ) の場合
---------------------------------------------------------


直径 3 (mm) = 0.3 (cm) の円筒形を考えれば、( S=π/4 D^2=7.07*10^-2 )

.. math::

   t &= \dfrac{ ( 100 \times 10^3 ) \times ( 5.05 \times 10^{10}) \times 297.0 } { ln2 \times ( 6.02 \times 10^{23} ) \times 4.9 \times ( 7.07 \times 10^{-2} ) } \\
   &= 1.037 \times 10^{-5} (cm) \\
   &= 1.037 \times 10^{-4} (mm) \\
   &= 0.1 (\mu m)

100kBqのRaは 0.1 um 程度で、極めて薄い．



---------------------------------------------------------
コード
---------------------------------------------------------

.. literalinclude:: pyt/activity_to_thickness.py
   		    :language: python

