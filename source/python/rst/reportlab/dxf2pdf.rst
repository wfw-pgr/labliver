##############################################################
 dxfファイルからpdfファイルへの変換コード
##############################################################

=========================================================
dxfファイルの問題点
=========================================================

* 多くのドロー系ツールにおいて、paperspaceが使用できない
* 特に、CorelDrawがpaperspaceが使用できない様子で、modelspaceに記載されたモデルデータを強制センタリングで中央寄せしてしまうらしく、所望の印刷範囲でdxfを生成できないことが問題の発端．
* 解決策として、dxf -> pdf の変換をして、ドロー系で一旦変換してから、印刷することにしようとしている．


=========================================================
変換コード
=========================================================

変換コードは下記

.. literalinclude:: ../../code/reportlab/dxf2pdf.py
   		    :caption:  dxf2pdf.py
   		    :language: python

