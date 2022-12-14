=========================================================
二分法 ( Bisection Solver )
=========================================================

安定に解ける求解アルゴリズムの一つ．解を含む有限の区間を指定することができれば，その両端を解へと漸近させていくことで解を求めることができることを利用する．
二分法のアルゴリズムは以下の通り．

1. 方程式 :math:`f(x)=0` の初期解として，解 :math:`x_0` を含む有限の区間 :math:`[a,b]` の両端座標を与える．ただし， :math:`f(a), f(b)` は解 :math:`f(x_0)=0` を挟んで，異なる符号を有するものとする．
2. 解空間の両端の平均値 :math:`m=(a+b)/2` を計算する．
3. 解空間両端 a, b のうち，m と関数 :math:`f(\cdot)` の符号が同じであればをmと置き換える．
4. :math:`f(m) < \epsilon` ( :math:`\epsilon` ：許容誤差 ) であれば，解探索を終了する．条件を満たさない場合， 1-4 を再度繰り返す．


二分法の特徴
======================================

長所

* 解の存在が保証されており， **安定に解くことができる** ．

短所

* 解の **収束が遅い** ．
* 推測値として与える **初期解** の設定が比較的難しい．解の存在が保証され，およその座標を特定でき，正負両方向から挟んだ初期解を与える必要がある．

  
サンプルコード
======================================

以下に 二分法のサンプルコードを示す．

メインルーチン．初期解を与えて二分法ルーチンを呼び，結果を表示する．

.. literalinclude:: code/main.f90
   :caption: main.f90
   :language: fortran
   :linenos:

二分法求解ルーチン． *analyticFunc* が求解すべき関数 :math:`f(x)` を返却する解析関数．
サブルーチン *bisectionMethod* は，

.. literalinclude:: code/bisectionMod.f90
   :caption: bisectionMod.f90
   :language: fortran
   :linenos:


実行例
======================================

上記サンプルコードの実行例を示す．
解くべき方程式は， :math:`sin(x) = 0.707 \sim \sqrt{2}/2` とした．
有限の桁数で打ち切っているが，解は :math:`x_N \sim \pi/4` となるはずである．

.. code-block:: shell
                
   kent@euler ~/fortran/bisectionSolver $ ./main 
   0.78524716339597944        5.8453242246514492E-013   5.8453242246514492E-013  0.70700000000058449     

左から， 得られた解と数値的残差 :math:`x_N, y_N` ，解くべき方程式の理論残差値と左辺値 :math:`f(x_N), sin(x_N)` を示している．解は予想される値に十分近い値を示している． （ここでは，右辺を適当に0.707としている．）
