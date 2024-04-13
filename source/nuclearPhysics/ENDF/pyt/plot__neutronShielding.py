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
inpFile3 = "dat/cs__B10_na.dat"
Data1    = lpf.load__pointFile( inpFile=inpFile1, returnType="point" )
Data2    = lpf.load__pointFile( inpFile=inpFile2, returnType="point" )
Data3    = lpf.load__pointFile( inpFile=inpFile3, returnType="point" )
print( np.min( Data1[:,x_] ), np.max( Data1[:,x_] ) )
print( np.min( Data1[:,y_] ), np.max( Data1[:,y_] ) )
print( np.min( Data2[:,x_] ), np.max( Data2[:,x_] ) )
print( np.min( Data2[:,y_] ), np.max( Data2[:,y_] ) )
print( np.min( Data3[:,x_] ), np.max( Data3[:,x_] ) )
print( np.min( Data3[:,y_] ), np.max( Data3[:,y_] ) )

pngFile                  = "png/neutronShielding.png"
config                   = lcf.load__config()
config                   = cfs.configSettings( configType="plot.def", config=config )
config["FigSize"]        = (6.0,6.0)
config["plt_position"]   = [ 0.16, 0.16, 0.94, 0.94 ]
config["plt_xAutoRange"] = False
config["plt_yAutoRange"] = False
config["plt_xRange"]     = [ +1.e-3, +1.e8 ]
config["plt_yRange"]     = [ +1.e-5, +1.e5 ]
config["xMajor_Nticks"]  = 11
config["yMajor_Nticks"]  = 11
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
fig.add__plot( xAxis=Data1[:,x_], yAxis=Data1[:,y_], label="226Ra(n,g)" , linestyle="--" )
fig.add__plot( xAxis=Data2[:,x_], yAxis=Data2[:,y_], label="226Ra(n,2n)", linestyle="-" )
fig.add__plot( xAxis=Data3[:,x_], yAxis=Data3[:,y_], label="10B(n,a)", linestyle="-." )
fig.add__legend()
fig.set__axis()
fig.save__figure()

