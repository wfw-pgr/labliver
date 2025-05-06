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
    on_frm, on_end      = 2, 24
    off_frm, off_end    = 0, 8
    on_, off_, cm_, rm_ = 0, 1, 2, 3

    # ------------------------------------------------- #
    # --- [1] Arguments                             --- #
    # ------------------------------------------------- #
    beamon       = list( range(  on_frm,  on_end+1 ) )
    beamoff      = list( range( off_frm, off_end+1 ) )
    datFilesList = [ [ "dat/sch/result__sch_{0}_{1}.dat".format( iON, iOFF )
                       for iON in beamon ] for iOFF in beamoff ]
    labels       = [ "{} d beam off".format( iOFF ) for iOFF in beamoff ]

    # ------------------------------------------------- #
    # --- [2] Fetch Data                            --- #
    # ------------------------------------------------- #
    import nkUtilities.load__pointFile as lpf
    p365    = []
    for iOFF,datFiles in enumerate( datFilesList ):
        DataLists = [ lpf.load__pointFile( inpFile=datFile, returnType="point" )
                      for datFile in datFiles ]
        tarr      = []
        for iON,Data in enumerate(DataLists):
            func1  = sp.interpolate.interp1d( Data[:,t_], Data[:,CB_], kind="nearest" )
            func2  = sp.interpolate.interp1d( Data[:,t_], Data[:,RM_], kind="nearest" )
            tarr  += [ [ beamon[iON], beamoff[iOFF], func1(365.0), func2(365.0) ] ]
        p365 += [ np.array( tarr )[:,np.newaxis,:] ]
    p365 = np.concatenate( p365, axis=1 )
    print( "p365 = {}".format( p365.shape ) )
    import nkUtilities.save__pointFile as spf
    outFile   = "dat/p365__scheduleScan.dat"
    names     = [ "beamon", "beamoff", "cummulate", "remaining" ]
    spf.save__pointFile( outFile=outFile, Data=p365 )

    # ------------------------------------------------- #
    # --- [3] plot Figure ( beamon-cummulate )      --- #
    # ------------------------------------------------- #
    config   = lcf.load__config()
    config_  = {
        "figure.size"        : [4.5,4.5],
        "figure.pngFile"     : "png/beamon_vs_cummulate.png", 
	"figure.position"    : [ 0.16, 0.16, 0.94, 0.94 ],
        "ax1.y.normalize"    : 1.0e9, 
	"ax1.x.range"        : { "auto":False, "min": 0.0, "max":  25.0, "num":6 },
	"ax1.y.range"        : { "auto":False, "min": 0.0, "max":2000.0, "num":11 },
	"ax1.x.label"        : "Irradiation days (d)",
	"ax1.y.label"        : "Production (GBq/y)",
	"ax1.x.minor.nticks" : 5, 
        "plot.marker"        : "o",
        "plot.markersize"    : 3.0,
        "legend.fontsize"    : 9.0, 
    }
    
    config = { **config, **config_ }
    fig    = gpl.gplot1D( config=config )
    for ik,iOFF in enumerate(beamoff):
        fig.add__plot( xAxis=p365[:,ik,on_], yAxis=p365[:,ik,cm_], \
                       label=labels[ik], color="C{}".format(ik) )
    fig.set__axis()
    fig.set__legend()
    fig.save__figure()

    # ------------------------------------------------- #
    # --- [3] plot Figure ( beamon-cummulate )      --- #
    # ------------------------------------------------- #
    config    = lcf.load__config()
    config_   = {
        "figure.size"        : [4.5,4.5],
        "figure.pngFile"     : "png/beamoff_vs_cummulate.png", 
	"figure.position"    : [ 0.16, 0.16, 0.94, 0.94 ],
        "ax1.y.normalize"    : 1.0e9, 
	"ax1.x.range"        : { "auto":False, "min": 0.0, "max":   7.0, "num": 8 },
	"ax1.y.range"        : { "auto":False, "min": 0.0, "max":2000.0, "num":11 },
	"ax1.x.label"        : "Beam off days (d)",
	"ax1.y.label"        : "Production (GBq/y)",
	"ax1.x.minor.nticks" : 1, 
        "plot.marker"        : "o",
        "plot.markersize"    : 3.0,
        "legend.fontsize"    : 9.0, 
    }
    config    = { **config, **config_ }
    xIndex_   = np.array( [ 2, 3, 4, 5, 6, 7, 8, 9, 10 ] )
    ONlabels = [ "{} d beam on".format( xI ) for xI in xIndex_ ]
    xIndex    = xIndex_ - on_frm
    fig       = gpl.gplot1D( config=config )
    for ik,xI in enumerate(xIndex):
        fig.add__plot( xAxis=p365[xI,:,off_], yAxis=p365[xI,:,cm_], \
                       label=ONlabels[ik], color="C{}".format(ik) )
    fig.set__axis()
    fig.set__legend()
    fig.save__figure()
    

# ======================================== #
# ===  実行部                          === #
# ======================================== #
if ( __name__=="__main__" ):
    display()

