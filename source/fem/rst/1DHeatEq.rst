##############################################################
１次元熱拡散方程式の定常解に対する有限要素解析(定式化編)
##############################################################

=========================================================
厳密解
=========================================================

x=0でT=0の熱浴に接触した熱伝導係数 :math:`\lambda` ，熱生成項 :math:`\dot{Q}` の断面積 :math:`A` の棒状の物質を考える．系は1次元の並進対称系とする．支配方程式は，

.. math::
   \dfrac{ \partial }{ \partial x } [ \lambda \dfrac{ \partial T }{ \partial x } ] + \dot{Q} = 0

この解のうち，熱伝導係数も熱生成項も位置によらず，一定であった場合を考える．

両辺積分して，

.. math::
   \lambda \dfrac{ \partial T }{ \partial x } = - \int \dot{Q} dx = - \dot{Q} [ x + C_1 ]

:math:`x=x_{max}` における自由境界条件 :math:`\partial T / \partial x=0` より，

.. math::
   \partial T / \partial x (x=x_{max}) &= - \dfrac{\dot{Q}}{\lambda} [x+C_1] = 0 \\
   C_1 &= - x_{max}

再度積分して

.. math::
   T = - \dfrac{ \dot{Q} }{ \lambda } [ \dfrac{1}{2} x^2 - x_{max} x + C_2 ]
   
固定端境界条件 :math:`T(x=0)=0` を用いて，

.. math::
   T &= - \dfrac{ \dot{Q} }{ \lambda } [ C_2 ] = 0 \\
   C_2 &= 0

上記より，

.. math::
   T = - \dfrac{ \dot{Q} }{ \lambda } [ x ( \dfrac{1}{2} x - x_{max} ) ]

が解となる．
   

=========================================================
近似解を代入して考えてみる
=========================================================

区間 :math:`[X_k,X_{k+1}]` に存在する :math:`x` における温度を各接点の情報 :math:`\phi_k,\phi_{k+1}` から例えば **1次要素 (線形近似)** を用いて表す．

.. math::
   u_M
   &= ( \dfrac{X_{k+1}-x}{L} ) \phi_k + ( \dfrac{x-X_k}{L} ) \phi_{k+1} \\
   &= N_k(x) \phi_k + N_{k+1}(x) \phi_{k+1}

ここで， :math:`N_k(x)` は点kに関する形状関数で位置xの関数である． 上式では線形要素を例として表記したが，1次以上の形状関数を用いても同様に表すことができ，位置 :math:`x` における解 :math:`u_M(x)` は一般に次のように表せる．

.. math::
   u_M(x) = \sum_j T_j N_j(x) 

これは，試行関数の重ね合わせによる近似解( :math:`u_M=\sum_j a_j \Psi_j` )に他ならない．

区間 :math:`[X_k,X_{k+1}]` の間の解は上式のように形状関数の重ね合わせで表すことができる．
重ね合わせは次のようにベクトルによる内積の表式を用いればスッキリと表せる．

.. math::
   u_M(x) = [N] \{ \phi \}

ここで， :math:`\{ \cdot \}{}` は **縦ベクトル** ， :math:`[\cdot]` は **横ベクトル** を表している．
上記の連立方程式は問題を分割したひとつの要素に注目して得られていることを強調しておく．
つまり，問題全体として，方程式は **[要素分割数]個** できることになる．



=========================================================
*Green* の定理の適用
=========================================================

:math:`x=x_i \ (i=1,\cdots,n)` における任意の重み関数 :math:`w_i \ \ (i=1,2,\cdots,n)` を考え，重み付き残差法の式 :math:`\int_V w_i R dV = 0` に対して 1次元の *Green* の定理 :math:`\int_V v \dfrac{ d^2u }{ dx^2 } dV = \int_S v \dfrac{du}{dx} dS + \int_V \dfrac{dv}{dx} \dfrac{du}{dx} dV` を適用する．

