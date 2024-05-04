##############################################################
PHITS起動用スクリプト ( go__phits.py )
##############################################################

=========================================================
PHITS 起動用スクリプト
=========================================================

以下を実行

* 入力ファイルをプリコンパイル
* 実行
* 自動ポスト処理



=========================================================
起動方法
=========================================================

::

   $ go__phits.py inp/main_phits.inp

   
|

---------------------------------------------------------
プリコンパイルの書き方
---------------------------------------------------------

* 基本は、$<define> 句、$<loadJSON>句、$<include>句、$<postProcess>句、を使用して入力ファイルを作成．

  
|

---------------------------------------------------------
コマンドラインオプション
---------------------------------------------------------

.. csv-table::
   :header: "Arguments", "Input", "Description"
   :widths: 15, 15, 40
   :width:  750px
   
   "inpFile", "第一実引数 (必須)", "入力ファイル名（ e.g. main_phits.inp ）"
   "--phits_win", "optional, string", "windowsのPHITS実行コマンドパス (phitsSend2.bat)"
   "--phits_lin", "optional, string", "mac, LinuxのPHITS実行コマンドパス (phits.sh)"
   "--materialFile", "optional, string", "マテリアルデータベースのファイル名、指定するとmaterials_database_phits.inpを生成"
   "-c, --compile_mode", "optional, bool", "-cオプションを付加すると、PHITS実行、ポスト処理なし、プリコンパイルのみ．"

   
|

---------------------------------------------------------
必要な初期設定手順
---------------------------------------------------------

* スクリプトのコマンドプロンプト実行のためには、下記設定．

  - 先頭行にshebangを記載 ( e.g. #!/usr/local/env python3.10 ) ．
  - PATHの通ったところに置く ( e.g. "/usr/local/bin/" )．
  - 実行権限を付与 ( chmod +x go__phits.py )．

    
|

---------------------------------------------------------
go_phits.pyの設定
---------------------------------------------------------

* PHITSのパスの確認．

  .. code-block:: python

     default_settings = {
       "phits_win":r"C:\phits\bin\phitsSend2.bat", # install path of PHITS code. ( Windows )
       "phits_lin":r"phits.sh",                    # install path of PHITS code. ( Linux, mac )
     }
   

* OS判別は、os.name = "posix" / "nt" で判別 ( "posix":mac, Linux, "nt":Windows )
  
   + phits_winはウィンドウズ上でPHITSを動かす際の実行バッチのパス．
     
     - ( 送る->PHITS のバッチファイル"phitsSend2.bat" )．

   + phits_linはmac, Linuxでの実行スクリプト ( phits.sh )の場所、または、実行コマンド名．

     - phits.sh をパスの通ったところにあれば、"phits.sh" でよい．
     - WSLは phits_lin="posix"、phits.sh実行扱い．WSL上でインストール "phits.sh" のパスを通しておく．
