##############################################################
ショートカットキーの割当て
##############################################################

=========================================================
割当て命令
=========================================================

---------------------------------------------------------
global-set-key 命令
---------------------------------------------------------

* emacs内でのショートカットキーの割当は、 **global-set-key** を用いる．

::

   (global-set-key "\C-xt" 'align-regexp)

    
* 上記により、"\C-xt" に対して、 **align-regexp** 関数を割り当てた．


---------------------------------------------------------
定義関数への割当
---------------------------------------------------------

* 独自の関数 ( **defun** にて定義したもの ) についても、割当が可能である．例えば、

::

   (defun split-window-horizontally-n (num_wins)
     (interactive "p")
     (if (= num_wins 2)
         (split-window-horizontally)
       (progn
         (split-window-horizontally (- (window-width) (/ (window-width) num_wins)))
         (split-window-horizontally-n (- num_wins 1)))) )
   (global-set-key "\C-x#" '(lambda () (interactive) (split-window-horizontally-n 3)))


