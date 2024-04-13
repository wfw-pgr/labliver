##############################################################
section: "solver"について 
##############################################################


=========================================================
Nonlinear Nonlinear System Newton (Newton法) について
=========================================================

非線形解の探索には、 **Picard Iteration** と、 **Newton Method** が使用できる．
ここで、 **Picard Iteration** は緩和係数 :math:`\alpha` を用いて、

.. math::

   y^{N+1} = \alpha y^{N+1}_{solved} + (1-\alpha) y^{N}

として、計算を進める．１次精度であり、収束は遅いが安定している．一方、 **Newton Method** は、関数の勾配を利用して解探索するため、 ２次精度で収束が速い．

Elmerでは、収束状況毎に逐次、以下の順序で解探索方法を変更する．

(1) Picard Iteration
(2) Newton Method

ざっくりと、Picard Iterationで探索した後、近いところでNewton法を適用することで、安定性と速さを両立した非線形解収束を得る．

この際、 **いつ手法を切り替えるか** を左右するのが、以下のパラメータである．


.. csv-table:: **title**
   :header: "Parameter", "Type", "Description"
   :widths: 40, 20, 40
   :width:  800px
   
   "Nonlinear System Newton After Iterations", "integer", "何回、線形解法を反復した後に、Newton Methodへ切り替えるか．"
   "Nonlinear System Newton After Tolerance", "real", "誤差スコアがどの程度以下となった際に、Newton Methodへ切り替えるか．"


=========================================================
Reference
=========================================================

* なし
