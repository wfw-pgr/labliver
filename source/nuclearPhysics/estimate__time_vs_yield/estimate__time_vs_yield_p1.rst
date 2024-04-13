##############################################################
照射製造時の製造量の時間変化について
##############################################################

=========================================================
基礎方程式
=========================================================

---------------------------------------------------------
ビームOFF時
---------------------------------------------------------

減衰するのみのため、下記、放射平衡の式と同じ．

.. math::
   
   \dfrac{ d[A] }{ dt } &= - \lambda_1 [A] \\
   \dfrac{ d[B] }{ dt } &= + \lambda_1 [A] - \lambda_2 [B]

   
---------------------------------------------------------
ビームON時
---------------------------------------------------------

ビームによる核種製造 ( 製造効率 Y [atoms/s] )と減衰の両項を考慮．崩壊生成物の表式は同じ．

.. math::
   
   \dfrac{ d[A] }{ dt } &= - \lambda_1 [A] + Y \\
   \dfrac{ d[B] }{ dt } &= + \lambda_1 [A] - \lambda_2 [B]



---------------------------------------------------------
初期条件
---------------------------------------------------------

* 初期条件として、 :math:`t=t_0` の際に、 :math:`[A]=[A]_0` , :math:`[B]=[B]_0` であるとして、その後の時間発展を計算すれば良い．
* これを接続していけば、任意の時刻の製造量を計算できる．


| 

=========================================================
[A] に関する一般解
=========================================================

---------------------------------------------------------
ビームOFF時
---------------------------------------------------------

.. math::
   
   \dfrac{ d[A] }{[A] } &= - \lambda_1 dt \\
   [A] &= C_0 e^{ - \lambda_1 t }

初期条件 :math:`t=t_0` 、 :math:`[A]=[A]_0` を用いて、

.. math::

   [A] = [A]_{0} e^{ - \lambda_1 (t-t_0) }
   

---------------------------------------------------------
ビームON時
---------------------------------------------------------

斉次解

.. math::
   
   [A] = C(t) e^{ - \lambda_1 t }

より、変数 C(t) を求めると、

.. math::

   \dot{ C }(t) e^{ -\lambda_1 t } - \lambda_1 C(t) e^{ - \lambda_1 t} + \lambda_1 C(t) e^{ - \lambda_1 t} &= Y \\
   \dot{ C }(t) e^{ -\lambda_1 t } &= Y
   
.. math::
   
   C(t) &= \dfrac{Y}{\lambda_1} e^{\lambda_1 t} + C_0

一般解は、

.. math::

   [A] = \dfrac{Y}{\lambda_1} + C_0 e^{- \lambda_1 t}


初期条件 :math:`t=t_0` 、 :math:`[A]=[A]_0` を用いて、積分定数を決定すると、

.. math::

   [A] = [A]_0 e^{ -\lambda_1 (t-t_0) } + \dfrac{Y}{\lambda_1} [ 1 - e^{ -\lambda_1 (t-t_0) } ]
   

( もちろん、Y=0 でビームOFF時と同値となる． )


=========================================================
[B] に関する一般解
=========================================================

---------------------------------------------------------
ビームOFF時
---------------------------------------------------------

解くべき方程式は、

.. math::

   [A] &= [A]_{0} e^{ - \lambda_1 (t-t_0) } \\
   \dfrac{ d[B] }{ dt } &= + \lambda_1 [A] - \lambda_2 [B]


斉次解

.. math::
   
   [B] = D(t) e^{ - \lambda_2 t }

より、

.. math::

   \dot{D} (t) e^{ - \lambda_2 t } &= \lambda_1 [A]_0 e^{ -\lambda_1 (t-t_0) } \\
   D(t) &= D_0 + \dfrac{ \lambda_1 [A]_0 }{ \lambda_2 - \lambda_1 } e^{ \lambda_1 t_0 } e^{ ( \lambda_2 - \lambda_1 ) t }

   
一般解は、

.. math::

   [B] = D_0 e^{-\lambda_2 t} + \dfrac{ \lambda_1 [A]_0 }{ \lambda_2 - \lambda_1 } e^{ - \lambda_1 (t-t_0) }

初期条件、 :math:`t=t_0` で :math:`[A]=[A]_0` , :math:`[B]=[B]_0` を用いて、

.. math::

   [B]_0 &= D_0 e^{ -\lambda_2 t_0 } + \dfrac{ \lambda_1 [A]_0 }{ \lambda_2 - \lambda_1 } \\
   D_0 &= \left[ [B]_0 - \dfrac{ \lambda_1 [A]_0 }{ \lambda_2 - \lambda_1 } \right] e^{\lambda_2 t_0}

これより、解は

