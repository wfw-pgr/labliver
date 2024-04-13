##############################################################
コンパイル関係のメモ
##############################################################

=========================================================
コンパイルに必要なソフトウェア
=========================================================

以下が必要であると噂されている．

* OpenCASCADE ( occt-7.6.0 or newer. )
* Fltk ( GUI tool )
* freetype

  
=========================================================
gmsh のビルド
=========================================================

* gmsh gitlab( https://gitlab.onelab.info/gmsh/gmsh ) に従う．
* ソースファイルの入手 ::

    $ git clone https://gitlab.onelab.info/gmsh/gmsh.git

* cmakeによるビルド ::

    $ mkdir build
    $ cd build
    $ cmake -DENABLE_BUILD_DYNAMIC=1 ..
    $ make

* オプションの-DENABLE_BUILD_DYNAMIC=1 はAPIを生成するオプション．つける．



=========================================================
gmsh の起動
=========================================================

* gmsh 起動しない ::

    $ gmsh
    
* python2で起動しようとする．/usr/local/env python がpython2を指してる． ::

    $ sudo emacs /usr/local/bin/gmsh
    [out] #! /usr/local/env python
    [in]  #! /usr/local/env python3

* これで、python3で実行しようとする．gmsh4.11.1が呼ばれる．
* 環境変数に、 gmshLibraryPath と PYTHONPATH がgmsh用にあり、どちらも /usr/local/lib に通しているけど、必要かどうかは不明．
  
