##############################################################
Canny Edge Detection について
##############################################################

=========================================================
Canny Edge Detection とは
=========================================================

* 1986年にJohn Canny によって考案されたエッジ検出手法である．


  .. note::

     "Canny edge detection is a technique to extract useful structural information from different vision objects and dramatically reduce the amount of data to be processed."


=========================================================
エッジ検出プロセス
=========================================================

* Canny法によるエッジ検出は次の５つのステージに分解することができる．

  1. ノイズ除去のためにガウシアンフィルタを適用する．
  2. Sobelフィルタを用いて、勾配強度を計算する．
  3. エッジの偽検出を防ぐために、勾配強度の制限もしくは下限値を適用する．
  4. ポテンシャルエッジを決定するために２重の閾値を適用する．
  5. ヒステリシスによってエッジ追跡する．弱いエッジ、強いエッジに接続していないエッジを取り除く．
  
  + ( 参考URL： "https://en.wikipedia.org/wiki/Canny_edge_detector" )
  + ( 参考URL： "https://imagingsolution.net/imaging/canny-edge-detector/" )


---------------------------------------------------------
1. ガウシアンフィルタによるノイズ除去
---------------------------------------------------------

* 画像Iに対して ガウシアンフィルタ :math:`F_{Gauss}` を作用させることで、ノイズ低減した画像Gを生成する．

  .. math::

     G = ( I * F_{Gauss} )
     

---------------------------------------------------------
2. 勾配強度の計算
---------------------------------------------------------

* x, y 方向のSobelフィルタ、 :math:`F_{Sobel}^{x}, F_{Sobel}^{y}` を畳込みすることにより、画像のx,y方向の微分を計算する．
  
  + Sobelフィルタは、 *画像の平均化を行いながらエッジ強調を行うフィルタ処理で、ノイズを低減しながらエッジを強調する* ことができる．
  + x 方向微分とy方向微分のSobelフィルタのカーネルは、例えば以下として表現される．

    .. math::

       F_{Sobel}^{x} = \begin{bmatrix}  -1 &  0 &  1 \\ -2 & 0 & 2 \\ -1 & 0 & 1   \end{bmatrix}, \ \ \ \ \ \ 
       F_{Sobel}^{y} = \begin{bmatrix}  -1 & -2 & -1 \\  0 & 0 & 0 \\  1 & 2 & 1   \end{bmatrix}

       
  + Sobelフィルタとの畳込み結果として、

    .. math::
       
       G_x = ( G * F_{Sobel}^{x} ) \\
       G_y = ( G * F_{Sobel}^{y} )

       
* 微分画像から、勾配強度、及び、勾配方向を次式で計算する．

  .. math::

     M(i,j) = \sqrt{ G_x(i,j)^2 + G_y(i,j)^2 } \\
     O(i,j) = \arctan \dfrac{ G_y(i,j) }{ G_y(i,j) }

  + O(i,j)はM(i,j) の偏微分方向の向いてるベクトルの0°から測定した角度値．
    

---------------------------------------------------------
3. 「勾配方向上の非極値抑制」によるエッジ細線化
---------------------------------------------------------

* 勾配強度M(i,j), O(i,j)は、連続的に変化する勾配強度と方向のスカラーマップ．
* より軽量で意味のある情報を抜き取るために、勾配の極値部分のみを抜き出すことで、エッジ候補の細線化を行う．
* O(i,j)を 0, 45, 90, 135°のいずれかの値へ離散化する（周囲９マス方向のうちいずれか）．
* 離散化方向の直線上のみで考えて、最も勾配の大きな成分のみをエッジ候補として残し、あとはすべて、捨てる．


---------------------------------------------------------
4. ヒステリシス処理による、エッジの決定
---------------------------------------------------------

* 得られたエッジ候補に対して、信頼性の高い強いエッジ候補と、信頼性の比較的低い弱いエッジ候補へと分類する．
* 強いエッジ候補は、そのままエッジとして使用し、弱いエッジ候補は、強いエッジ候補に接続するエッジ候補と孤立したエッジ候補に分類し、前者は強いエッジ候補と合成し、エッジ線の長距離化させる．

  + 強いエッジ候補は、勾配強度 :math:`M(i,j) >= \lambda_{High}` となるようなエッジ候補とする．
  + 弱いエッジ候補は、勾配強度 :math:`\lambda_{Low} <= M(i,j) <= \lambda_{High}` となるようなエッジ候補とする．

  + 弱いエッジ候補のうち、近傍画素が強いエッジ候補になっている場合のみ，連結成分処理により，強エッジ領域に結合する．
    

* これにより，最終出力の「長いエッジ」を得る．．

