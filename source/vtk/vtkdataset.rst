=========================================================
XML形式のVTKの基本構成
=========================================================

xml形式のvtkファイルの基本構成は以下である．
   
.. code-block:: xml
   :emphasize-lines: 1,2,4

   <?xml version="1.0"?>
     <VTKFile type="ImageData">
      ***データセット要素 ImageData に関する記述***
     </VTKFile>

１行目は **xml文書に共通であるXMLファイルであることの宣言文** である．２行目において **VTKFile形式の文書** であることと， **取り扱うデータセット要素** を宣言している．XMLのversion数にはあまり拘る必要はなく，1.0で問題ない．ここではImageDataと呼ばれるデータセット要素を用いることを宣言している．VTKFile のタグ間は，以下に述べるデータセット要素のうち，いずれかを用いる．


=========================================================
VTKで取扱うことができる各種データセット要素
=========================================================

Paraview等の各種 **レンダリングソフトウェア** で **3D表示** するためには，数値計算等で得られたデータを **自己無矛盾なデータとして与える** 必要がある．座標位置毎のデータ，データ同士の隣接・結合情報等の表現が必要となる．このように，  :blue:`数値データと3Dレンダリングの橋渡しするデータ規格及び記述・処理用ライブラリ群がVTK` である．VTKでは，以下に記す  :red:`データセット要素` と呼ばれる **データ構造** のうち，いずれかを用いることで3次元(2次元)データを表現する．

* <ImageData> (.vti)
* <RectilinearGrid> (.vtr)
* <StructuredGrid> (.vts)
* <PolyData> (.vtp)
* <UnstructuredGrid> (.vtu)


ImageData
======================================  

ImageDataはpixel数が定められた画像のように， **等間隔** ， **構造格子** の記述に用いることができる．ImageDataのアトリビュートに 最大・最小，原点，データ間隔を指定できる．PointDataは格子上のデータを指定する際に，CellDataは格子内のデータを指定する際に用いることができ，それぞれデータ点数が (Nx,Ny,Nz) と (Nx-1,Ny-1,Nz-1) の違いがある．

.. code-block:: xml
                     
   <ImageData WholeExtent="xMin xMax yMin yMax zMin zMax" Origin="x0 y0 z0" Spacing="dx dy dz">
      <Piece Extent="x1 x2 y1 y2 z1 z2">
        <PointData> Data </PointData>
        <CellData> Data </CellData>
      </Piece>
   </ImageData>


   
RectilinearGrid
======================================    

RectilinearGrid はSpacingやOriginを指定する必要がないが，PointDataタグ/CellDataタグとは別に **Coordinateタグ** を持ち， **各軸(e.g. x軸，y軸，z軸)** を指定する．

.. code-block:: xml

   <RectilinearGrid WholeExtent="xMin xMax yMin yMax zMin zMax">
      <Piece Extent="x1 x2 y1 y2 z1 z2">
        <PointData>  Data </PointData>
        <CellData>   Data </CellData>
        <Coordinate> Data </Coordinate>
      </Piece>
   </ImageData>

Coordinateタグの例． **ImageDataは等間隔直交構造格子の記述のみ** であるが，RectilinearGridでは，  :blue:`不等間隔格子や円柱・極座標の記述も可能` である． Coordinateタグによる各軸の指定は以下のようになる．

.. code-block:: xml

   <Coordinates>
     <DataArray> x0 x1 x2 x3 ... </DataArray>
     <DataArray> y0 y1 y2 y3 ... </DataArray>
     <DataArray> z0 z1 z2 z3 ... </DataArray>
   </Coordinates>

   
StructuredGrid
======================================

StructuredGrid は RectilinearGrid 同様に，構造格子上のデータを指定できる． RectilinearGrid では，データ点の座標位置を指定する際に **Coordinateタグ** を用いたが， **StructuredGridはPointsタグを用いる** . 

.. code-block:: xml

   <RectilinearGrid WholeExtent="xMin xMax yMin yMax zMin zMax">
      <Piece Extent="x1 x2 y1 y2 z1 z2">
        <PointData>  Data </PointData>
        <CellData>   Data </CellData>
        <Points>     Data </Points>
      </Piece>
   </ImageData>

ここで，Pointsタグは次のような ( データ点が存在する空間の次元, データ点数 ) のデータ配列から構成される．

.. code-block:: xml

   <Points>
     <DataArray NumberOfComponents="3">
       0.0 0.0 0.0
       1.0 0.0 0.0
       2.0 0.0 0.0
       0.0 1.0 0.0
       1.0 1.0 0.0
       ...
     </DataArray>
   </Points>

データ量の観点から言えば，StructureGridは冗長なデータ点数が多い．同じ，等間隔直交構造格子上のデータを表現するのであれば， (ImageData) < (RectilinearGrid) < (StrucutredGrid) となる．
