;; ========================================================= ;;
;; === .sif mode Emacs Major Mode                        === ;;
;; ========================================================= ;;

;; -- generic mode として定義                    -- ;;
(require 'generic-x)

;; -- リストインターリーブ関数の定義             -- ;;
(defun list-interleave (ls res inserting)
  (cond
   ((not ls)  (reverse res))
   ((not res) (list-interleave (cdr ls) (cons (car ls) res) inserting))
   (t (list-interleave
       (cdr ls)
       (cons (car ls) (cons inserting res))
       inserting))))

;; -- .sif 変数型群の定義 ( 変数グループの定義 ) -- ;;
(defvar sif-variables-type-operators
  (apply 'concat (list-interleave
                  '("String" "Real" "Logical" "Integer" "None")
                  '() "\\|")))

;; -- .sif 読み込み時の動作を指定する関数        -- ;;
(defun sif-initial-call ()
  '( (setq indent-tabs-mode nil)
     (setq tab-width 2)
     )
  )

;; ------------------------------------------------ ;;
;; -- .sif Major Mode の定義                     -- ;;
;; ------------------------------------------------ ;;

;; -- generic-mode 名 :: sif-mode                -- ;;
(define-generic-mode 'sif-mode
  ;; 1. コメント行の印
  '("!" "#")
  ;; 2. とりあえずハイライトするキーワード群     -- ;;
  '("Header" "Constants" "Material" "End" "Solver" "Boundary Condition"
    "Simulation" "Body" "Body Force" "Initial Condition" "Equation" "Components")
  ;; 3. 詳細な区別でハイライトするキーワード群   -- ;;
  `( ("\sw"
      . font-lock-string-face)
     (,sif-variables-type-operators
      . font-lock-type-face)
     )
  ;; -- 3.1 :: ダブルクォーテーションされた文字 :: string-face として表示 -- ;;
  ;; -- 3.2 :: 上の関数に示した文字列           :: type-face   として表示 -- ;;
  ;; -- 
  ;; 4. file name ( 拡張子の指定 => \\.***$ )
  '("\\.sif$")
  ;; 5. hook function ( 起動時に実行する関数 無ければ nil, もしくは、上記関数で定義． )
  '( sif-initial-call )
  ;; 6. explanation   ( モードの説明書、呼び出された時になんて表示されるか． )
  "sif mode for elmer FEM environment"
  )

;; ------------------------------------------------ ;;
;; -- 拡張子との連想                             -- ;;
;; ------------------------------------------------ ;;

;; (add-to-list 'auto-mode-alist '("\\.sif\\'" . sif-mode))
