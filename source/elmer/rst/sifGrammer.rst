===============================================================================
Elmer (Non-GUI向け) 設定ファイル(.sif) の記法について
===============================================================================

Elmer(Non-GUI)用の設定ファイルの書き方についての殴り書き備忘録(要整備)．


全体構成
=========================================================

* Fortran の Parameterファイル likeな記法．
* いくつかのまとまり（大分類）が存在し、まとまり(Section)毎にキーワード内包している．
* 各キーワード(項目名)と値を1対1対応させるような形式．


全体ルール
=========================================================

* 拡張子=".sif" ( 多分違ってても何ら問題無し )
* コメント文字は"!"．コメント文字前スペースは許される．
* Case Insensitive ( 大文字/小文字区別無し )
* "大分類名" で始まり、 "End" で終わる構造をファイル内に必要分だけ記述する．
* もし、定義されていない数値があった場合、自動的にデフォルト値が用いられる．
* キーワードと値の区切り文字は"="
* 配列は、"キーワード名(配列サイズ) = A B C ..." となる．(e.g. gravity(4) = 0 0 -1 9.82 )
* 論理変数の指定には、"キーワード名 = Logical True/False" となる．(ここでのLogical はキャスト扱い．省いても大丈夫．Realキャストもある．)
* 変数間がある関数 :math:`y=f(x)` で対応づけられる時、これを数値データとして与えることができる．次のようにして表す．これは初期条件や境界条件の指定時に用いることができる．データ間は線形に内挿される．

.. code-block::
   :caption: 関数応答の表現 (データテーブル表記)
             
   yval = Variable Coordinate 1
   Real
     0.0 0
     1.0 1.0
     2.0 4.0
     3.0 9.0
     4.0 16.0
   End


  
  

指定するSectionについて
=========================================================

指定するSectionには以下がある．

* Header
* Constants
* Simulation
* Solver
* Equation
* Body
* Body Force
* Material
* Initial Condition
* Boundary Condition

Header / Constants / Simulation は複数回にわけて記述してもエラーはでない(そんなことをする意味はないが)．
Header / Constants / Simulation 以外は条件に合わせて複数個定義する．それらの区別には番号nをSection名の後につける．( e.g. Body 1 / Solver 3 etc. )


Header Sectionについて
=========================================================

最初に読み込むべき、Elmer実行時のHeaderが記載されたSection. Mesh DBはほぼ確実に指定する必要があるので、ほぼ全ての.sifファイルにおいて、最初に指定されるSection．

.. code-block::
   :caption: Headerの指定例
   
   Header
     CHECK KEYWORDS "Warn"
     Mesh DB "." "model"
     Include Path ""
     Results Directory ""
   End


* Keyword Check "Warn" :: キーワードチェック時の動作．( 抜粋 "usually placed in the beginning of the input file. When this command is given, the solver outputs warning messages if the input file contains keywords that are not listed in the file of known keywords. If newkeywords are introduced, misleading warning messages can be avoided by adding the new keywords to thekeyword fileSOLVER.KEYWORDS, located in the directory of the shared library files of ElmerSolver. Theother options includeignore, abort, silent." )
* Mesh DB "Dir" "MeshDir" :: メッシュデータベース(=メッシュが格納されたディレクトリ)の場所を指定．第一引数:ディレクトリの存在する場所、第二引数:ディレクトリ名． (e.g. Mesh DB "." "model" は、 "./model" がメッシュファイルが格納された場所になる．)
* Include Path "" :: Include Pathを通して置く場所．共通して使うライブラリ等があれば指定．
* Results Directory :: 結果格納用ディレクトリ


Constants Sectionについて
======================================

シミュレーション内で使用される定数を記載する．

.. code-block::
   :caption: Constants section の指定例

   Constants
     Stefan Boltzmann = 5.6704e-8
     Boltzmann Constant = 1.3807e-23
     Gravity(4) = 0 0 -1 9.82
   End


各係数を定義．

* Gravity(4) :: ( ex ey ez magnitude)で指定(サイズ4の配列)．ex ey ez は重力が働く向き、magnitudeは重力の大きさ．



Simulation Sectionについて
======================================

シミュレーションを統括する一般的な指定事項を記載する．


.. code-block::
   :caption: Simulation section の指定例

   Simulation
     Coordinate System = "Cartesian 3D"
     Coordinate Mapping(3) = 1 2 3
     
     Simulation Type = "Steady State"
     Steady State Max Iterations = 20
     Timestepping Method = "Explicit Euler"

     Solver Input File = "elastic_linear.sif"
     Output File = "elastic_linear.dat"
     Post File = "elastic_linear.vtu"
   End

* Simulation Type :: "過渡応答" か "定常状態" か ( Transient / Steady State )
* Coordinate System :: 座標系について書く ( Cartesian 1D / Cartesian 2D / Cartesian 3D / Polar 2D / Polar 3D / Cylindric / Cylindric Symmetric and Axi Symmetric )
* Coordinate Mapping :: 座標系のマッピング ( xyz系, xzy系, RTZ系, RZT系 etc. )
* Timestepping Method :: 時間積分法 ( Newmark / BDF )．Newmark は Newmark Beta、BDF は BDF Orderの指定が必要．Newmark で Newmark Beta = 0.0, 0.5, 1.0 のときは、それぞれ、Explicit Euler, Crank-Nicolson, Implicit Euler に相当する．ので、Newmark Beta無しに、Timestepping Methodとして、3つのうちのいずれかを指定しても良い．
* Steady State Max Iterations :: 定常解析の最大反復回数
* Solver Input File :: .sif ファイルの名前．何の意味があるのかよくわからない．
* Output File :: 出力ファイル名 ( 実行状況・結果を記したテキストファイル )
* Post File :: ポスト解析用ファイル．拡張子に".vtu"を指定すると自動的に VTK 形式で出力．あとは".ep" (elmer postファイル形式)だが、ElmerのGUIがないと使えない．


