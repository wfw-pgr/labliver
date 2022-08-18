##############################################################
基本動作例３： EPICS-ArduinoによるLチカ (ON/OFF) 制御
##############################################################

=========================================================
検証目標
=========================================================

* ハードウェア（Arduino）の出力状態を遠隔制御する検証．

  
=========================================================
前提条件
=========================================================

* IOCは **"RaspberryPi"** 、OPIは手元PCのmacOS、制御機器は **"Arduino Uno"** ．
* Arduino-RaspberryPi間はUSB接続、RaspberryPi-mac間はLANケーブルで接続する．
* Arduinoの２番端子-GND端子間に 1KΩ抵抗x2個、LEDを直列に接続する．２番端子の出力によってLEDを点灯させる．
* 制御モジュールとして、 **"StremDevice"** を使用し、その他、 **asyn** , **"pyEpics"** を適宜使用する．
* 作業ディレクトリ： ${HOME}/epics/app/lightupLED/  ( ${HOME}=/home/epics/ )


  
=========================================================
Arduinoプログラム１：（Lチカ：ON/OFF制御）の転送
=========================================================

* シリアル制御（USB）から、ASCII文字を受け取り、文字に応じて以下の動作をする．
  + 文字が **"H"** ( ASCII:72 (10進数) ) であった場合LEDを **点灯** させる．
  + 文字が **"L"** ( ASCII:76 (10進数) ) であった場合LEDを **消灯** させる．

* Arduino プログラムは以下である．
* 下記プログラムは、**Arduino IDE** を使用してArduinoへ転送しておく．（手元PCからでも勿論、可）

.. literalinclude:: ../code/lightupLED/lightupLED.ino
   :caption: arduino_LEDcontrol01.ino
   :language: c

              
* pythonからの制御テストコードは以下である．

.. literalinclude:: ../code/lightupLED/test__lightupLED.py
   :caption: test__lightupLED.py
   :language: python

                   


=========================================================
IOC構築
=========================================================

---------------------------------------------------------
IOC構築 / テスト の手順
---------------------------------------------------------

* アプリ名は、参考URL（下記）に従い、lightupLEDとする．
* また、.dbやレコード名などは、全てlightupLEDへ統一する．
* IOC-App 構築の手順は、以下である．

  1. **ベースアプリ** の作成．
  2. **configure/RELEASE** に共有するモジュールのインストールパスを追記．
  3. **"lightupLEDApp"** 内の データベース情報、及び、コンパイル用のMakefileへ追記する．
  4. **StreamDevice** 用の **プロトコル** を、 **protocols/lightupLED.proto** として作成する．
  5. IOC初期化スクリプト( **iocBoot/ioclightupLED/st.cmd** ) を編集し、実行可能とする．
  6. make 、及び、st.cmdの実行、camonitorにより、経時変化を観察する．

以下、上記手順について詳述する．


---------------------------------------------------------
1. ベースアプリの作成
---------------------------------------------------------

* makeBaseApp.plを用いたベースアプリの作成 ::

    $ mkdir -p ~/epics/app/lightupLED
    $ cd  ~/epics/app/lightupLED
    $ makeBaseApp.pl -t ioc lightupLED
    $ makeBaseApp.pl -i -t ioc lightupLED

    
---------------------------------------------------------
2. 共通コンパイル設定事項の編集 ( configure/RELEASE )
---------------------------------------------------------

* configure/RELEASEに、共通のコンパイル設定（モジュールの場所等、）を例えば以下のように記載する． ::

    ASYN   = /home/epics/epics/support/asyn
    STREAM = /home/epics/epics/support/StreamDevice

  
---------------------------------------------------------
3. データベースファイルとコンパイルの準備
---------------------------------------------------------

* データベース及び使用するモジュールの情報を記載し、${HOME}/epics/app/lightupLED/lightupLEDApp/Db/lightupLED.dbを作成する．

  .. literalinclude:: ../code/lightupLED/lightupLED.db
                      :caption: lightupLED.db
                      :language: shell
                      :linenos:

        
* データベースのコンパイル対象として、上記の"lightupLED.db"を追加． ::

    @ lightupLEDApp/Db/Makefile
    
    DB += lightupLED.db
    

* その他モジュールを利用する場合は、IOCの通信コードのコンパイルに使用するモジュール情報を、 "lightupLEDApp/src/Makefile" に記載し、コンパイルできるようにする． ::

    @ lightupLEDApp/src/Makefile
    
    lightupLED_DBD  += stream.dbd
    lightupLED_DBD  += asyn.dbd
    lightupLED_DBD  += drvAsynSerialPort.dbd

    lightupLED_LIBS += stream
    lightupLED_LIBS += asyn
    

---------------------------------------------------------
4. StreamDeviceの設定ファイル ( "protocol" )の作成
---------------------------------------------------------

* ディレクトリ "protocols"を作成し、StreamDeviceの入出力情報を記載する． ::

    $ mkdir $HOME/epics/app/lightupLED/protocols

  
  .. literalinclude:: ../code/lightupLED/lightupLED.proto
                      :caption: lightupLED.proto
                      :language: shell
                      :linenos:

    
---------------------------------------------------------
5. IOC 初期化スクリプト "st.cmd" の編集
---------------------------------------------------------

* IOC初期化スクリプト ( iocBoot/ioclightupLED/st.cmd ) に、以下の情報を記載する．
    
    .. literalinclude:: ../code/lightupLED/st.cmd
                        :caption: st.cmd
                        :language: shell
                        :emphasize-lines: 14,20,24,25

                
    .. warning::

       (隘路事項) dbLoadRecord, dbLoadDatabaseの順番が逆になったりすると、うまく動作しない．しかも、".db"ファイルの１行目がおかしいというエラーメッセージがでるので、ミスリーディングである．st.cmd前後の状態も確認すべきである．

                
* スクリプトに実行権限を与えておく． ::

    $ chmod u+x $HOME/epics/app/lightupLED/iocBoot/ioclightupLED/st.cmd

    
---------------------------------------------------------
6. make 及び、初期化スクリプト "st.cmd" の実行
---------------------------------------------------------

* ベースディレクトリにて make する． ::

    $ cd $HOME/epics/app/lightupLED/
    $ make distclean
    $ make

* 初期化スクリプトを実行する． ::

    $ cd $HOME/epics/app/lightupLED/iocBoot/ioclightupLED/
    $ sudo ./st.cmd


  
=========================================================
ADCの動作状況の確認
=========================================================
    
---------------------------------------------------------
ローカルからのcamonitor
---------------------------------------------------------

* 別コンソールを立ち上げて、以下コマンドを実行 ::

    epics@raspberrypi: ~ $ caput epics:lightupLED "H"      ( H も可 )


---------------------------------------------------------
OPI（手元macOS）からのCA
---------------------------------------------------------

* pyEpicsからCA． ::

    $ python3
    >>> import epics
    >>> epics.caput( "epics:lightupLED", "H" )
    

* OPIからIOCを介して、 **"Lチカ"** を実施することができた．


=========================================================
参考URL
=========================================================

* Arduino-EPICS サンプル ( KEK-EPICS Users JP, https://cerldev.kek.jp/trac/EpicsUsersJP/wiki/epics/arduino/simpleRead )
* Github:inigoalonso/setup-epics-serial-arduino ( arduino-EPICS  https://gist.github.com/inigoalonso/99d9076c672661a4b821 )
* StreamDevice -protocol Files- ( https://paulscherrerinstitute.github.io/StreamDevice/protocol.html )
