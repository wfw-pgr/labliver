import os, sys
import numpy as np
import nkUtilities.load__config   as lcf
import nkUtilities.gplot1D        as gp1

en_, xs_, = 0, 1,

# ------------------------------------------------- #
# --- [1] load data                             --- #
# ------------------------------------------------- #
DataDict  = {}
inpFiles  = { "(g,n)":"xs__rp088225.tot", "TENDL2023":"xs__TENDL2023.dat", }
for tag,ifile in inpFiles.items():
    with open( ifile, "r" ) as f:
        DataDict[tag] = np.loadtxt( f )
        
# ------------------------------------------------- #
# --- [2] plot graph                            --- #
# ------------------------------------------------- #
config   = lcf.load__config()
config_  = {
    "figure.size"        : [4.5,4.5],
    "figure.pngFile"     : "compare__tendl_talys.png", 
    "figure.position"    : [ 0.16, 0.16, 0.94, 0.94 ],
    "ax1.y.normalize"    : 1.0e0, 
    "ax1.x.range"        : { "auto":False, "min": 0.0, "max":40.0, "num":9 },
    "ax1.y.range"        : { "auto":False, "min": 0.0, "max":400., "num":9 },
    "ax1.x.label"        : "Energy (MeV)",
    "ax1.y.label"        : "Cross section (mb)",
    "ax1.x.minor.nticks" : 1, 
    "plot.marker"        : "o",
    "plot.markersize"    : 3.0,
    "legend.fontsize"    : 9.0, 
}
config = { **config, **config_ }
    
fig    = gp1.gplot1D( config=config )
for tag,Data in DataDict.items():
    fig.add__plot( xAxis=Data[:,en_], yAxis=Data[:,xs_], label=tag )
fig.set__axis()
fig.set__legend()
fig.save__figure()
