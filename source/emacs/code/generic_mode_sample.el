;;; ========================================================================= ;;;
;;;   Elmer-mode ( .sif )       to edit .sif parameter files in Elmer         ;;;
;;; ========================================================================= ;;;
;; see https://uid0130.blogspot.com/2014/05/emacsgeneric-mode.html 

;; ------------------------------------------------------------------- ;;
;; ---  [1]   call generic-x mode.                                 --- ;;
;; ------------------------------------------------------------------- ;;
(require 'generic-x)

;; ------------------------------------------------------------------- ;;
;; ---  [2] リストインターリーブ関数の定義                          -- ;;
;; ------------------------------------------------------------------- ;;
(defun list-interleave (ls res inserting)
  (cond
   ((not ls)  (reverse res))
   ((not res) (list-interleave (cdr ls) (cons (car ls) res) inserting))
   (t (list-interleave
       (cdr ls)
       (cons (car ls) (cons inserting res))
       inserting))))

;; ------------------------------------------------------------------- ;;
;; ---  [3] リストインターリーブ関数を使用したキーワード群の定義    -- ;;
;; ------------------------------------------------------------------- ;;
;; -- 変数型群01 -- ;;
(defvar elmer-type-keywords01
  (apply 'concat (list-interleave
                  '("[Ss]tring" "[Rr]eal" "[Ll]ogical" "[Ii]nteger")
                  '() "\\|")))
;; -- 変数型群02 -- ;;
(defvar elmer-type-keywords02
  (apply 'concat (list-interleave
                  '("[Tt]rue" "[Ff]alse" "[Nn]one")
                  '() "\\|")))

;; --  演算子群01 -- ;;
(defvar elmer-operator-keywords01
  (apply 'concat (list-interleave
                  '("=" "(" ")" "<" ">")
                  '() "\\|")))
;; --  演算子群02 -- ;;
(defvar elmer-operator-keywords02
  (apply 'concat (list-interleave
                  '("#" "@.*" "\\$.*" )
                  '() "\\|")))
;; --  演算子群03 -- ;;
(defvar elmer-operator-keywords03
  (apply 'concat (list-interleave
                  '("!")
                  '() "\\|")))

;; --  セクション表題 01 -- ;;
(defvar elmer-section-keywords01
  (apply 'concat (list-interleave
                  '("^[Ee][Nn][Dd]" "^[Hh]eader" "^[Ss]imulation" "^[Cc]onstants"
                    "^[Ss]olver" "^[Bb]ody" "^[Ee]quation" "^[Mm]aterial"
                    "^[Bb]oundary [Cc]ondition" "^[Ii]nitial Condition" "^[Bb]ody [Ff]orce"
                    )
                  '() "\\|")))


;; ------------------------------------- ;;
;; --- [2]   define font-lock face   --- ;;
;; ------------------------------------- ;;
(defface font-lock-operator01
  '((t (:foreground "green")))  "Comment:: Font faces for operator01" )

(defface font-lock-operator02
  '((t (:foreground "pink")))   "Comment:: Font faces for operator02" )

(defface font-lock-operator03
  '((t (:foreground "blue1")))  "Comment:: Font faces for operator03" )

(defface font-lock-type01
  '((t (:foreground "grey")))   "Comment:: Font faces for type"       )

(defface font-lock-type02
  '((t (:foreground "orange"))) "Comment:: Font faces for type"       )

(defface font-lock-section01
  '((t (:foreground "yellow")))   "Comment:: Font faces for section"    )

(define-generic-mode 'elmer-mode    ;; name of the mode to create
  '("!!" "#" )                      ;; comments start with '!!'
  kw_list_elmer_mode                ;; Main Highlights. Defined as below ( must be unique name. )
  `(                                ;; back-quatation is needed here !!!!
    ;; Detailed Highlights..
    (,elmer-type-keywords01     . 'font-lock-type01    )
    (,elmer-type-keywords02     . 'font-lock-type02    )
    (,elmer-operator-keywords01 . 'font-lock-operator01)
    (,elmer-operator-keywords02 . 'font-lock-operator02)
    (,elmer-operator-keywords03 . 'font-lock-operator03)
    (,elmer-section-keywords01  . 'font-lock-section01 )
    )
  '("\\.sif$")                      ;; files for which to activate this mode 
  (setq-default tab-width 2 indent-tabs-mode nil) ;; other functions to call
  "A mode for elmer .sif files"     ;; doc string for this mode
  )

(setq kw_list_elmer_mode '( "define" "include" "postProcess" "filepath" ) )

(provide 'elmer-mode)
