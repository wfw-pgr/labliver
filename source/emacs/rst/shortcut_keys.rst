##############################################################
ショートカットキーについて
##############################################################

=========================================================
ショートカットキーの割り当て方
=========================================================

* emacs内でのショートカットキーの割当は、 **global-set-key** を用いる． ::

    (global-set-key "\C-xt" 'align-regexp)

    
* 上記により、"\C-xt" に対して、 **align-regexp** 関数を割り当てた．
* 独自の関数 ( **defun** にて定義したもの ) についても、割当が可能である．例えば、 ::

    (defun split-window-horizontally-n (num_wins)
      (interactive "p")
      (if (= num_wins 2)
          (split-window-horizontally)
        (progn
          (split-window-horizontally
           (- (window-width) (/ (window-width) num_wins)))
          (split-window-horizontally-n (- num_wins 1)))))
    (global-set-key "\C-x#" '(lambda ()
                               (interactive)
                               (split-window-horizontally-n 3)))

  

=========================================================
割当ショートカットについて
=========================================================

例えば、以下のような関数を割り当てるとよい．::

    (global-set-key "\C-xt" 'align-regexp)