.. math::
   
   [B] = \left[ [B]_0 - \dfrac{ \lambda_1 [A]_0 }{ \lambda_2 - \lambda_1 } \right] e^{ -\lambda_2 (t-t_0) } + \dfrac{ \lambda_1 [A]_0 }{ \lambda_2 - \lambda_1 } e^{ -\lambda_1(t-t_0) }


整理して、

.. math::

   [B] = [B]_0 e^{ -\lambda_2 (t-t_0) } + \dfrac{ \lambda_1 [A]_0 }{ \lambda_2 - \lambda_1 } \left[ e^{ -\lambda_1(t-t_0) } - e^{ -\lambda_2(t-t_0) } \right] 

第一項は、:red:`初期の放射能の時間減衰` 、第二項は、 :red:`連鎖崩壊の式` となっている．

   
---------------------------------------------------------
ビームON時
---------------------------------------------------------

解くべき方程式は、

.. math::

   [A] &= [A]_0 e^{ -\lambda_1 (t-t_0) } + \dfrac{Y}{\lambda_1} [ 1-e^{ -\lambda_1 (t-t_0) } ]\\
   \dfrac{ d[B] }{ dt } &= + \lambda_1 [A] - \lambda_2 [B]

   
斉次解

.. math::
   
   [B] = D(t) e^{ - \lambda_2 t }

より、

.. math::

   \dot{D} (t) e^{ - \lambda_2 t } &= \lambda_1 [A]_0 e^{ -\lambda_1 (t-t_0) } + Y[ 1-e^{-\lambda_1(t-t_0)} ] \\
   \dot{D} (t)  &= \lambda_1 [A]_0 e^{ \lambda_1 t_0 } e^{ (\lambda_2-\lambda_1) t } + Y e^{\lambda_2 t } - Y e^{ \lambda_1 t_0 } e^{ (\lambda_2 - \lambda_1) t } \\
   D(t) &= D_0 + \dfrac{ \lambda_1 [A]_0 }{ \lambda_2 - \lambda_1 } e^{ \lambda_1 t_0 } e^{ ( \lambda_2 - \lambda_1 ) t } + \dfrac{ Y }{ \lambda_2 } e^{\lambda_2 t } - \dfrac{ Y }{ \lambda_2 - \lambda_1 } e^{ \lambda_1 t_0 } e^{ (\lambda_2 - \lambda_1) t }

   
一般解は、

.. math::

   [B] &= D_0 e^{ -\lambda_2 t } + \dfrac{ \lambda_1 [A]_0 }{ \lambda_2 - \lambda_1 } e^{ - \lambda_1 ( t - t_0 ) } + \dfrac{ Y }{ \lambda_2 } - \dfrac{ Y }{ \lambda_2 - \lambda_1 } e^{ - \lambda_1 ( t - t_0 ) }

初期条件、 :math:`t=t_0` で :math:`[A]=[A]_0` , :math:`[B]=[B]_0` を用いて、

.. math::

   [B]_0 &= D_0 e^{ -\lambda_2 t_0 } + \dfrac{ \lambda_1 [A]_0 }{ \lambda_2 - \lambda_1 } + \dfrac{ Y }{ \lambda_2 } - \dfrac{ Y }{ \lambda_2 - \lambda_1 } \\
   D_0 &= \left[ [B]_0 - \dfrac{ \lambda_1 [A]_0 }{ \lambda_2 - \lambda_1 } - \dfrac{ Y }{ \lambda_2 } + \dfrac{ Y }{ \lambda_2 - \lambda_1 } \right] e^{ \lambda_2 t_0 }

これより、解は

.. math::
   
   [B] = \left[ [B]_0 - \dfrac{ \lambda_1 [A]_0 }{ \lambda_2 - \lambda_1 } - \dfrac{ Y }{ \lambda_2 } + \dfrac{ Y }{ \lambda_2 - \lambda_1 } \right] e^{ - \lambda_2 (t-t_0) } + \dfrac{ \lambda_1 [A]_0 }{ \lambda_2 - \lambda_1 } e^{ - \lambda_1 ( t-t_0 ) } + \dfrac{ Y }{ \lambda_2 } - \dfrac{ Y }{ \lambda_2 - \lambda_1 } e^{ - \lambda_1 ( t-t_0 ) } 

整理して、

.. math::

   [B] = [B]_0 e^{ - \lambda_2 (t-t_0) }
   + \dfrac{ \lambda_1 [A]_0 - Y }{ \lambda_2 - \lambda_1 } \left[ e^{ - \lambda_1 ( t-t_0 ) } - e^{ - \lambda_2 (t-t_0) } \right]
   + \dfrac{ Y }{ \lambda_2 } ( 1 - e^{ - \lambda_2 ( t-t_0 ) } )


第一項は、 :red:`初期の放射能の時間減衰の項` 、
第二項は、 :red:`連鎖崩壊の項 ( 生成分の変形あり )` 、
第三項は、 :red:`核種生成の項` となっている．
