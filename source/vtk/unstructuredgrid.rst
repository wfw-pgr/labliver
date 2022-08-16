=========================================================
UnstructuredGridの記述
=========================================================

UnstructuredGrid の例
======================================

xml形式のデータファイルは以下の通り．

.. literalinclude:: code/unstruc_sample_show.vtu
   :language: xml

.. image:: image/screenshot_unstruc_ParaView_sample.png
   :scale: 30%
   :align: center

        
UnstructuredGrid 出力用クラス
======================================

* 以下の引数をとる．

  + Data= [nElem]
  + Elem= [nElem,nVerts]
  + Node= [nNode,3]
  + VectorData= *True* or *False*
  + vtkFile= *FileName*
  
    
.. literalinclude:: code/makeUnstructuredGrid.py
   :language: python
