=========================================================
EPICSサーバの導入について
=========================================================

ここでは、EPICSサーバの初期設定、及び、基本動作テストについて記載する．

---------------------------------------------------------
環境
---------------------------------------------------------

以下の環境を想定する．

* IOCとして使用するPC： **Raspberry Pi 2 Model B**
* OS : Raspbian
* user名：epics
* EPICS導入ディレクトリ （環境変数$\{EPICS_BASE\}）： /home/epics/epics/epics-base/
  

---------------------------------------------------------
EPICS( epics-base ) のインストール
---------------------------------------------------------


epcis-baseのダウンロード及びインストール
=========================================================


* baseの本家ウェブサイト( https://docs.epics-controls.org/projects/how-tos/en/latest/getting-started/installation.html )に従う. ::

    $ git clone --recursive https://github.com/epics-base/epics-base.git
    $ cd epics-base
    $ make

    
環境変数の設定
=========================================================

* 以下を ${HOME}/.zshrc や ${HOME}/.bash_profile 等へ書き込む ::

    export EPICS_BASE=${HOME}/epics/epics-base
    export EPICS_HOST_ARCH=$(${EPICS_BASE}/startup/EpicsHostArch)
    export PATH=${EPICS_BASE}/bin/${EPICS_HOST_ARCH}:${PATH}

    
epics-baseのテスト
=========================================================

* 以下の、データベースファイル( **.dbファイル** ,example.db )を作成する． ::

    record(ai, "temperature:water")
    {
      field(DESC, "Water temperature in the fish tank")
    }

* 以下、コマンドにて実行する． ::

    $ softIoc -d example.db
    epics> 
    ( EPICSコンソールに入る．新規コンソールを立ち上げて、以下を実行. )
    $ caput temperature:water 22
    $ caget temperature:water
    

---------------------------------------------------------
その他、モジュールのインストール
---------------------------------------------------------

* EPICSサーバを使用する際に、ハードウェア機器に応じて、拡張モジュールを使用する事が多い．
* 導入するモジュールは例えば、以下．

  + ASYN (Asynchronous (非同期通信用モジュール)re2cが必要)
  + Stream Devices (バイトストリーム処理用モジュール：例えば1バイト文字列を利用した制御RS-232C等)
  + seq (シーケンサー, C言語ライクな状態記述言語によるプログラム)
  + devGpio ( Raspberry Pi のGPIO端子の制御用モジュール、主はエラーで動作できていない．)

* インストールは各websiteに従えば、問題なくインストール可能．

