#######################################################################
EPICSの備忘録
#######################################################################

=========================================================
EPICSとは
=========================================================

* EPICSは、PCから複数の制御機器を統括的に取り扱えるようにした制御用ミドルウェア、サーバ、命令群である．
* ユーザPCのソフトウェアとハードウェアをシームレスに接続できる環境を提供しうる．
* 開発元は、アルゴンヌ国立研究所．Open License (EPICS Open License)である．
* 公式の説明は以下の通り.

  
.. note::

  "EPICS is a set of Open Source software tools, libraries and applications developed collaboratively and used worldwide to create distributed soft real-time control systems for scientific instruments such as a particle accelerators, telescopes and other large scientific experiments."

  

---------------------------------------------------------
EPICSの特徴
---------------------------------------------------------

以下のようなシステムの制御を得意とする．

* 多数の機器がぶらさがった大規模システムを統括的に制御できる．
* 高速・リアルタイムな通信が可能
* 柔軟かつスケーラブルで、拡張が容易である．


  
=========================================================
本解説の構成
=========================================================

以下， **EPICS** について以下の構成で解説する．

.. toctree::
   :maxdepth: 1

   ../rst/basic_startup
   ../rst/vocabulary
   ../rst/commands
   ../rst/example1__httpRequest_to_Google
   ../rst/example2__arduino_ADConvertor
   ../rst/example3__arduino_LEDcontrol01
   ../rst/example4__arduino_LEDcontrol02



=========================================================
CSS (Control System Studio) を用いたGUI構築について
=========================================================

以下、**CSS** について、以下の構成で解説する．
   
.. toctree::
   :maxdepth: 1

   ../rst/css__startup
   ../rst/css__install
   ../rst/css__configure




   
=========================================================
References
=========================================================

* EPICS-controls ( newer version of website, https://epics-controls.org/ )
* EPICS ( older version of website, https://epics.anl.gov/ )
* EPICS Users JP ( KEK EPICS wiki,  https://cerldev.kek.jp/trac/EpicsUsersJP )
* その他資料リンク ( EPICS Users JP, https://cerldev.kek.jp/trac/EpicsUsersJP/wiki/intro )
* Getting-Started EPICS controls ( https://docs.epics-controls.org/projects/how-tos/en/latest/getting-started/installation.html )
* 参考ノート： "https://note.com/dev_associate/n/nfa4605c70f60", "https://note.com/dev_associate/n/nd886d700b10a"
* OPI/IOC通信時のポート番号、IPアドレスの設定 ( https://epics.anl.gov/EpicsDocumentation/AppDevManuals/ChannelAccess/cadoc_4.htm )
* Arduino-EPICS サンプル ( KEK-EPICS Users JP, https://cerldev.kek.jp/trac/EpicsUsersJP/wiki/epics/arduino/simpleRead )
* Github:inigoalonso/setup-epics-serial-arduino ( arduino-EPICS  https://gist.github.com/inigoalonso/99d9076c672661a4b821 )
* StreamDevice -protocol Files- ( https://paulscherrerinstitute.github.io/StreamDevice/protocol.html )
* Arduino PWM 制御 ( https://deviceplus.jp/arduino/how-to-control-led-with-arduino-pwm/ )
* EPICS Record Reference ( https://epics.anl.gov/base/R7-0/6-docs/RecordReference.html )
