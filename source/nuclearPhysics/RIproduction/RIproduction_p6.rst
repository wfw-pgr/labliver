##############################################################
RI製造量計算 (6)
##############################################################

=========================================================
厚み評価 : fluence mode
=========================================================

* 厚み評価を均一厚みではなく、PHITSから評価する．
* parameters.jsonc 内のパラメータ： target.thick.type ごとの動作．

  + "bq" ： 原料元素の放射能を入れて、原子数密度から体積を計算する．体積から指定した断面積における厚みを計算する．
  + "direct" ： 直接厚みを指定する．製造量はこの値によって増減する．
  + "fluence" ： (New!) PHITSのfluenceに体積をかけることによって、光子フラックスに透過距離がかかった値が計算できる photonFluxとして与える値に、この透過厚みが反映されているとして、厚みを別に与えることはしない（均等厚みの仮定をおいていないので、これが推奨か）．


---------------------------------------------------------
parameter
---------------------------------------------------------

::

   "target.thick.type":"fluence",       // "Bq", "direct", "fluence"



=========================================================
PHITS側の設定
=========================================================

* fluenceを評価する．（厚みがはっきりしている場合のみ、T-Crossでもよい）
* [T-Track] タリーを使用する．例えば

.. literalinclude:: dat/tally__fluence_phits.inp


* vol = 1.0 を指定すると、体積V で除算されない ( 後に体積がけする必要がないので推奨． )
* area = 1.0 で T-cross セクションを使用するのも同様．入射粒子数をカウントする．（単位面積あたりとしないカウントが可能．）

  + 検出する値は、粒子の軌跡をすべて足し合わせた値に相当する．( unit = m )
  + 体積を指定した際は、粒子軌跡長の総和の体積平均値  :math:`n_{fluence}`
  + 体積を 1 とした際は、粒子軌跡長の総和 :math:`N_{fluence}` 
  + この値は、crossで検出する値 :math:`N_{cross}` （ある領域に流入する粒子数）に、実行的な厚み( :math:`L_{eff}` ) をかけた値とほぼ一致することを確認している．

  .. math::

     N_{cross} [counts] L_{eff} [m] = n_{fluence} [m/m^3] * V [m^3] = N_{fluence} [m]
    
* 実行長さを含めていることになる．（円盤を斜めにおいている場合、実質的な厚み 1/cos が増加する．）
* 変な形状の場合は、実質的な厚みを解析的に計算できないため、こちらが一般性をもつ解法になると考えている．
