##############################################################
one-API の intel Fortran のインストールについて
##############################################################

=========================================================
one-APIの intel Fortran
=========================================================

* 2023年2月現在、 **one-API** 内の **intel Fortran compiler** ( **intel C compiler** も )が無料で利用できる．
* インストールは種々の方法があるが、unix-likeな aptを利用したインストール方法について、記載する．
* 手法は、HPに記載の手法で問題なく入った．( Ubuntu20.04, WSL2 )

  
=========================================================
apt鍵のダウンロード、及び、登録
=========================================================

* wgetのプロキシの解除 ( ~/.wgetrc にプロキシサーバ及びユーザ名・パスワードを記載 )
* apt 鍵の取得 ::

  $ sudo apt-get install -y gpg-agent wget
  $ wget -O- https://apt.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS.PUB \ | gpg --dearmor | sudo tee /usr/share/keyrings/oneapi-archive-keyring.gpg > /dev/null


* apt sources.listへの追加． ::

  $ echo "deb [signed-by=/usr/share/keyrings/oneapi-archive-keyring.gpg] https://apt.repos.intel.com/oneapi all main" | sudo tee /etc/apt/sources.list.d/oneAPI.list

* aptの更新 ::

  $ sudo apt update

=========================================================
apt を用いたインストール
=========================================================

* aptでアクセスできるようになっているので、通常のインストールが可能． ::

  $ sudo apt install intel-basekit intel-hpckit

* 2 個めのhpckitが **intel compiler**



=========================================================
パスの設定 (  )
=========================================================

* pathが通ってないので、以下を読み込む．( .bash_profileに書き込んでおく ) ::

  $ source /opt/intel/oneapi/setvars.sh

=========================================================
Reference
=========================================================

* Intel oneAPI Toolkits - Free for All Developers ( https://www.intel.com/content/www/us/en/developer/articles/news/free-intel-software-developer-tools.html )
* intel oneAPI apt install ( https://www.intel.com/content/www/us/en/developer/tools/oneapi/base-toolkit-download.html?operatingsystem=linux&distributions=aptpackagemanager ) 