.. math::
   \int_V w_i \{ \lambda \dfrac{d^2 T}{dx^2} + \dot{Q} \} dV 
   &= \lambda \int_V w_i \dfrac{d^2 T}{dx^2} dV + \int_V w_i \dot{Q} dV \\
   &= \lambda \int_S w_i \dfrac{d T}{dx} dS - \lambda \int_V \dfrac{d w_i}{dx} \dfrac{d T}{dx} dV + \int_V w_i \dot{Q} dV \\
   &= 0

ここに，要素分割による形状関数による近似 :math:`T=u_M = [N] \{\phi\}{}` を代入すれば，

.. math::
   \lambda \int_V \dfrac{d w_i }{dx} \dfrac{d [N]}{dx} \{\phi\} dV = \lambda \int_S w_i \dfrac{d [N]}{dx} \{\phi\} dS + \int_V w_i \dot{Q} dV

となる．面積分項は流束を用いて，

.. math::
   \lambda \int_S w_i \dfrac{d [N]}{dx} \{\phi\} dS = - \int_S w_i q dS

と表すことができ，隣接する要素間で流出量と流入量は打ち消しあい，要素内部では意味を持たない．
この項は境界条件においてのみ意味をもつ．このように表すと，

.. math::
   \lambda \int_V \dfrac{d w_i }{dx} \dfrac{d [N]}{dx} \{\phi\} dV = - \int_S w_i q dS + \int_V w_i \dot{Q} dV

ここでは， :math:`w_i \ \ (i=1,\cdots,n)` に対する式を導出した．重み関数はn個の節点情報を求めるために，n個用いることで方程式系を閉じさせる．これらをベクトルによってまとめて取り扱うように次のように表記しておく．

.. math::
   \lambda \int_V \dfrac{d \{w\} }{dx} \dfrac{d [N]}{dx} \{\phi\} dV = - \int_S \{w\} q dS + \int_V \{w\} \dot{Q} dV


   
=========================================================
*Galerkin* 法の適用
=========================================================

*Galerkin* 法では， :math:`w_i=\Psi_i` を採用する．ここでは， :math:`\{w\}=[N]^{T}` とすれば良い．

.. math::
   \lambda \int_V \dfrac{d [N]^{T} }{dx} \dfrac{d [N]}{dx} \{\phi\} dV = - \int_S [N]^T q dS + \int_V [N]^T \dot{Q} dV

上式が **Galerkin法における有限要素法の式** である．
今，節点変数を除いた部分を

.. math::
   [k]  ^{e} &= \lambda \int_V \dfrac{d [N]^{T} }{dx} \dfrac{d [N]}{dx} dV \\
   \{f\}^{e} &= - \int_S [N]^T q dS + \int_V [N]^T \dot{Q} dV

とおけば，各有限要素における近似解は，

.. math::
   [k]^{(e)} \{ \phi \}^{(e)} = \{ f \}^{(e)}

と書ける．
ここで，上付き(e)は要素毎( by element )の式であることを意味しており，分割した要素を全て集めると，解くべき式の行列表現となる．
行列表現の意味するところは，勿論，有限要素法の帰着する先が連立方程式であることである．
つまり，行列反転さえ行えば，節点変数である :math:`\{\phi\}{}` が求解可能である．


=========================================================
:math:`[k]^{(e)}` 及び :math:`{f}^{(e)}` の計算
=========================================================

左辺のk-Matrix(k-マトリクス)，及び，右辺のf-vector(f-ベクトル)を求めれば，ある要素における節点情報を解くことができる．
これらを規定しているのは，形状関数 :math:`[N]` であるので，例として再度1次要素を取り上げて，計算を行う．

区間 :math:`[X_k,X_{k+1}]` の端部2節点による形状関数は

.. math::
   N_{k}   &= \dfrac{X_{k+1}-x}{L} = 1 - x/L \\
   N_{k+1} &= \dfrac{x-X_{k  }}{L} =   + x/L 

であるから，これらの微分は以下になる．

.. math::
   \dfrac{ dN_{k  } }{ dx } &= - \dfrac{1}{L} \\
   \dfrac{ dN_{k+1} }{ dx } &= + \dfrac{1}{L}

ベクトルとしてまとめて表記すると，

.. math::
   [N] =
   \begin{bmatrix}
   \dfrac{X_{k+1}-x}{L} & \dfrac{x-X_{k  }}{L}
   \end{bmatrix}

