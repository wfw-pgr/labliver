##############################################################
Gmsh python API のコマンド
##############################################################

=========================================================
occ  (python OpenCascade カーネルのコマンド )
=========================================================

* 図形計算ライブラリとして、OCCを利用したgmsh python APIコマンドを用いる．（⇔ built-in : .geo ）

  
---------------------------------------------------------
0次元：点を打つコマンド
---------------------------------------------------------

::
    
    $ (int tag) = gmsh.model.occ.addPoint(x, y, z, meshSize=0., tag=-1)



+ 戻り値は tag

---------------------------------------------------------
1次元：線を書くコマンド
---------------------------------------------------------

::
   
    $ (int tag) = gmsh.model.occ.addLine(startTag, endTag, tag=-1)
    $ (int tag) = gmsh.model.occ.addCircleArc(startTag, centerTag, endTag, tag=-1)
    $ (int tag) = gmsh.model.occ.addCircle(x, y, z, r, tag=-1, angle1=0., angle2=2*pi, zAxis=[], xAxis=[])
    $ (int tag) = gmsh.model.occ.addCircle(x, y, z, r, tag=-1, angle1=0., angle2=2*pi, zAxis=[], xAxis=[])
    $ (int tag) = gmsh.model.occ.addEllipseArc(startTag, centerTag, majorTag, endTag, tag=-1)
    $ (int tag) = gmsh.model.occ.addEllipse(x, y, z, r1, r2, tag=-1, angle1=0., angle2=2*pi, zAxis=[], xAxis=[])
    $ (int tag) = gmsh.model.occ.addSpline(pointTags, tag=-1, tangents=[])
    

    $ (int tag) = gmsh.model.occ.addBSpline(pointTags, tag=-1, degree=3, weights=[], knots=[], multiplicities=[])



+ 戻り値は、作成した線のタグ．

    
      
---------------------------------------------------------
１次元ジオメトリから２次元ジオメトリを生成コマンド
---------------------------------------------------------

::
    
    $ (int tag) = gmsh.model.occ.addWire(curveTags, tag=-1, checkClosed=False)
    $ (int tag) = gmsh.model.occ.addCurveLoop(curveTags, tag=-1)
    $ (int tag) = gmsh.model.occ.addPlaneSurface(wireTags, tag=-1)
    $ (int tag) = gmsh.model.occ.addSurfaceFilling(wireTag, tag=-1, pointTags=[], degree=3, numPointsOnCurves=15, numIter=2, anisotropic=False, tol2d=0.00001, tol3d=0.0001, tolAng=0.01, tolCurv=0.1, maxDegree=8, maxSegments=9)    


    
+ 戻り値は、作成したワイヤ及びカーブループのタグ．
+ addPlaneSurface は wireTags (リストを要求するのでそのままタグ番号を整数で渡さないように注意．)
    

    
---------------------------------------------------------
2次元：面を描くコマンド
---------------------------------------------------------

::
   
    $ (int tag) = gmsh.model.occ.addRectangle(x, y, z, dx, dy, tag=-1, roundedRadius=0.)
    $ (int tag) = gmsh.model.occ.addDisk(xc, yc, zc, rx, ry, tag=-1, zAxis=[], xAxis=[])

    
    
+ 戻り値は tag 

      
---------------------------------------------------------
２次元ジオメトリから３次元ジオメトリの生成コマンド
---------------------------------------------------------

::
   
    $ (int tag) = gmsh.model.occ.addSurfaceLoop(surfaceTags, tag=-1, sewing=False)
    $ (int tag) = gmsh.model.occ.addVolume(shellTags, tag=-1)


    
+ 戻り値は tag 

    
---------------------------------------------------------
３次元：立体基本図形を挿入するコマンド
---------------------------------------------------------

::
   
    $ (int tag) = gmsh.model.occ.addSphere(xc, yc, zc, radius, tag=-1, angle1=-pi/2, angle2=pi/2, angle3=2*pi)
    $ (int tag) = gmsh.model.occ.addBox(x, y, z, dx, dy, dz, tag=-1)
    $ (int tag) = gmsh.model.occ.addCylinder(x, y, z, dx, dy, dz, r, tag=-1, angle=2*pi)
    $ (int tag) = gmsh.model.occ.addCone(x, y, z, dx, dy, dz, r1, r2, tag=-1, angle=2*pi)
    $ (int tag) = gmsh.model.occ.addWedge(x, y, z, dx, dy, dz, tag=-1, ltx=0., zAxis=[])
    $ (int tag) = gmsh.model.occ.addTorus(x, y, z, r1, r2, tag=-1, angle=2*pi, zAxis=[])


    
+ 戻り値は tag 

    
---------------------------------------------------------
３次元：２次元図形のスイープで作成するコマンド
---------------------------------------------------------

::
   
    $ (list of tuples (dim,tag) ) = gmsh.model.occ.extrude(dimTags, dx, dy, dz, numElements=[], heights=[], recombine=False)
    $ (list of tuples (dim,tag) ) = gmsh.model.occ.revolve(dimTags, x, y, z, ax, ay, az, angle, numElements=[], heights=[], recombine=False)
    $ (list of tuples (dim,tag) ) = gmsh.model.occ.addPipe(dimTags, wireTag, trihedron="")


    
+ 戻り値は **outDimTags** ( e.g. [(3,1)], [(3,1),(3,2),] )



---------------------------------------------------------
図形論理 (boolean) コマンド
---------------------------------------------------------

* 戻り値は **( outDimTags, outDimTagMap )**

  + 基本的にマップの方は使わないので、以下のように戻値を受けることを推奨する． ::

      $ ret,map = gmsh.model.occ.cut(...)

* 引数として、removeObject, removeTool ( logical ) があり、論理演算の入力：objectDimTags, toolDimTagsを残すか、消すかを選べる．基本は以下の動作か．

  + cut ： removeObject=True, removeTool=False
  + fuse： removeObject=True, removeTool=True
  + intersect： removeObject=True, removeTool=True

    
::
   
  $ ret = gmsh.model.occ.cut( objectDimTags, toolDimTags, removeObject=True, removeTool=True)
  $ ret = gmsh.model.occ.fuse( objectDimTags, toolDimTags, removeObject=True, removeTool=True )
  $ ret = gmsh.model.occ.intersect( objectDimTags, toolDimTags, removeObject=True, removeTool=True )
  $ ret = gmsh.model.occ.remove( dimTags, recursive=False)


---------------------------------------------------------
STEPファイルの読み込みコマンド
---------------------------------------------------------


::

   $ outDimTags = gmsh.model.occ.importShapes(fileName, highestDimOnly=True, format="")
  
