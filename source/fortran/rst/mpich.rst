=========================================================
mpich2のインストール
=========================================================

* 基本的には公式に従っていればよい． ( https://www.mpich.org/static/downloads/3.2/mpich-3.2-installguide.pdf )
* mpich2 ( http://www.mpich.org/downloads/ )
* インストール手順
    
  + tar を落としてくる
  + ディレクトリを展開
  + ./configure
  
    ::

       ./configure F77=ifort FC=ifort

  + make

    ::
   
       make 2>&1 | tee m.txt

  + install （もしかしたら失敗するかも )
  
  
    ::

       sudo make install |& tee mi.txt

    ifortが無いといって怒られる場合，libtool内でifortがわからなくなっている可能性があるので，これをちゃんと教えてあげる.

    ::

       locate compilervars.sh

    等で，ifortcoreのある場所を調べて, evansでは( /opt/intel/composerxe-2011/bin/ ), libtool内に以下を書き込み

    ::
     
       source /opt/intel/composerxe-2011/bin/compilervars.sh intel64


    これで，インストールができるようになった．mpiexec, mpifort等にパスが通っている場合にOK.
  
