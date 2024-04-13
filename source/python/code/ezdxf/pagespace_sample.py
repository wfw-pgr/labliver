import sys
import ezdxf

# -- コーディング用設定 -- #
w_, h_    = 0, 1

# -- パラメータ設定 -- #
a4_width  = 210
a4_height = 297
radius    = 60
size      = ( a4_width, a4_height )
center    = ( 0.4*a4_width, 0.6*a4_height )

# -- 出力ファイル名 -- #
outFile   = "dxf/pagespace_sample.dxf"

# -- 新しい.dxfファイルを作成 -- #
doc       = ezdxf.new()
msp       = doc.modelspace()

# -- model を描く（modelspaceへ） -- #
msp.add_circle( center=center, radius=radius )

# -- Layout を設定 ( page_setupが肝要 ) -- #
lo      = doc.layout()
sp      = lo.page_setup( size=size, margins=(0,0,0,0) )
vp      = lo.add_viewport( center=center, view_center_point=center, \
                           size=size, view_height=size[h_] )

# -- .dxf ファイルとして保存 -- #
doc.saveas( outFile )
print( "[pagespace_sample.py] outFile :: {} ".format( outFile ) )

