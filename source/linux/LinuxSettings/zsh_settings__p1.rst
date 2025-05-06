##############################################################
zsh (1)
##############################################################

=========================================================
zsh とは
=========================================================

* zsh は、  :red:`高機能で柔軟な設定が可能なシェル`
* bashに比べて、  :blue:`補完機能` や  :blue:`プロンプトカスタマイズ` が容易で、  :blue:`ユーザーフレンドリー`


=========================================================
zsh のインストール
=========================================================

以下のコマンドで zsh をインストールする：

.. code-block:: bash

   sudo apt update
   sudo apt install -y zsh

インストール後、以下のコマンドで zsh をデフォルトシェルに変更できる：

.. code-block:: bash

   chsh -s $(which zsh)

   
* WSLの場合、`chsh` の変更が反映されない場合があるため、`.bashrc` に `exec zsh` を追記する方法もあり．


=========================================================
oh-my-zsh による拡張
=========================================================

* zsh の機能強化に、 `oh-my-zsh` の導入が一般的．以下のコマンドでインストール可能：

.. code-block:: bash

   sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

   
* インストール後、`~/.zshrc` が自動生成される。

  
|
  
---------------------------------------------------------
プロンプトテーマや補完の設定
---------------------------------------------------------

`~/.zshrc` 内の `ZSH_THEME` 変数を変更することで、プロンプトの見た目を変更できる。例：

.. code-block:: bash

   ZSH_THEME="robbyrussell"

軽量でシンプルなプロンプトが好みの場合は `"bira"` や `"agnoster"` の代わりに `"minimal"` などを使用するのもよい。

補完機能やヒストリ検索を有効にするには、以下のプラグインが便利：

.. code-block:: bash

   plugins=(git z sudo history-substring-search)

設定変更後は、zsh を再起動するか、`source ~/.zshrc` により反映する。

|

---------------------------------------------------------
zsh-completions の導入
---------------------------------------------------------

* zsh-completionsは、zshはの強力な補完機能を深化する．

  
インストール手順
---------------------

1. oh-my-zsh を使用する場合、`custom/plugins` 以下にダウンロード：

.. code-block:: bash

   $ git clone https://github.com/zsh-users/zsh-completions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-completions

   
2. `.zshrc` の `plugins` に `zsh-completions` を追加：

.. code-block:: bash

   plugins=(git zsh-completions)


3. 読み込み
   
.. code-block:: bash
                
   $ source ~/.zshrc
   

注意点と補足
-------------------

- `compinit` を再実行した際に「insecure completion-dependent directories」エラーが出ることがある。
  その場合は `~/.zsh/zsh-completions` 以下のパーミッションを `755` に修正する。

  .. code-block:: bash

     chmod -R 755 ~/.zsh/zsh-completions

- 補完が機能しない場合は `compaudit` を実行し、問題のあるディレクトリやファイルを確認することが推奨される。




---------------------------------------------------------
zsh の利点とまとめ
---------------------------------------------------------

- zsh は **高機能で柔軟な設定が可能なシェル**
- `oh-my-zsh` の導入により、テーマや機能をすぐに活用できる．

  
