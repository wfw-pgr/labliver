import numpy as np
import nkUtilities.plot1D         as pl1
import nkUtilities.load__config   as lcf
import nkUtilities.configSettings as cfs

x_,y_                    = 0, 1

# ------------------------------------------------- #
# --- [1] load data file                        --- #
# ------------------------------------------------- #
import nkUtilities.load__pointFile as lpf
inpFile1 = "dat/cs__Ra226_ng.dat"
inpFile2 = "dat/cs__Ra226_n2n.dat"
Data1    = lpf.load__pointFile( inpFile=inpFile1, returnType="point" )
Data2    = lpf.load__pointFile( inpFile=inpFile2, returnType="point" )
print( np.min( Data1[:,x_] ), np.max( Data1[:,x_] ) )
print( np.min( Data1[:,y_] ), np.max( Data1[:,y_] ) )
print( np.min( Data2[:,x_] ), np.max( Data2[:,x_] ) )
print( np.min( Data2[:,y_] ), np.max( Data2[:,y_] ) )

pngFile                  = "png/cs__Ra226.png"
config                   = lcf.load__config()
config                   = cfs.configSettings( configType="plot.def", config=config )
config["FigSize"]        = (6.0,6.0)
config["plt_position"]   = [ 0.16, 0.16, 0.94, 0.94 ]
config["plt_xAutoRange"] = False
config["plt_yAutoRange"] = False
config["plt_xRange"]     = [ +1.e-3, +1.e8 ]
config["plt_yRange"]     = [ +1.e-5, +1.e4 ]
config["xMajor_Nticks"]  = 11
config["yMajor_Nticks"]  = 9
config["plt_marker"]     = "none"
config["plt_markersize"] = 0.0
config["plt_linestyle"]  = "-"
config["plt_linewidth"]  = 0.8
config["plt_xlog"]       = True
config["plt_ylog"]       = True
config["xTitle"]         = "Energy (eV)"
config["yTitle"]         = "Cross section (b)"

# ------------------------------------------------- #
# --- [3] plot                                  --- #
# ------------------------------------------------- #
fig     = pl1.plot1D( config=config, pngFile=pngFile )
fig.add__plot( xAxis=Data1[:,x_], yAxis=Data1[:,y_], label="(n,g)" , linestyle="--" )
fig.add__plot( xAxis=Data2[:,x_], yAxis=Data2[:,y_], label="(n,2n)", linestyle="-" )
fig.add__legend()
fig.set__axis()
fig.save__figure()