Equation Sectionについて
======================================

どういう方程式系をFEMで解析するのかを記述する．これは、Body 毎に指定できる ( e.g. Body m では、Equation n を解く )．
Equation は、1つ以上の Solver の集まり ( e.g. Equation n = Solver i + Solver j etc. )．
つまり、Body, Equation, Solverの関係は、 **Body n == Equation m << ( Solver i, Solver j, ... )**


といった構成になる．各種解析毎にすでに定められているものがあるので、大体はチュートリアルを参考にすれば良い．

.. code-block::
   :caption: 応力解析の例

   Equation 1
     Name               = "StressAnalysis"
     Stress Analysis    = True
     Calculate Stresses = Logical False
   End

* Name :: 方程式系の名前.
* Stress Analysis :: 線形応力解析をするかどうか．
* Calculate Stresses :: 応力を計算するかどうか．


.. code-block::
   :caption: ソルバ組み合わせの例

   Equation 1
     Name              = "CombinedSolver"
     Active Solvers(2) = 1 2
   End

   Solver 1
     ...
   End

   Solver 2
     ...
   End

* Active Solvers :: 使用するSolverのリスト．

  
Solver Sectionについて
======================================

どういうSolverを使うのかを指定．

.. code-block::
   :caption: 基本的なSolverの指定値

   Solver 1
     Exec Solver   = "Always"
     Equation      = "Stress Analysis"
     Variable      = "Displacement"
     Variable Dofs = 3
     Exported Variable 1 = "Displacement"
   End


* Exec Solver :: いつ実行しますか？ ( never / always / before all / before timestep / after timestep / before saving / after saving / after all. )
* Equation :: どんな方程式を解きますか？ ( ElmerModelManuals.pdf 参照 )
* Variable :: 何を変数としますか？ ( 変数名の指定 )
* Variable Dofs :: 変数の自由度
* Exported Variable 1 :: 出力される変数の名前


  
.. code-block::
   :caption: 線形 / 非線形 その他解析毎に指定するキーワード例

   Solver 1
     Linear System Solver = "Iterative"
     Linear System Iterative Method = "BiCGStab"
     Linear System Max Iterations = 10000
     Linear System Convergence Tolerance = 1.0e-3
     Linear System Preconditioning = "ILU0"
     Steady State Convergence Tolerance = 1.0e-5
     Nonlinear System Convergence Tolerance = 1.0e-3
     Nonlinear System Max Iterations = 1
   End




Body Sectionについて
======================================

Bodyはメッシュ内の各 Physical Objects ( Line/Surface/Volume ) に対して指定する．まとめて指定するのも可能．
これらPhysical Objects がどのような特性を有し、どのような方程式系で解かれるのかを指定する．
指定する要素には

* Name :: ( Bodyに名前を付けれる )
* Target Bodies(*) :: どのPhysical Objects を対象とするか．
* Equation :: ( どのような方程式系を適用するか )
* Material :: ( どのような物性値を有しているか )
* Body Force :: ( どのような体積力：重力、外力、熱ソース/シンク etc. )
* Initial Condition :: ( 初期条件はどうするか )

がある．
  
.. code-block::
   :caption: Body の指定例

   Body 1
     Target Bodies(1) = 301
     Name = "Body1"

     Equation = 1
     Material = 1
     Body Force = 1
     Initial Condition = 2
   End


Material Sectionについて
======================================

割り当てる物性値．


.. code-block::
   :caption: 応力解析の例．

   Material 1
     Name           = "Iron_SS400"
     Youngs Modulus = 200.0e9
     Poisson Ratio  = 0.3
   End

* Name :: 名前
* Youngs Modulus :: Youngs 率 ( ヤング率 : 単位 N/m^2 = Pa )
* Poisson Ratio :: Poisson比 ( ポアソン比 : 単位 無次元 )



Body Force Section について
======================================

体積力を指定する．



Initial Condition Section について
======================================

初期状態を指定する．


Boundary Condtion Section について
======================================

境界条件を指定する．


.. code-block::
   :caption: 応力解析における固定境界条件( Dirichlet Condition )指定例．
   
   Boundary Condition 1
     Name = "Constraint1"
     Target Boundaries(1) = 201

     Displacement 1 = 0
     Displacement 2 = 0
     Displacement 3 = 0
   End

* Name :: 名前を付けれる．
* Target Boundaries(*) :: 対象とする境界条件 ( Physical Objectsの番号::gmsh内で指定 ( mesh.boundaryに存在する番号 ). )
* Displacement 1 :: 変数名とその座標番号 を指定して、Dirichlet境界条件を課す．

.. code-block::
   :caption: 応力解析における境界に作用する力を指定する例( 力に対するDirichlet Condition )．
   
   Boundary Condition 2
     Name = "Constraint2"
     Target Boundaries(1) = 202

     Force 3 = -1.0e5


* Force 3 に配列で指し示す( - z方向 に 1e5 (N) の力 )を課す．-と1.0e5の間にスペースは許されない．
