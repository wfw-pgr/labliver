import os, sys, json5
import scipy as sp
import numpy                      as np
import nkUtilities.load__config   as lcf
import nkUtilities.gplot1D        as gpl
import nkUtilities.configSettings as cfs


# ========================================================= #
# ===  display                                          === #
# ========================================================= #
def display():

    iON_, iOFF_, cm_, rm_, ab_ = 0, 1, 2, 3, 2
    
    # ------------------------------------------------- #
    # --- [1] load data                             --- #
    # ------------------------------------------------- #
    import nkUtilities.load__pointFile as lpf
    inpFile1  = "dat/p365__1target_2sep__selected.dat"
    inpFile2  = "dat/p365__2target_2sep__prep6h.dat"
    inpFile3  = "dat/p365__noalternating.dat"
    inpFile4  = "dat/p365__alternating.dat"
    Data1     = lpf.load__pointFile( inpFile=inpFile1, returnType="point" )
    Data2     = lpf.load__pointFile( inpFile=inpFile2, returnType="point" )
    Data3     = lpf.load__pointFile( inpFile=inpFile3, returnType="point" )
    Data4     = lpf.load__pointFile( inpFile=inpFile4, returnType="point" )
    Data1     = Data1[ np.where( ( Data1[:,1] >= 2 ) & ( Data1[:,1] <= 8 ) ) ]
    Data2     = Data2[ np.where( ( Data2[:,0] >= 2 ) & ( Data2[:,0] <= 8 ) ) ]
    Data3     = Data3[ np.where( ( Data3[:,1] >= 2 ) & ( Data3[:,1] <= 8 ) ) ]
    Data4     = Data4[ np.where( ( Data4[:,0] >= 2 ) & ( Data4[:,0] <= 8 ) ) ]
    
    # ------------------------------------------------- #
    # --- [4] plot Figure ( beamon-cummulate )      --- #
    # ------------------------------------------------- #
    config   = lcf.load__config()
    config_  = {
        "figure.size"        : [4.5,4.5],
        "figure.pngFile"     : "png/selected__2t2s_vs_1t1s.png", 
	"figure.position"    : [ 0.16, 0.16, 0.94, 0.94 ],
        "ax1.y.normalize"    : 1.0e9, 
	"ax1.x.range"        : { "auto":False, "min": 0.0, "max":  10.0, "num":11 },
	"ax1.y.range"        : { "auto":False, "min": 0.0, "max":1200.0, "num": 7 },
	"ax1.x.label"        : "Beam off duration (days)",
	"ax1.y.label"        : "Production (GBq/y)",
	"ax1.x.minor.nticks" : 1, 
        "plot.marker"        : "o",
        "plot.markersize"    : 3.0,
        "legend.fontsize"    : 9.0, 
    }
    config = { **config, **config_ }
    
    fig    = gpl.gplot1D( config=config )
    fig.add__plot( xAxis=Data1[:,iOFF_], yAxis=Data1[:,2], color="C0",
                   label="1 targets w/ 2 separation", marker="o", linestyle="--" )
    fig.add__plot( xAxis=Data2[:,iOFF_], yAxis=Data2[:,3], color="C1",
                   label="2 targets w/ 2 separation", marker="o", linestyle="--" )
    fig.add__plot( xAxis=Data3[:,iOFF_], yAxis=Data3[:,2], color="C0",
                   label="1 targets w/o 2 separation", marker="D", linestyle="-" )
    fig.add__plot( xAxis=Data4[:,iOFF_], yAxis=Data4[:,3], color="C1",
                   label="2 targets w/o 2 separation", marker="D", linestyle="-"  )
    fig.set__axis()
    fig.set__legend()
    fig.save__figure()


    # ------------------------------------------------- #
    # --- [4] plot Figure ( beamon-cummulate )      --- #
    # ------------------------------------------------- #
    config   = lcf.load__config()
    config_  = {
        "figure.size"        : [4.5,4.5],
        "figure.pngFile"     : "png/beamon_selected__2t2s_vs_1t1s.png", 
	"figure.position"    : [ 0.16, 0.16, 0.94, 0.94 ],
        "ax1.y.normalize"    : 1.0e9, 
	"ax1.x.range"        : { "auto":False, "min": 0.0, "max": 10.0, "num":11 },
	"ax1.y.range"        : { "auto":False, "min": 0.0, "max":500.0, "num":11 },
	"ax1.x.label"        : "Beam on duration (days)",
	"ax1.y.label"        : "Production (GBq/y)",
	"ax1.x.minor.nticks" : 1, 
        "plot.marker"        : "o",
        "plot.markersize"    : 3.0,
        "legend.fontsize"    : 9.0, 
    }
    config = { **config, **config_ }
    
    fig    = gpl.gplot1D( config=config )
    fig.add__plot( xAxis=Data1[:,iON_], yAxis=Data1[:,2], label="1 targets" )
    fig.add__plot( xAxis=Data2[:,iON_], yAxis=Data2[:,3], label="2 targets" )
    fig.set__axis()
    fig.set__legend()
    fig.save__figure()

    

# ======================================== #
# ===  実行部                          === #
# ======================================== #
if ( __name__=="__main__" ):
    display()

