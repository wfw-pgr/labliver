##############################################################
Tips - 小技 - (4) コードリスティングのスタイル変更
##############################################################

=========================================================
Qiita・chatGPTライクなリスティングスタイルへ変更
=========================================================

* 外観の変更
* 垂直スクロールバーの追加
* コピーボタンの追加

|

=========================================================
外観の変更
=========================================================

* custom.css に記載．

.. code-block:: css

   /* ------------------------------------------ */
   /* -- literalinclude, code-block スタイル  -- */
   /* ------------------------------------------ */
   div.highlight,
   div.highlight pre,
   pre.literal-block {
       position: relative;     /* copybtn位置制御のために必要な場合が多い */
       background: #1e1e1e ;
       color: #d4d4d4 ;
       font-family: Ricty, Consolas, Menlo, Monaco, "Courier New", monospace ;
       border-radius: 6px ;
       padding: 1em ;
       font-size: 0.95em ;
       line-height: 1.5 ;
       white-space: pre ;  /* 自動折り返し禁止 */
       box-sizing: border-box;
   }

|

=========================================================
垂直スクロールバーの追加
=========================================================

* custom.css に記載．

.. code-block:: css

   /* -------------------- */
   /* 横・縦スクロール対応 */
   /* -------------------- */
   div.highlight pre {
       overflow-x: auto ;
       overflow-y: auto ;
       max-height: 400px ;  /* 必要に応じて調整 */
       max-width: 100% ;
   }

|

=========================================================
コピーボタンの追加
=========================================================

---------------------------------------------------------
コピーボタン機能を **pip install**
---------------------------------------------------------

.. code-block:: bash
                  
   pip install sphinx-copybutton

|

---------------------------------------------------------
conf.pyへ設定追記
---------------------------------------------------------

.. code-block:: python

   # -- copy button -- #
   #
   #   need. -> $ pip install sphinx_copybutton   #
   #
   extensions += ['sphinx_copybutton']
   copybutton_prompt_text = r'>>> |\.\.\. |\$ '
   copybutton_prompt_is_regexp = True
   #
   # -- copy button -- #

|

---------------------------------------------------------
custom.cssへ設定追記
---------------------------------------------------------

.. code-block:: css

   /* ----------------- */
   /* コピーボタン 設定 */
   /* ----------------- */
   div.highlight .copybtn {
       /* -- */  
       /*  -- ボタン外観 -- */
       /* -- */  
       position: absolute;
       top: 16px;             /* 上からの位置        */
       right: 24px;           /* 右からの位置        */
       z-index: 10;           /* 重ね位置（最前面）  */
       background-color: aqua ;
       color: navy ;
       border: none;
       border-radius: 6px;
       padding: 3px 3px;      /* 内側余白サイズ      */
       font-size: 1.2em;      /* アイコンサイズ      */
       opacity: 0.4;          /* 1：透明, 0：不透明  */
       cursor: pointer;
       transition: background-color 0.3s, opacity 0.3s;
   }
   div.highlight .copybtn:hover {
       /* -- */  
       /* -- マウスホバー -- */
       /* -- */  
       background-color: aqua ;
       opacity: 0.8 ;
   }

|
