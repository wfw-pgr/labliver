=========================================================
ハミルトニアンによる運動の記述
=========================================================

正準方程式 ( Hamilton方程式：Hamilton's Equations )
====================================================

**解析力学の最重要式** . 運動方程式は，一般化座標 :math:`q` と共役な運動量を用いて，次のように表せる．

.. math::
   \dot{q} = + \dfrac{ \partial H }{ \partial p } \\
   \dot{p} = - \dfrac{ \partial H }{ \partial q }

多次元の場合，

.. math::
   \dot{q_k} = + \dfrac{ \partial H }{ \partial p_k } \\
   \dot{p_k} = - \dfrac{ \partial H }{ \partial q_k }
   
一般化座標と共役な運動量は  :blue:`対称的な(符号が異なるだけ)式` で表せる．


ハミルトン方程式の導出
======================================

ハミルトン方程式は，ラグランジュ方程式への **ルジャンドル変換の適用** によって得られる．ラグランジュ形式の運動方程式は，

.. math::
   p_i         &= \dfrac{ \partial L }{ \partial \dot{q_i} } (q_1,\cdots,q_N, \dot{q_1},\cdots,\dot{q_N} ) \\
   \dot{ p_i } &= \dfrac{ \partial L }{ \partial      q_i  } (q_1,\cdots,q_N, \dot{q_1},\cdots,\dot{q_N} )

を与えるが，この後の操作を考えると，直接，

.. math::
   \dot{ q_i } &= F_q (q_1,\cdots,q_N, p_1,\cdots,p_N ) \\
   \dot{ p_i } &= F_q (q_1,\cdots,q_N, p_1,\cdots,p_N )

を与えてくれた方が便利である．
そのために，  :blue:`ルジャンドル変換を適用` する．

ラグランジアン :math:`L(q,\dot{q})` を :math:`\dot{q}` に関してルジャンドル変換すると， :math:`H(q,p)` (1次元)が次の表式で得られる．

.. math::
   H(q,p) = p\dot{q} - L(q,\dot{q})

多次元でも同様．これにより，ハミルトン方程式 ( *Hamilton Eq.* )は，

.. math::
   \dot{q_i} &= + \dfrac{ \partial H }{ \partial p_i } \ \ \ ( 1 \ge i \ge N ) \\
   \dot{p_i} &= - \dfrac{ \partial H }{ \partial q_i } \ \ \ ( 1 \ge i \ge N )

となる．



リウヴィルの定理 ( Liouville's Theorem )
==============================================

力学法則は，  :red:`位相空間体積を保存する` ．
位相空間上のとある領域を考える．領域内の運動は，無限次元ベクトル

.. math::
   u= \left[ \begin{array}{c}
   u_1     \\ u_2     \\ \vdots  \\ u_N     \\
   u_{N+1} \\ u_{N+2} \\ \vdots  \\ u_{2N}
   \end{array} \right]
   = \left[ \begin{array}{c}
   \dot{q}_1     \\ \dot{q}_2     \\ \vdots  \\ \dot{q}_N     \\
   \dot{p}_{N+1} \\ \dot{p}_{N+2} \\ \vdots  \\ \dot{p}_{2N}
   \end{array} \right]

これに対して，発散をとると，
   
.. math::
   \nabla \cdot u
   &= \sum_{j}^N \dfrac{ \partial u_j }{ \partial q_j } + \sum_{j}^N \dfrac{ \partial u_j }{ \partial p_j } \\
   &= \dfrac{ \partial \dot{q}_j }{ \partial q_j } + \dfrac{ \partial \dot{p}_j }{ \partial p_j } \\
   &= \dfrac{ \partial }{ \partial q_j } \dfrac{ \partial H }{ \partial p_j } - \dfrac{ \partial }{ \partial p_j } \dfrac{ \partial H }{ \partial q_j } \\
   &= 0
   
より，位相空間流れ :math:`u` は，非圧縮流であることがわかる．
つまり，とある領域内に含まれる体積は，保存される．



Hamilton方程式の座標変換 ( **正準変換** )
=============================================

* Lagrangeの運動方程式は点変換に関して，形を変えない．
* Hamilton方程式に対して，どのような変換（写像）がHamilton方程式を不変とするのか？
* このような変換は存在し，これを :red:`正準変換` という．


  
正準変換の直接条件
=============================================

正準変換である **必要十分条件** は次である．

.. math::
   \dfrac{ \partial Q_i  }{ \partial q_j } &= + \dfrac{ \partial p_j }{ \partial P_i } \\
   \dfrac{ \partial Q_i  }{ \partial p_j } &= - \dfrac{ \partial q_j }{ \partial P_i } \\
   \dfrac{ \partial P_i  }{ \partial p_j } &= + \dfrac{ \partial q_j }{ \partial Q_i } \\
   \dfrac{ \partial P_i  }{ \partial q_j } &= - \dfrac{ \partial p_j }{ \partial Q_i } \\


正準変換は次のような性質を持つ．

* **点変換は，正準変換の一つ** である．（ラグランジアンが不変に保たれるのは，Hamiltonianも不変に保たれるから）
* **正準変換の逆変換は正準変換** である．（正準変換を元に戻すのも正準変換）
* **正準変換の合成変換は正準変換** である．（正準変換を何度繰り返しても正準変換）


  
母関数
======================================

座標変換 :math:`q_i \rightarrow Q_i` したいけど，変換の際に正準変換となるような変換を構築するのはどうしたら良いのか？
  
母関数 :math:`W(q,Q)` に対して， :math:`P=-\partial W / \partial Q` とすれば良い．

このような関係と座標変換を構築する手法はいくつか知られている．
:blue:`母関数は，正準変換するためのツールのようなもの` である．


 
