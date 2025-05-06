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
    AAt_, ABt_, CBt_ = 7, 8, 9
    cycleLIST        = [ "cycle1", "cycle2" ]
    beamoffList      = list( range( 2, 10+1 ) )
    
    # ------------------------------------------------- #
    # --- [2] Fetch Data                            --- #
    # ------------------------------------------------- #
    import nkUtilities.load__pointFile as lpf
    p365 = []
    for beamoff in beamoffList:
        beamon   = beamoff
        datFile1 = "dat/2target_2sep/result__2target_2sep_{0}_{0}_cycle1.dat".format( beamoff )
        datFile2 = "dat/2target_2sep/result__2target_2sep_{0}_{0}_cycle2.dat".format( beamoff )
        Data1    = lpf.load__pointFile( inpFile=datFile1, returnType="point" )
        Data2    = lpf.load__pointFile( inpFile=datFile2, returnType="point" )
        nData    = min( Data1.shape[0], Data2.shape[0] )
        Data1    = Data1[:nData,:]
        Data2    = Data2[:nData,:]
        Data_tot = np.concatenate( [ Data1[:,t_][:,np.newaxis], Data1[:,AA_:CB_+1], \
                                     Data2[:,AA_:CB_+1], (Data1+Data2)[:,AA_:CB_+1] ], axis=1 )
        names    = [ "time", "AA1", "AB1", "CB1", "AA2", "AB2", "CB2", "AAt", "ABt", "CBt" ]
        import nkUtilities.save__pointFile as spf
        outFile   = "dat/2target_2sep/result_2target_2sep_{0}_{0}_total.dat".format( beamoff )
        spf.save__pointFile( outFile=outFile, Data=Data_tot, names=names )

        func1    = sp.interpolate.interp1d( Data_tot[:,t_], Data_tot[:,ABt_], kind="nearest" )
        func2    = sp.interpolate.interp1d( Data_tot[:,t_], Data_tot[:,CBt_], kind="nearest" )
        p365    += [ np.array( [ beamon, beamoff, func1(365.0), func2(365.0) ] )[np.newaxis,:] ]
    p365      = np.concatenate( p365, axis=0 )

    # ------------------------------------------------- #
    # --- [3] Fetch Data ( no 2target_2sep )         --- #
    # ------------------------------------------------- #
    import nkUtilities.load__pointFile as lpf
    inpFile     = "dat/p365__1target_2sep.dat"
    Data        = lpf.load__pointFile( inpFile=inpFile, returnType="point" )
    noBeamAxis1 = np.copy( Data[:,1] )
    oneTarget   = np.copy( Data[:,2] )
    index1      = np.where( ( noBeamAxis1 >= 2) & ( noBeamAxis1 <= 6 ) )
    noBeamAxis1 = noBeamAxis1[ index1 ]
    oneTarget   = oneTarget  [ index1 ]
    noBeamAxis2 = np.copy( p365[:,1] )
    twoTarget   = np.copy( p365[:,3] )
    index2      = np.where( ( noBeamAxis2 >= 2) & ( noBeamAxis2 <= 10 ) )
    noBeamAxis2 = noBeamAxis2[ index2 ]
    twoTarget   = twoTarget  [ index2 ]
    print( noBeamAxis1.shape, oneTarget.shape )
    print( noBeamAxis2.shape, twoTarget.shape )
    print( oneTarget )
    print( twoTarget )
    
    # ------------------------------------------------- #
    # --- [4] save data                             --- #
    # ------------------------------------------------- #
    outFile   = "dat/p365__2target_2sep.dat"
    spf.save__pointFile( outFile=outFile, Data=p365 )
            
    # ------------------------------------------------- #
    # --- [4] plot Figure ( beamon-cummulate )      --- #
    # ------------------------------------------------- #
    config   = lcf.load__config()
    config_  = {
        "figure.size"        : [4.5,4.5],
        "figure.pngFile"     : "png/p365__2target_2sep.png", 
	"figure.position"    : [ 0.16, 0.16, 0.94, 0.94 ],
        "ax1.y.normalize"    : 1.0e9, 
	"ax1.x.range"        : { "auto":False, "min": 0.0, "max": 10.0, "num":11 },
	"ax1.y.range"        : { "auto":False, "min": 0.0, "max":500.0, "num":11 },
	"ax1.x.label"        : "Beam off duration (days)",
	"ax1.y.label"        : "Production (GBq/y)",
	"ax1.x.minor.nticks" : 1, 
        "plot.marker"        : "o",
        "plot.markersize"    : 3.0,
        "legend.fontsize"    : 9.0, 
    }
    config = { **config, **config_ }
    
    fig    = gpl.gplot1D( config=config )
    fig.add__plot( xAxis=noBeamAxis2, yAxis=twoTarget,                label="2 targets" )
    fig.add__plot( xAxis=noBeamAxis1, yAxis=oneTarget, linewidth=0.0, label="1 targets" )
    fig.set__axis()
    fig.set__legend()
    fig.save__figure()


    

# ======================================== #
# ===  実行部                          === #
# ======================================== #
if ( __name__=="__main__" ):
    display()