.. math::
   \dfrac{ d [N] }{ dx } =
   \begin{bmatrix}
   - \dfrac{1}{L} & + \dfrac{1}{L}
   \end{bmatrix}
   

である．これを用いて，要素毎のk-Matrixを求めると，

.. math::
   [k]^{e}
   &= \int_V \lambda ( \dfrac{d[N]^T}{dx} \dfrac{d[N]}{dx} ) dV \\
   &= \lambda \int_0^L
   \begin{bmatrix}
   - \dfrac{1}{L} \\
   + \dfrac{1}{L}
   \end{bmatrix}
   \begin{bmatrix}
   - \dfrac{1}{L} & + \dfrac{1}{L}
   \end{bmatrix}
   A
   dx \\
   &= \dfrac{ \lambda A }{ L^2 } \int_0^L
   \begin{bmatrix}
   +1 & -1 \\
   -1 & +1 
   \end{bmatrix}
   dx \\
   &= \dfrac{ \lambda A }{ L }
   \begin{bmatrix}
   +1 & -1 \\
   -1 & +1 
   \end{bmatrix}

次に，f-vectorを項別に求めると，

(熱生成項)

.. math::
   \int_V [N]^T \dot{Q} dV
   &= \int_{0}^{L}
   \begin{bmatrix}
   1-x/L \\
    +x/L
   \end{bmatrix}
   \dot{Q} A dx \\
   &= \dot{Q} A
   [
   \begin{bmatrix}
   x - \dfrac{x^2}{2L} \\
     + \dfrac{x^2}{2L}
   \end{bmatrix}
   ]_0^L
   = \dot{Q} A
   \begin{bmatrix}
   + \dfrac{1}{2}L \\
   + \dfrac{1}{2}L
   \end{bmatrix} \\
   &= \dfrac{ \dot{Q} AL }{2}
   \begin{bmatrix}
   1 \\
   1
   \end{bmatrix}

(熱流束項)
     
.. math::
   \int_S [N]^T q dS
   = q A \|_{x=L}
   = q A
   \begin{bmatrix}
   0 \\
   1
   \end{bmatrix}

ここで，熱流束項は自由境界端部でのみ作用する．

以上の導出から，とある要素における有限要素法が満たすべき連立方程式は，

.. math::
   [k]^{(e)} \{ \phi \}^{(e)} &= \{ f \}^{(e)} \\
   \dfrac{ \lambda A }{ L }
   \begin{bmatrix}
   +1 & -1 \\
   -1 & +1 
   \end{bmatrix}
   \begin{bmatrix}
   \phi_{k} \\
   \phi_{k+1}
   \end{bmatrix}
   &= \dfrac{ \dot{Q} AL }{2}
   \begin{bmatrix}
   1 \\
   1
   \end{bmatrix}
   - q A
   \begin{bmatrix}
   0 \\
   1
   \end{bmatrix} _{if \ ( k \ is \ edge )} 

この連立方程式を解いて， :math:`[\phi_k,\phi_{k+1}]` を求めれば，節点温度を解析得ることができる．
これは要素一つだけに着目した解であり，境界条件が影響しない要素はほぼ無意味な端部条件による解しか得られない．
実際には，境界条件から情報が内部のセルへ浸透していき，端部での節点温度の求解が内部領域の節点温度として作用していくので，要素全体で一斉に解を得ることが正しい解を得るために必須となる．

つまり，これまでに導出した要素方程式系( Element Matrix & Element Equations )を集めて，系全体の方程式系 ( Global Matrix & Global Equations )を構成する必要がある．これは決して難しいことではなく，単に集合させるだけで良い．結果，要素行列をまとめたGlobal Matrixが以下のように定義される．

.. math::
   [K]        &= \sum     [k]    \\
   \{ \Phi \} &= \sum \{ \phi \} \\   
   \{ F \}    &= \sum \{ f    \}

解くべき Global Equationsを，次式に表す．

.. math::
   [K] \{ \Phi \} = \{ F \}

Global Equationsを行列反転させれば，有限要素法によって得たい解 (ここでは１次元熱拡散方程式の定常解)を得ることができる．
