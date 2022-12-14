##############################################################
Git/GitHubの基本の使用方法
##############################################################


=========================================================
初期アカウント設定
=========================================================

* ローカル / グローバルのユーザ情報設定 ::

  $ git config --global user.name  "wfw-pgr"
  $ git config --global user.email xxx[at]gmail.com


=========================================================
Git 管理の開始
=========================================================

---------------------------------------------------------
リモートレポジトリの設定
---------------------------------------------------------

* GitHub ( webサイト上 ) で， **リモートレポジトリを作成** する．
* 手順は以下．

  1. サインイン
  2. Repositories タブをクリック．
  3. ( New ) ボタンをクリック. 
  4. レポジトリ名の設置、Private/Publicの設定 や Descriptionの記載、など．
  5. 以下、サイトのコマンド例に従って操作．


---------------------------------------------------------
ローカルレポジトリの設定
---------------------------------------------------------

* Git管理の対象ディレクトリにて、ローカルレポジトリの設定コマンド（以下）を実行する．
* 対象ディレクトリ以下は、 **全てGit管理の対象** となる ( **".gitignore" 記載のファイル以外** )． ::

  $ git init ( 初期セットアップ )
  $ git add ./* ( Git管理対象リストへ追加 )
  $ git commit -m " add comment :: first commit." ( Gitへ登録 )
  $ git remote add origin https://github.com/wfw-pgr/xxx.git ( リモートブランチ"origin"としてURLを設定 )
  $ git branch -M main ( 現在のブランチ("master")を"main"へ名称変更 )
  $ git push -u origin master ( ローカルブランチの状態をリモートレポジトリへ転送 )


=========================================================
Git管理ファイルの更新
=========================================================

* ローカルレポジトリにおける管理では、追加・変更ファイルを登録・更新し( **"git add"** )、 確定した変更としてコメント付きで登録する ( **git commit** )．
* リモートレポジトリに変更を反映する際は、更新をプッシュする ( **"git push"** )．
* （更新例） ::

  $ git add ./
  $ git commit -m "update files."
  $ git push origin main
   

   
===============================================================
GitHubのリモートレポジトリのローカルへのコピー ("git clone")
===============================================================

* GitHubからのダウンロード（自他ともに可能）． ( レポジトリのコピー＝[クローン] ("git clone") ) ::
  
  $ git clone https://github.com/wfw-pgr/xxx.git

   
===============================================================
GitHubのリモートレポジトリの更新内容を取得する ("git pull")
===============================================================

* GitHubからの更新取得（自他ともに可能）． ::
   
  $ git clone https://github.com/wfw-pgr/xxx.git



===============================================================
ブランチの作成、切替え、削除
===============================================================

* ローカルブランチの作成、切替 ::

  $ git branch    ( 既存ブランチの表示 )  
  $ git branch dev   ( 別ブランチ"dev"を作成 )
  $ git checkout dev    ( 別ブランチ"dev" への切り替え )

* ローカルブランチの削除 ::

  $ git branch -d dev


===============================================================
ブランチのマージ
===============================================================
   
* ファイル変更後の更新 ( ブランチ"dev"にて変更後、変更を登録する ) ::
   
  $ git add ./     ( 追加・変更ファイルのローカルブランチ"dev"のリストへ追加 ) 
  $ git commit -m "add new function."  ( ローカルブランチ"dev"へコミット(最終登録決定) ) 

   
* ブランチ"dev"の更新内容をメインブランチ("main")へ反映． ::

  $ git checkout main
  $ git merge dev
  $ git branch -d dev
