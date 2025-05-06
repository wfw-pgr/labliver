##############################################################
日本語環境設定（Emacs + ibus + mozc, WSLg GUI対応）
##############################################################

WSLg 環境上の Emacs（GUI）で日本語入力の設定をまとめた．


=========
概要
=========


- WSL2 + WSLg + Ubuntu 24.04 環境
- Emacs（GUI）での日本語入力
- IMフレームワークとして `ibus + mozc` を使用
- Emacs では `mozc.el` を介して IME を制御
- macOS風の切り替え方式（無変換=英数、変換=かな）
- Mozc の変換キー処理を無効化（GUIからの変更）
- Emacs Lisp による切替制御を実装
- Mozc GUI のキーマップ設定には癖あり：マウス非対応


---------------------------------------------------------
IME の選定理由（ibus + mozc）
---------------------------------------------------------

- GUIアプリとの互換性が高い（GTKベース）
- `fcitx5` より設定が簡潔かつ安定
- Mozc の設定も `ibus-setup` で直感的に操作可能
- Emacs 側で制御しやすい


=========================================================
設定手順
=========================================================

1. ibus + mozc のインストール::

    sudo apt install ibus ibus-mozc mozc-utils-gui

2. IM 関連の環境変数を .zprofile に設定::

    export GTK_IM_MODULE=ibus
    export QT_IM_MODULE=ibus
    export XMODIFIERS="@im=ibus"

3. ibus を起動::

    ibus-daemon -drx

4. ibus-setup にて Mozc を追加::

    ibus-setup

    - Mozc を追加 ( Input Method )
    - Input Method - Mozc - Preferences - キーの設定 - 編集
    - 無変換 / 変換 に対する動作を解除または IMEの無効化/有効化に設定．
    - 変換 ( 変換前入力中 ) は「確定」に設定（ダミー化） 
      


=========================================================
Emacs 側の設定（mozc.el + キーバインド）
=========================================================

以下を `init.el` に追加することで、macOS風の入力切替を実現


::
   
   (defun my-ime-on ()
     (interactive)
     (unless current-input-method
     (toggle-input-method))
   )
   
   (defun my-ime-off ()
     (interactive)
     (when current-input-method
     (deactivate-input-method))
   )
   (global-set-key [henkan]   'my-ime-on)
   (global-set-key [muhenkan] 'my-ime-off)

    

=========================================================
Mozc GUI のキーマップ変更方法
=========================================================


Mozc のキーマップ編集画面はマウス操作が効かないため、以下のキーボード操作で行う::

- 矢印キー：項目の移動
- Space：モード切り替え／選択肢表示（2回押す）
- Enter：決定
- Delete：割り当て削除（Mozcのバージョンによる）

特に「無変換」「変換」キーに `InputModeLatin` や `InputModeHiragana` が割り当てられている場合は、
削除または「確定」に置き換えることで Emacs 側の制御を優先できる。



=========================================================
まとめ
=========================================================

- Emacs での日本語入力には `ibus + mozc` 、実際はemacs内の mozc.el を利用
- macOS風の設定、IME GUI設定には癖があるので、操作注意．
- Mozc のキー設定を整理すれば、`Henkan` / `Muhenkan` による IME 切替が可能
