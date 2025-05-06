##############################################################
apt コマンド 備忘録
##############################################################

=========================================================
apt とは
=========================================================

`apt` は Debian系Linuxディストリビューション（Ubuntu, Debianなど）で使用される、パッケージ管理システムのコマンドラインツール．パッケージのインストール、アップデート、アンインストール、情報表示ができる．

主なコマンド例

::

  $ sudo apt update        # パッケージリストの更新
  $ sudo apt install <pkg> # パッケージのインストール
  $ sudo apt search <pkg>  # パッケージの検索

``apt`` は ``apt-get`` や ``apt-cache`` を統合し、ユーザーフレンドリーにしたもの．

|

=========================================================
aptの初期設定（プロキシ設定とsources.list）
=========================================================

---------------------------------------------------------
プロキシ設定
---------------------------------------------------------

プロキシ環境下で `apt` を使用する場合 、  :blue:`/etc/apt/apt.conf.d/80proxy` を設定する．例えば、::

   Acquire::ftp::proxy "ftp://proxy01.server.co.jp:8080"
   Acquire::ftp::proxy "ftp://proxy02.server.co.jp:8080"
   Acquire::http::proxy "ftp://proxy01.server.co.jp:8080"
   Acquire::http::proxy "ftp://proxy02.server.co.jp:8080"
   Acquire::https::proxy "ftp://proxy01.server.co.jp:8080"
   Acquire::https::proxy "ftp://proxy02.server.co.jp:8080"


|
  
---------------------------------------------------------
sources.list の確認と編集
---------------------------------------------------------

aptが参照するリポジトリは  :blue:`/etc/apt/sources.list` に記載．国内ミラーが高速のはず．::


  deb http://ftp.jaist.ac.jp/pub/Linux/ubuntu/ noble main restricted universe multiverse
  deb http://ftp.jaist.ac.jp/pub/Linux/ubuntu/ noble-updates main restricted universe multiverse
  deb http://ftp.jaist.ac.jp/pub/Linux/ubuntu/ noble-security main restricted universe multiverse
  

命令の意味は、::

  deb http://ftp.jaist.ac.jp/pub/Linux/ubuntu/ noble-security main restricted universe multiverse
  │   │                                      │              └─ パッケージのカテゴリ
  │   │                                      └─ Distribution(noble=24.04) + セクション
  │   └───────── リポジトリのURL(ミラーサーバ)
  └────── バイナリ(deb) / ソースコード (deb-src)


* deb はバイナリ、deb-src はソースコード
* noble, noble-updates, noble-security ( nobleはUbuntu 24.04, updates, securityはそのままの意味 )


|

=========================================================
apt の基本的な使用方法
=========================================================


.. csv-table:: 
   :header: "command", "description"
   :widths: 30, 70
   :width:  700px

   "sudo apt update", "パッケージリストを更新"
   "sudo apt upgrade", "インストール済みパッケージを最新化"
   ":blue:`sudo apt install <pkg>`", "指定したパッケージをインストール"
   "sudo apt remove <pkg>", "指定したパッケージを削除（設定ファイルは残る）"
   "sudo apt purge <pkg>", "パッケージと設定ファイルを完全に削除"
   "sudo apt autoremove", "不要になった依存パッケージを自動削除"
   "sudo apt clean", "ダウンロード済みのパッケージキャッシュを削除"
   "apt list --installed", "インストール済みパッケージ一覧を表示"
   "apt search <keyword>", "キーワードでパッケージを検索"
   "apt show <pkg>", "パッケージの詳細情報を表示"   

|
   
=========================================================
OS導入時のインストール推奨パッケージ
=========================================================


開発・運用の基本環境を整えるために、最初に以下のパッケージ群をインストールすることを推奨します::

  sudo apt update && sudo apt upgrade -y
  sudo apt install -y \
      build-essential
      curl \
      wget \
      git \
      unzip \
      zip \
      software-properties-common \
      lsb-release \
      apt-transport-https \
      htop \
      tree \
      ncdu \
      tmux \
      neofetch \
      fd-find \
      emacs \
      net-tools \
      openssh-server 

|

---------------------------------------------------------
python のインストール
---------------------------------------------------------

* apt install python でなく、 :blue:`pyenv推奨` ：

  - python のページに記載．
