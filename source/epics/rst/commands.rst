##############################################################
EPICS中のコマンドに関する備忘録
##############################################################


=========================================================
データベースファイル（.db ） について
=========================================================

---------------------------------------------------------
構成
---------------------------------------------------------

* データベースファイル(.db)の構成は、以下の通り． ::

    record( ai, "epics:temperature" )
    {
      field( DESC, "temperature of water" )
      field( DTYP, "stream" )
      field( INP , "@temperature.proto getTemperature PS1" )
      field( SCAN, "I/O Intr" )
    }

* 構成の規約としては以下、
  
  + ひとつの.db 中に データ単位：レコード（record）が複数定義され、
  + レコードは、属性：フィールド（field）を複数持ち、
  + フィールドごとに、一つの値（文字列）が割り当てられている．
    

---------------------------------------------------------
レコード（record）
---------------------------------------------------------

* レコードタイプの例については以下参照．

  + ai, ao, bi, bo
  + stringin, stringout, longin, longout
  + etc.

* 詳細は、 **EPICS Record Reference**  を参照のこと．

  + EPICS Record Reference ( https://epics.anl.gov/base/R7-0/6-docs/RecordReference.html )


---------------------------------------------------------
フィールド（field）
---------------------------------------------------------

* field( var1, var2 ) の形を取り、var1に属性のタイプを、var2に値を書き込む．
* 属性のタイプとしては、例えば以下がある．

.. csv-table:: **fieldの属性タイプ**
     :header: "属性のタイプ", "説明", "例"
     :widths: 10, 30, 20
            
     "DESC", "フィールドの説明情報、DESCription", "temperature of water"
     "DTYP", "レコードのデータ型、Data TYPe", "stream"
     "INP", "入力値の取得規約、どうやって入力するか．INPut", "@temperature.proto getTemperature PS1"
     "SCAN", "入出力頻度・タイミング．SCAN", "I/O Intr"


     
* stream型のINP, OUTについての記述は次の通り． ::

    INP/OUT = "(使用するプロトコル名) （プロトコル中の入力に使用する関数名） （プロトコルに渡す変数名）"


  ここで、プロトコルに渡す変数名は、IOCが把握しているものにする．
  TCP/IPやシリアルの値を用いる場合、ポートやデバイスへの紐付けを **"st.cmd" に記載するはず** である． ::

    (e.g.1) drvAsynIPPortConfigure( "web", "www.google.co.jp:80",0,0,0 )
    (e.g.2) drvAsynSerialPortConfigure( "PS1", "/dev/ttyACM0" )

  + それぞれ、 "web"に"www.google.co.jp:80"、
  + "PS1"に "/dev/ttyACM0" を割り当てており、 .dbファイルは、プロトコルにこれを渡し、プロトコルに従ってデータを取得、書込する．  


=========================================================
プロトコルファイル（.proto）について
=========================================================

* 通信規約を規定する関数を定義する．例を示す． ::

    Terminator = CR LF;
    putval{
      out "%s";
      in  "%d";
    }

  + ここでは、入出力のデータ区切り： **"Terminator"** と、データの取扱： **"puvVal関数"** が記載されている．
  + "CR LF" は "Carriage Return Line Feed" （キャリッジ・リターン、ライン・フィード）．（ つまり"\r\n"）
  + putval関数は、与えられた引数を フォーマット "%s" (文字列型)で出力する．

+ 例えば、シリアルポートから、文字列"RD 1\r\n"のようなバイト型文字列が送信されてきた場合（RS-232C通信のようなASCIIのコマンド）、ch1の値をint型として返す．


=========================================================
初期化スクリプト（st.cmd）に関して
=========================================================

--------------------------------------------------------------------------------
追記事項について
--------------------------------------------------------------------------------

以下の事項などを追記し、 st.cmd を作成する．

* StreamDeviceを使用する場合、protocolsディレクトリの位置を記載する． ::

    epicsEnvSet( "STREAM_PROTOCOL_PATH", ".:../../protocols" )

      
* 初期化時にロードするデータベースファイルを記載する． ::

    dbLoadRecords( "db/temperature.db", "user=epics" )

    
  + "user=epics" は .dbファイル内部で規定されている $(user)に値を与える事が可能．

  
  
* ethernetケーブルなどの、ハードウェアを使用する場合は、設定を記載する． ::
  
    (e.g.1) drvAsynIPPortConfigure( "web", "www.google.co.jp:80",0,0,0 )
    
    or
    
    (e.g.2 l.1) drvAsynSerialPortConfigure( "PS1", "/dev/ttyACM0" )
    (e.g.2 l.2) asynSetOption ("PS1", 0, "baud", "19200")





--------------------------------------------------------------------------------
命令を表にまとめておく．（Sphinxのcsv-table都合でカンマは/に置換．）
--------------------------------------------------------------------------------


.. csv-table:: **"st.cmd"内のコマンド**
   :header: '式', '説明
   :widths: 40,40

   'epicsEnvSet( "環境変数名"/"値" )', '環境変数をセットする． (e.g.) epicsEnvSet( "STREAM_PROTOCOL_PATH"/ ".:../../protocols" )'
   'dbLoadRecords( ".dbファイル名"/"キーワード類" )', '.dbファイルを読み込む．(e.g.) dbLoadRecords( "db/temperature.db"/ "user=epics" )'
   'drvAsynIPPortConfigure( "変数名"/"IPアドレス:ポート番号"/0/0/0 )', 'TCP/IP通信のアドレス、ポート情報を変数に割り当てる (e.g.) drvAsynIPPortConfigure( "web"/"www.google.co.jp:80"/0/0/0 )'
   'drvAsynSerialPortConfigure( "変数名"/ "シリアルデバイス名" )', 'シリアルポート番号を変数に割り当てる．(e.g.) drvAsynSerialPortConfigure( "PS1"/ "/dev/ttyACM0" )'

