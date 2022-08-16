=========================================================
シンプレクティック性と解析力学
=========================================================

シンプレクティック記法
======================================

解析力学の特徴は， *Hamilton Eq.* における一般化座標と共役な運動量 :math:`q_k,p_k` の対称性である．対称性を活かして，N自由度系の状態を2N次元の相空間中の点rで表して，

.. math::
   r = \left[ \begin{array}{c}
   q_1 \\ q_2 \\ \vdots \\ q_N \\
   p_1 \\ p_2 \\ \vdots \\ p_N
   \end{array} \right]

とすれば， *Hamilton Eq.* は以下の一つの式で表すことができる．

.. math::
   \dot{r}_i = \sum_{j=1}^{2N} J_{ij} \dfrac{ \partial H }{ \partial r_j }

これを **シンプレクティック記法** という．


シンプレクティック記法の行列 :math:`\bm{J}`
=====================================================

行列 :math:`\bm{J}` は，

.. math::
   \bm{J} = \left[ \begin{array}{cc}
     \bm{0} & \bm{1} \\
   - \bm{1} & \bm{0}
   \end{array} \right]

で表される行列であり，以下のような性質がある．

* 転置行列について

.. math::
   \bm{J}^T = \left[ \begin{array}{cc}
   \bm{0} & - \bm{1} \\
   \bm{1} & \bm{0}
   \end{array} \right] = - \bm{J}

* 逆行列について

.. math::
   \bm{J} \bm{J}^T = \bm{J}^T \bm{J} = \bm{1} =
   \left[ \begin{array}{cc}
   \bm{1} & \bm{0} \\
   \bm{0} & \bm{1}
   \end{array} \right]

.. math::
   \bm{J}^T = \bm{J}^{-1} = - \bm{J}

* 行列の二乗について

.. math::
   \bm{J}^2   &= - \bm{1} \\
   | \bm{J} | &= 1



**シンプレクティック条件**
======================================

ここで取り扱う :red:`シンプレクティック条件` は， **シンプレクティック記法における正準変換の条件** である．正準変換の条件は，正準変換の直接条件を満たせばよかった．シンプレクティック条件はより見通しの良い表記になる．

正準変換 :math:`(q_i,p_i) \rightarrow (Q_i,P_i)` のシンプクレクティック記法 :math:`r_i \rightarrow R_i` を考える．正準方程式は，

.. math::
   \dot{R}_i = \sum^{2N}_{j=1} J_{ij} \dfrac{ \partial H }{ \partial R_j }

左辺を変形すると，

.. math::
   \dot{R}_i &= \sum^{2N}_{m=1} \dfrac{ \partial R_i }{ \partial r_m } \dot{r}_m \\
   &= \sum^{2N}_{m=1} \sum^{2N}_{k=1} \dfrac{ \partial R_i }{ \partial r_m } J_{mk} \dfrac{ \partial H }{ \partial r_k } \\
   &= \sum^{2N}_{m=1} \sum^{2N}_{k=1} \sum^{2N}_{j=1} \dfrac{ \partial R_i }{ \partial r_m } J_{mk} \dfrac{ \partial R_j }{ \partial r_k } \dfrac{ \partial H }{ \partial R_j } \\

上式と比較し，

.. math::
   \sum^{2N}_{m=1} \sum^{2N}_{k=1} \dfrac{ \partial R_i }{ \partial r_m } J_{mk} \dfrac{ \partial R_j }{ \partial r_k } = J_{ij}

以上より，
   
.. math::
   \bm{M} \bm{J} \bm{M}^T = \bm{J}

ここで，

.. math::
   M_{ij} = \dfrac{ \partial R_i }{ \partial r_j }

であり， :math:`\bm{M}` をシンプレクティック行列と呼ぶ．

以上の， :math:`\bm{M} \bm{J} \bm{M}^T = \bm{J}` を  :red:`シンプレクティック条件` という．


