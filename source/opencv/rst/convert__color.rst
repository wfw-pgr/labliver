##############################################################
色空間の変更について
##############################################################

=========================================================
色空間の変更
=========================================================

* 画像の色空間を変更する．

  + 注意点としては、BGRやRGB は [ Nx, Ny, 3 ] など３要素を持つ numpy配列だが、
  + GRAY は、 [ Nx, Ny, 1 ] ( 実際は [Nx,Ny] ) の１値しか有していない（グレースケール）．
  + データ型は np.uint8 ( 符号なし整数型8bit値 : unsigned integer 8 bit ( 0-255まで ) )

  .. code-block:: python
                  
     img_rgb  = cv2.cvtColor( img_bgr , cv2.COLOR_BGR2RGB   )
     img_gray = cv2.cvtColor( img_bgr , cv2.COLOR_BGR2GRAY  )
     img_bgr  = cv2.cvtColor( img_gray, cv2.COLOR_GRAY2BGR  )


* グレースケールを介して逆変換すると、色画像には戻らない点に注意． ::

    img_bgr = cv2.cvtColor( cv2.cvtColor( img_bgr, cv2.COLOR_BGR2GRAY ), cv2.COLOR_GRAY2BGR )
                      

  + (Left) 元画像    (Right) bgr -> gray -> bgr の変換後画像
  + 一方で、 numpy配列の形状は、[ Nx, Ny, 3 ]．グレースケール値をBGR３要素に np.repeat しただけ．

    .. image:: ../image/lena_gray.jpg
               :width:  300px
               :align:  center


