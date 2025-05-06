##############################################################
現状の init.el 構成
##############################################################

=========================================================
github.com にて確認
=========================================================

* https://github.com/wfw-pgr/emacs.d.settings/tree/main

|

=========================================================
ディレクトリ構成
=========================================================

::
   
   .emacs.d
   ├── auto-save-list
   ├── backups
   ├── elpa
   │   ├── archives
   │   └── init-loader-20250313.47
   ├── init.el
   ├── inits
   │   ├── 00-languages.el
   │   ├── 00-languages.elc
   │   ├── 10-basics.el
   │   ├── 10-basics.elc
   │   ├── 20-customs.el
   │   ├── 20-customs.elc
   │   ├── MAKE--invoke_build
   │   └── tasks.py
   ├── lisps
   │   └── yasnippet
   ├── modes
   │   ├── def-mode.el
   │   ├── elmer-mode.el
   │   ├── jsonc-mode.el
   │   ├── lua-mode.el
   │   ├── phits-mode.el
   │   ├── rst-extensions.el
   │   └── rst.el
   ├── snippets
   │   ├── c++-mode
   │   ├── f90-mode
   │   ├── latex-mode
   │   ├── python-mode
   │   ├── rst-mode
   │   └── sif-mode
   └── themes
   └── mytheme-theme.el


|

=========================================================
基本コードのリスティング
=========================================================

---------------------------------------------------------
init.el
---------------------------------------------------------

.. literalinclude:: codes/init.el
   		    :language: emacs-lisp
                               
|

---------------------------------------------------------
inits/00_language.el
---------------------------------------------------------

.. literalinclude:: codes/00-languages.el
   		    :language: emacs-lisp

|

---------------------------------------------------------
inits/10_basics.el
---------------------------------------------------------

.. literalinclude:: codes/10-basics.el
   		    :language: emacs-lisp
                       
|

---------------------------------------------------------
inits/20_customs.el
---------------------------------------------------------

.. literalinclude:: codes/20-customs.el
   		    :language: emacs-lisp

|
|

=========================================================
init.el の ビルド
=========================================================

.elc へコンパイルして使用しているため、ビルドを忘れない．

::

   $ cd  inits
   $ invoke build
