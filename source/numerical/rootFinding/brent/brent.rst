=========================================================
*Brent* 法 ( Brent solver )
=========================================================

*Brent* 法．


*Brent* 法のアルゴリズム
======================================

*Brent* 法のアルゴリズム．


*Brent* 法の特徴
======================================

長所

短所

  

サンプルコード
======================================

サンプルコードを以下に示す．

.. literalinclude:: code/main.f90
   :caption: main.f90
   :language: fortran
   :linenos:

      
.. literalinclude:: code/brentSolvMod.f90
   :caption: brentSolvMod.f90
   :language: fortran
   :linenos:


実行結果例
======================================

実行結果例を以下に示す．

.. code-block:: shell

   kent@euler ~/fortran/brentSolver $ ./main 
   [Main@brentSolver] x1, x2, res, sin(x)
   0.78524716339422451       -6.5658589676331758E-013  -6.5658589676331758E-013
   [Main@brentSolver] Answer should be...
   0.70699999999934338       0.70699999999999996     
