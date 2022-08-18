##############################################################
基本動作例４： EPICS-Arduinoによる LED-PWM 調光制御
##############################################################

=========================================================
検証目標
=========================================================

* ハードウェア（Arduino）の出力状態をPWM制御する検証．

  
=========================================================
前提条件
=========================================================

* 前回同様．
* PWMでLEDを調光する．

  
=========================================================
Arduinoプログラム：（PWM 制御）の転送
=========================================================

* シリアル制御（USB）から、明るさ信号を送信し、PWM制御する．
* Arduino プログラムは以下である．

.. literalinclude:: ../code/pwmLED/pwmLED.ino
   :caption: arduino_LEDcontrol_02.ino
   :language: c


* pythonからの制御テストコードは以下である．

.. literalinclude:: ../code/pwmLED/test__pwmLED.py
   :caption: test__pwmLED.py
   :language: python


=========================================================
IOC構築
=========================================================

---------------------------------------------------------
IOC構築 / テスト の手順
---------------------------------------------------------

* アプリ名は、参考URL（下記）に従い、pwmLEDとする．
* また、.dbやレコード名などは、全てpwmLEDへ統一する．
* IOC-App 構築の手順は、以下である．

  1. **ベースアプリ** の作成．
  2. **configure/RELEASE** に共有するモジュールのインストールパスを追記．
  3. **"pwmLEDApp"** 内の データベース情報、及び、コンパイル用のMakefileへ追記する．
  4. **StreamDevice** 用の **プロトコル** を、 **protocols/pwmLED.proto** として作成する．
  5. IOC初期化スクリプト( **iocBoot/iocpwmLED/st.cmd** ) を編集し、実行可能とする．
  6. make 、及び、st.cmdの実行、camonitorにより、経時変化を観察する．

以下、上記手順について詳述する．


---------------------------------------------------------
1. ベースアプリの作成
---------------------------------------------------------

* makeBaseApp.plを用いたベースアプリの作成 ::

    $ mkdir -p ~/epics/app/pwmLED
    $ cd  ~/epics/app/pwmLED
    $ makeBaseApp.pl -t ioc pwmLED
    $ makeBaseApp.pl -i -t ioc pwmLED

    
---------------------------------------------------------
2. 共通コンパイル設定事項の編集 ( configure/RELEASE )
---------------------------------------------------------

* configure/RELEASEに、共通のコンパイル設定（モジュールの場所等、）を例えば以下のように記載する． ::

    ASYN   = /home/epics/epics/support/asyn
    STREAM = /home/epics/epics/support/StreamDevice

  
---------------------------------------------------------
3. データベースファイルとコンパイルの準備
---------------------------------------------------------

* データベース及び使用するモジュールの情報を記載し、${HOME}/epics/app/pwmLED/pwmLEDApp/Db/pwmLED.dbを作成する．

  .. literalinclude:: ../code/pwmLED/pwmLED.db
                      :caption: pwmLED.db
                      :language: shell
                      :linenos:

        
* データベースのコンパイル対象として、上記の"pwmLED.db"を追加． ::

    @ pwmLEDApp/Db/Makefile
    
    DB += pwmLED.db
    

* その他モジュールを利用する場合は、IOCの通信コードのコンパイルに使用するモジュール情報を、 "pwmLEDApp/src/Makefile" に記載し、コンパイルできるようにする． ::

    @ pwmLEDApp/src/Makefile
    
    pwmLED_DBD  += stream.dbd
    pwmLED_DBD  += asyn.dbd
    pwmLED_DBD  += drvAsynSerialPort.dbd

    pwmLED_LIBS += stream
    pwmLED_LIBS += asyn
    

---------------------------------------------------------
4. StreamDeviceの設定ファイル ( "protocol" )の作成
---------------------------------------------------------

* ディレクトリ "protocols"を作成し、StreamDeviceの入出力情報を記載する． ::

    $ mkdir $HOME/epics/app/pwmLED/protocols

  
  .. literalinclude:: ../code/pwmLED/pwmLED.proto
                      :caption: pwmLED.proto
                      :language: shell
                      :linenos:

    
---------------------------------------------------------
5. IOC 初期化スクリプト "st.cmd" の編集
---------------------------------------------------------

* IOC初期化スクリプト ( iocBoot/iocpwmLED/st.cmd ) に、以下の情報を記載する．
    
    .. literalinclude:: ../code/pwmLED/st.cmd
                        :caption: st.cmd
                        :language: shell
                        :emphasize-lines: 14,20,24,25

                
    .. warning::

       (隘路事項) dbLoadRecord, dbLoadDatabaseの順番が逆になったりすると、うまく動作しない．しかも、".db"ファイルの１行目がおかしいというエラーメッセージがでるので、ミスリーディングである．st.cmd前後の状態も確認すべきである．

                
* スクリプトに実行権限を与えておく． ::

    $ chmod u+x $HOME/epics/app/pwmLED/iocBoot/iocpwmLED/st.cmd

    
---------------------------------------------------------
6. make 及び、初期化スクリプト "st.cmd" の実行
---------------------------------------------------------

* ベースディレクトリにて make する． ::

    $ cd $HOME/epics/app/pwmLED/
    $ make distclean
    $ make

* 初期化スクリプトを実行する． ::

    $ cd $HOME/epics/app/pwmLED/iocBoot/iocpwmLED/
    $ sudo ./st.cmd


  
=========================================================
LEDのPWM制御状況の確認
=========================================================
    
---------------------------------------------------------
ローカルからのcamonitor
---------------------------------------------------------

* 別コンソールを立ち上げて、以下コマンドを実行 ::

    epics@raspberrypi: ~ $ caput epics:pwmLED 0   ( H も可 )
    epics@raspberrypi: ~ $ caput epics:pwmLED 10  ( H も可 )
    epics@raspberrypi: ~ $ caput epics:pwmLED 20  ( H も可 )
    epics@raspberrypi: ~ $ caput epics:pwmLED 240 ( H も可 )

* 明るさが変更されることを確認した．
  

---------------------------------------------------------
OPI（手元macOS）からのCA
---------------------------------------------------------

* pyEpicsからCA． ::

    $ python3
    >>> import epics
    >>> epics.caput( "epics:pwmLED",  10 )
    >>> epics.caput( "epics:pwmLED", 240 )
    

* OPIからIOCを介して、 **"LEDのPWM制御"** を実施することができた．


=========================================================
参考URL
=========================================================

* Arduino-EPICS サンプル ( KEK-EPICS Users JP, https://cerldev.kek.jp/trac/EpicsUsersJP/wiki/epics/arduino/simpleRead )
* Github:inigoalonso/setup-epics-serial-arduino ( arduino-EPICS  https://gist.github.com/inigoalonso/99d9076c672661a4b821 )
* StreamDevice -protocol Files- ( https://paulscherrerinstitute.github.io/StreamDevice/protocol.html )
* Arduino PWM 制御 ( https://deviceplus.jp/arduino/how-to-control-led-with-arduino-pwm/ )
