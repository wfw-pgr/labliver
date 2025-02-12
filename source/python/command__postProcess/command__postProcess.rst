##############################################################
ポスト処理実行スクリプト
##############################################################

=========================================================
パラメータファイルからのコマンド実行
=========================================================

* 計算後に、 **毎回、一定の決まったポスト処理** （グラフ生成など）をする場合、 :blue:`パラメータファイルにポスト処理を記載し自動実行できると便利` ．

  -  :blue:`情報整理` の観点で◎ ( readme 不要 )
  - スクリプト化すれば入力ファイル選択により  :blue:`自動実行可能`  ( e.g. go__phits.py )

|

=========================================================
使い方
=========================================================

---------------------------------------------------------
コマンドの記載
---------------------------------------------------------

* コメントラインとして、<postProcess>句を記載して、コマンドを記載する ::

  # <postProcess> cp out.dat result.dat


  - 記号 "#" はコメントマーク．変更可能．
  
|

---------------------------------------------------------
スクリプトの実行
---------------------------------------------------------

* command__postProcess.py スクリプトを呼ぶ．::

  $ command__postProcess.py parameter.inp
  
  or ::
    
  $ command__postProcess.py parameter.inp -c --comment_mark $

  etc.

  
|

---------------------------------------------------------
引数
---------------------------------------------------------

.. csv-table::   
   :header: "Argument", "Attribute", "Description"
   :widths: 10, 10, 20
   :width:  800px
   
   "inpFile", "第一引数", "入力ファイル名"
   "--comment_mark", "Optional", "コメント記号 ( Default: '#' )"
   "--command/-c", "Optional", "設定すればコマンド表示のみ、実行なし"

   
|


---------------------------------------------------------
コマンドの登録
---------------------------------------------------------

* 他のコマンドと同様、以下の３つを設定

  (1) スクリプト先頭におまじない（shebang）を記載  ( e.g. "#!/usr/bin/env python3.10" )
  (2) パスの通ったところにおく ( e.g. /usr/local/bin/ )
  (3) 実行権限付与 ( e.g. chmod +x /usr/local/bin/ )

* コマンドライン実行可能に ::

    $ command__postProcess.py replace_sample.conf --comment_mark $
  

|
  
=========================================================
コード
=========================================================

|

---------------------------------------------------------
ポスト処理実行スクリプト ( command__postProcess.py )
---------------------------------------------------------


.. literalinclude:: pyt/command__postProcess.py
   		    :language: python

|

---------------------------------------------------------
サンプル入力ファイル ( replace_sample.conf )
---------------------------------------------------------

.. literalinclude:: cnf/replace_sample.conf


|

---------------------------------------------------------
出力例
---------------------------------------------------------

::

   $ cd cnf
   $ command__postProcess.py replace_sample.conf --comment_mark $
   
