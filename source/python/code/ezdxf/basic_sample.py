import ezdxf

# -- 新規ファイルとモデルスペースを生成 -- #
doc = ezdxf.new()
msp = doc.modelspace()

# -- モデル：線分、円を追加 -- #
msp.add_line(start=(0, 0), end=(5, 0))
msp.add_circle(center=(2.5, 2.5), radius=2)

# -- dxfファイルとして保存 -- #
outFile = "basic_example.dxf"
doc.saveas( outFile )

print(" output :: {}".format( outFile ) )
