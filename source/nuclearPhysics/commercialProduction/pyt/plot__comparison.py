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

    t_, AB_, CB_ = 0, 4, 5
    
    # ------------------------------------------------- #
    # --- [1] load data                             --- #
    # ------------------------------------------------- #
    import nkUtilities.load__pointFile as lpf
    inpFile1  = "dat/sch/result__sch_10_5.dat"
    inpFile2  = "dat/1target_2sep/result__1target_2sep_10_5.dat"
    Data1     = lpf.load__pointFile( inpFile=inpFile1, returnType="point" )
    Data2     = lpf.load__pointFile( inpFile=inpFile2, returnType="point" )
    
    # ------------------------------------------------- #
    # --- [4] plot Figure ( beamon-cummulate )      --- #
    # ------------------------------------------------- #
    config   = lcf.load__config()
    config_  = {
        "figure.size"        : [4.5,4.5],
        "figure.pngFile"     : "png/comparision__2sep_10_5.png", 
	"figure.position"    : [ 0.16, 0.16, 0.84, 0.84 ],
        "ax1.y.normalize"    : 1.0e9, 
        "ax2.y.normalize"    : 1.0e9, 
	"ax1.x.range"        : { "auto":False, "min": 0.0, "max": 400.0, "num": 5 },
	"ax1.y.range"        : { "auto":False, "min": 0.0, "max":  80.0, "num": 5 },
	"ax2.y.range"        : { "auto":False, "min": 0.0, "max":1200.0, "num": 7 },
	"ax1.x.label"        : "Elapsed time t (days)",
	"ax1.y.label"        : "Activity (GBq)",
	"ax2.y.label"        : "Annual production (GBq/y)",
	"ax1.x.minor.nticks" : 1, 
        "plot.marker"        : "none",
        "plot.markersize"    : 3.0,
        "legend.fontsize"    : 9.0, 
    }
    config = { **config, **config_ }
    
    fig    = gpl.gplot1D( config=config )
    fig.add__plot ( xAxis=Data1[:,t_], yAxis=Data1[:,AB_], color="C2",
                    label="Activity 1 separation", linestyle="-" )
    fig.add__plot2( xAxis=Data1[:,t_], yAxis=Data1[:,CB_], color="C3",
                    label="Annual Production 1 separation", linestyle="-" )
    fig.add__plot ( xAxis=Data2[:,t_], yAxis=Data2[:,AB_], color="C1",
                    label="Activity 2 separation", linestyle="-" )
    fig.add__plot2( xAxis=Data2[:,t_], yAxis=Data2[:,CB_], color="C0",
                    label="Annual Production 2 separation", linestyle="-" )
    fig.add__cursor( xAxis=365.0, linestyle="--", linewidth=1.2, color="lightgrey" )
    fig.set__axis()
    fig.set__legend()
    fig.save__figure()
    

# ======================================== #
# ===  実行部                          === #
# ======================================== #
if ( __name__=="__main__" ):
    display()

