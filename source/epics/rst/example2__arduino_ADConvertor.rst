##############################################################
基本動作例２： ArduinoのAD変換端子からの入力読取り
##############################################################

=========================================================
検証目標
=========================================================

* ハードウェア（Arduino）を遠隔制御する検証．

  
=========================================================
前提条件
=========================================================

* IOCは **"RaspberryPi"** 、OPIは手元PCのmacOS、制御機器は **"Arduino Uno"** ．
* Arduino-RaspberryPi間はUSB接続、RaspberryPi-mac間はLANケーブルで接続する．
* Arduinoの5V-GND端子間に 1KΩ抵抗x2個、さらにLEDを直列に接続し、さらに抵抗の中間地点に Arduino A0端子を接続する．A0から、A/D変換(ADC)によってデジタル値に変換した値を読み取る．
* 制御モジュールとして、 **"StremDevice"** を使用する．
* その他、 **asyn** , **"pyEpics"** を適宜使用する．
* 作業ディレクトリ： ${HOME}/epics/app/simpleRead/  ( ${HOME}=/home/epics/ )


  
=========================================================
Arduinoプログラム（ADC )の転送
=========================================================

* Arduino プログラムは以下である．

.. literalinclude:: ../code/arduino_ADConvertor.ino
   :caption: A Arduino program to measure the voltage between 2 registers.
   :language: c

              
* 上記プログラムは、**Arduino IDE** を使用してArduinoへ転送しておく．（手元PCからでも勿論、可）


=========================================================
IOC構築
=========================================================

---------------------------------------------------------
IOC構築 / テスト の手順
---------------------------------------------------------

* アプリ名は、参考URL（下記）に従い、simpleReadとする．
* また、.dbやレコード名などは、全てsimpleReadへ統一する．
* IOC-App 構築の手順は、以下である．

  1. **ベースアプリ** の作成．
  2. **configure/RELEASE** に共有するモジュールのインストールパスを追記．
  3. **"simpleReadApp"** 内の データベース情報、及び、コンパイル用のMakefileへ追記する．
  4. **StreamDevice** 用の **プロトコル** を、 **protocols/simpleRead.proto** として作成する．
  5. IOC初期化スクリプト( **iocBoot/iocsimpleRead/st.cmd** ) を編集し、実行可能とする．
  6. make 、及び、st.cmdの実行、camonitorにより、経時変化を観察する．

以下、上記手順について詳述する．


---------------------------------------------------------
1. ベースアプリの作成
---------------------------------------------------------

* makeBaseApp.plを用いたベースアプリの作成 ::

    $ mkdir -p ~/epics/app/simpleRead
    $ cd  ~/epics/app/simpleRead
    $ makeBaseApp.pl -t ioc simpleRead
    $ makeBaseApp.pl -i -t ioc simpleRead

    
---------------------------------------------------------
2. 共通コンパイル設定事項の編集 ( configure/RELEASE )
---------------------------------------------------------

* configure/RELEASEに、共通のコンパイル設定（モジュールの場所等、）を例えば以下のように記載する． ::

    ASYN   = /home/epics/epics/support/asyn
    STREAM = /home/epics/epics/support/StreamDevice

  
---------------------------------------------------------
3. データベースファイルとコンパイルの準備
---------------------------------------------------------

* データベース及び使用するモジュールの情報を記載し、${HOME}/epics/app/simpleRead/simpleReadApp/Db/simpleRead.dbを作成する．

  .. literalinclude:: ../code/simpleRead.db
                      :caption: simpleRead.db
                      :language: shell
                      :linenos:

        
* データベースのコンパイル対象として、上記の"simpleRead.db"を追加． ::

    @ simpleReadApp/Db/Makefile
    
    DB += simpleRead.db
    

* その他モジュールを利用する場合は、IOCの通信コードのコンパイルに使用するモジュール情報を、 "simpleReadApp/src/Makefile" に記載し、コンパイルできるようにする． ::

    @ simpleReadApp/src/Makefile
    
    simpleRead_DBD  += stream.dbd
    simpleRead_DBD  += asyn.dbd
    simpleRead_DBD  += drvAsynSerialPort.dbd

    simpleRead_LIBS += stream
    simpleRead_LIBS += asyn
    

---------------------------------------------------------
4. StreamDeviceの設定ファイル ( "protocol" )の作成
---------------------------------------------------------

* ディレクトリ "protocols"を作成し、StreamDeviceの入出力情報を記載する． ::

    $ mkdir $HOME/epics/app/simpleRead/protocols

  
  .. literalinclude:: ../code/simpleRead.proto
                      :caption: simpleRead.proto
                      :language: shell
                      :linenos:

    
---------------------------------------------------------
5. IOC 初期化スクリプト "st.cmd" の編集
---------------------------------------------------------

* IOC初期化スクリプト ( iocBoot/iocsimpleRead/st.cmd ) に、以下の情報を記載する．
    
    .. literalinclude:: ../code/simpleRead_st.cmd
                        :caption: st.cmd
                        :language: shell
                        :emphasize-lines: 14,20,24,25

                
    .. warning::

       (隘路事項) dbLoadRecord, dbLoadDatabaseの順番が逆になったりすると、うまく動作しない．しかも、".db"ファイルの１行目がおかしいというエラーメッセージがでるので、ミスリーディングである．st.cmd前後の状態も確認すべきである．

                
* スクリプトに実行権限を与えておく． ::

    $ chmod u+x $HOME/epics/app/simpleRead/iocBoot/iocsimpleRead/st.cmd

    
---------------------------------------------------------
6. make 及び、初期化スクリプト "st.cmd" の実行
---------------------------------------------------------

* ベースディレクトリにて make する． ::

    $ cd $HOME/epics/app/simpleRead/
    $ make distclean
    $ make

* 初期化スクリプトを実行する． ::

    $ cd $HOME/epics/app/simpleRead/iocBoot/iocsimpleRead/
    $ sudo ./st.cmd

    
* make 完了後の最終的なディレクトリツリーは以下．

.. literalinclude:: ../code/DirectoryTree_ex2_arduino_ADC.tree
   :caption: Directory tree after compilation.
   :language: shell


  
=========================================================
ADCの動作状況の確認
=========================================================
    
---------------------------------------------------------
ローカルからのcamonitor
---------------------------------------------------------

* 別コンソールを立ち上げて、以下コマンドを実行 ::

    epics@raspberrypi: ~ $ camonitor epics:simpleRead


---------------------------------------------------------
OPI（手元macOS）からのCA
---------------------------------------------------------

* pyEpicsからCA． ::

    $ python3
    >>> import epics
    >>> epics.caget    ( "epics:simpleRead" )
    >>> epics.camonitor( "epics:simpleRead" )
    

* OPIからIOCを介して、制御( 電圧モニタ ) を実施することができた．


=========================================================
参考URL
=========================================================

* Arduino-EPICS サンプル ( KEK-EPICS Users JP, https://cerldev.kek.jp/trac/EpicsUsersJP/wiki/epics/arduino/simpleRead )
