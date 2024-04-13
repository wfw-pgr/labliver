=========================================================
macOS catalina へのインストールの方法
=========================================================

webベースの情報では、macOSへすんなりインストールできず、かなり苦労した．
ここで、私が成功したインストール方法についてまとめる．

brewを使った方法について
=====================================================

Homebrewを使ったインストールは私の環境ではうまくいかなかった．理由は、Mumps ( 現在非サポート? )のインストールでscalapackが入らずにつまづくから． なお、$ brew install scalapack しても、scalapackを消せと言われて先に進めない．::

  $ brew install dpo/openblas/mumps
  $ brew tap ElmerCSC/elmerfem
  $ brew install elmer --with-elmergui --HEAD --with-elmerice

  
を実行しろと書かれているのが多いけど、macOS catalinaからではインストールに失敗した．


ソースからビルドする方法について ( GUI無し )
=====================================================

うまくいかない時は、ソースからビルドしてみるのが推奨とelmerのページに書かれていた．ので、 https://www.csc.fi/web/elmer に書いてある通りに、実行してみた．::

  $ mkdir elmer
  $ cd elmer
  $ git clone git://www.github.com/ElmerCSC/elmerfem
  $ mkdir build
  $ cd build
  $ cmake -DWITH_ELMERGUI:BOOL=FALSE -DWITH_MPI:BOOL=FALSE -DCMAKE_INSTALL_PREFIX=../install ../elmerfem
  $ make -j2 install
  $ ctest -j2 

  
自分のCのコンパイラ環境が悪いんですが、後ほど、stdlib.hがないとかでおこられます．勿論、そんなわけなくて、指す場所がわからないだけです． .zshrc に ::

  export SDKROOT="$(xcrun --sdk macosx --show-sdk-path)"

  
を追記して、ヘッダファイルの場所がわかるようにすると解決．買ったばかりの macなので、そんなにいじくっている訳ではないので、デフォルトでCをコンパイルしようとするとおこられそうなのですが、macOS作っている会社、こんなこともできんOS作ってて本当に大丈夫か？などと思いつつ再度実行すると、まあ多分、GUI無しのElmerはインストールできるはず．

結構わんさかERRORとかWARNINGがでる... けど、なんとかインストールは可能．


ソースからビルドする方法について ( GUI有り )
=====================================================

実行すべきは、::
  
  $ cmake -DWITH_ELMERGUI:BOOL=TRUE -DWITH_MPI:BOOL=FALSE -DCMAKE_INSTALL_PREFIX=../install ../elmerfem

  

GCCを変更した場合
=====================================================

* 別のプログラムのインストール時に、gccを再インストール（バージョンも変更）、という事案があったらしく（事案とはGeant4の事案）、elmerが動かなくなっていた．

  + 新しくインストールしたgccを使用して、再度コンパイルすれば良い．
* この際、cMakeLists.txt の冒頭のgccがなぜか gcc-10 にバージョン指定．
  + gcc-12等（単にgccでいいかも）、利用するgccのバージョンへ変更後．cmake 
  + 他、上記コマンドに従って、再度インストール．問題なく動いた．
  + 相変わらず、大量にWARNINGはでる．（主にrank mismatch .... とか．）
* 問題なく動くが、テストの正答率は 94% 程度．失敗するのは、主にHarmonics・Eigenvalue・Helmholtz系（固有値系のソルバが死んでる？）なので、基本ソルバには影響は大きくはないとはおもっている．
