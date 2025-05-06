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
    
    t_, NA_, NB_, AA_, AB_, CB_, RM_ = 0, 1, 2, 3, 4, 5, 6
    D_frm, D_end = 2, 24
    nDays        = 7
    recList      = [ "0999", "0990", "0980", "0950", "0900", "0800" ]
    refillList   = [ 0, 1, 2, 3 ,4 , 5, 6, 7, 8, 10, 52 ]
    labels       = [ "99.9 (%)", "99.0 (%)", "98.0 (%)", "95.0 (%)", "90.0 (%)", "80.0 (%)" ]

    # ------------------------------------------------- #
    # --- [1] Arguments                             --- #
    # ------------------------------------------------- #
    datFilesList = [ [ "dat/refill/result_{0}_{1}.dat".format( irec, iref )
                       for iref in refillList ] for irec in recList ]
    
    # ------------------------------------------------- #
    # --- [2] Fetch Data                            --- #
    # ------------------------------------------------- #
    import nkUtilities.load__pointFile as lpf
    p365   = []
    xAxis  = np.array( refillList )
    for iD,datFiles in enumerate( datFilesList ):
        DataLists = [ lpf.load__pointFile( inpFile=datFile, returnType="point" )
                      for datFile in datFiles ]
        tarr      = []
        for ik,Data in enumerate(DataLists):
            func1  = sp.interpolate.interp1d( Data[:,t_], Data[:,CB_], kind="nearest" )
            func2  = sp.interpolate.interp1d( Data[:,t_], Data[:,RM_], kind="nearest" )
            tarr  += [ [ xAxis[ik], func1(365.0), func2(365.0) ] ]
        p365 += [ np.array( tarr )[:,:,np.newaxis] ]
    p365 = np.concatenate( p365, axis=2 )

    # ------------------------------------------------- #
    # --- [3] save data                             --- #
    # ------------------------------------------------- #
    import nkUtilities.save__pointFile as spf
    for ik,rec in enumerate(recList):
        outFile   = "dat/refill/refill__365_{}.dat".format( rec )
        save      = p365[:,:,ik]
        spf.save__pointFile( outFile=outFile, Data=save )
        
    # ------------------------------------------------- #
    # --- [4] plot Figure ( beamon-cummulate )      --- #
    # ------------------------------------------------- #
    config   = lcf.load__config()
    config_  = {
        "figure.size"        : [4.5,4.5],
        "figure.pngFile"     : "png/refill_vs_cummulate.png", 
	"figure.position"    : [ 0.16, 0.16, 0.94, 0.94 ],
        "ax1.y.normalize"    : 1.0e9, 
	"ax1.x.range"        : { "auto":False, "min": 0.0, "max":  10.0, "num":6 },
	"ax1.y.range"        : { "auto":False, "min": 0.0, "max":2000.0, "num":11 },
	"ax1.x.label"        : "Annual target refills (/year)",
	"ax1.y.label"        : "Production (GBq/y)",
	"ax1.x.minor.nticks" : 2, 
        "plot.marker"        : "o",
        "plot.markersize"    : 3.0,
        "legend.fontsize"    : 9.0, 
    }
    config = { **config, **config_ }
    
    fig    = gpl.gplot1D( config=config )
    for ik in range( len(recList) ):
        fig.add__plot( xAxis=p365[:-1,0,ik], yAxis=p365[:-1,1,ik], \
                       label=labels[ik], color="C{}".format(ik) )
    val = p365[-1,1,0] / config["ax1.y.normalize"]
    fig.add__cursor( yAxis=float(val), color="grey" )
    fig.set__axis()
    fig.set__legend()
    fig.save__figure()

    # ------------------------------------------------- #
    # --- [4] normalize production plot             --- #
    # ------------------------------------------------- #
    config   = lcf.load__config()
    config_  = {
        "figure.size"        : [4.5,4.5],
        "figure.pngFile"     : "png/refill_vs_relativeProduction.png", 
	"figure.position"    : [ 0.16, 0.16, 0.94, 0.94 ],
	"ax1.x.range"        : { "auto":False, "min": 0.0, "max": 10.0, "num":6 },
	"ax1.y.range"        : { "auto":False, "min": 0.0, "max":120.0, "num":7 },
	"ax1.x.label"        : "Annual target refills (/year)",
	"ax1.y.label"        : "Relative production (%)",
	"ax1.x.minor.nticks" : 2, 
        "plot.marker"        : "o",
        "plot.markersize"    : 3.0,
        "legend.fontsize"    : 9.0, 
    }
    config = { **config, **config_ }
    
    fig    = gpl.gplot1D( config=config )
    for ik in range( len(recList) ):
        values = p365[:-1,1,ik] / p365[-1,1,ik] * 100.0
        fig.add__plot( xAxis=p365[:-1,0,ik], yAxis=values, \
                       label=labels[ik], color="C{}".format(ik) )
        fig.add__cursor( yAxis=100.0, color="grey" )
    fig.set__axis()
    fig.set__legend()
    fig.save__figure()


    

# ======================================== #
# ===  実行部                          === #
# ======================================== #
if ( __name__=="__main__" ):
    display()

