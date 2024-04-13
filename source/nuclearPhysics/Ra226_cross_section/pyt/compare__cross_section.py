import numpy as np
import scipy as sp
import scipy.interpolate

# ========================================================= #
# ===  compare__cross_section.py                        === #
# ========================================================= #

def compare__cross_section( inpFiles=None, pngFile=None, labels=None ):

    e_, cs_                  = 0, 1
    
    # ------------------------------------------------- #
    # --- [1] arguments                             --- #
    # ------------------------------------------------- #
    if ( inpFiles is None ): sys.exit( "[compare__cross_section.py] inpFile == ???" )
    
    # ------------------------------------------------- #
    # --- [2] load cross-section Data               --- #
    # ------------------------------------------------- #
    import nkUtilities.load__pointFile as lpf
    stack = []
    nData = len( labels )
    for inpFile in inpFiles:
        Data   = lpf.load__pointFile( inpFile=inpFile, returnType="point" )
        stack += [ Data[:,:,np.newaxis] ]
    
    # ------------------------------------------------- #
    # --- [3] plot config                           --- #
    # ------------------------------------------------- #
    import nkUtilities.plot1D         as pl1
    import nkUtilities.load__config   as lcf
    import nkUtilities.configSettings as cfs
    config                   = lcf.load__config()
    config                   = cfs.configSettings( configType="plot.def", config=config )
    config["FigSize"]        = (4.5,4.5)
    config["plt_position"]   = [ 0.16, 0.16, 0.94, 0.94 ]
    config["plt_xAutoRange"] = False
    config["plt_yAutoRange"] = False
    config["plt_xRange"]     = [  0.0, 50.0  ]
    config["plt_yRange"]     = [  0.0, 400.0 ]
    config["xMajor_Nticks"]  = 11
    config["yMajor_Nticks"]  =  9
    config["plt_marker"]     = "o"
    config["plt_markersize"] = 2.0
    config["plt_linestyle"]  = "-"
    config["plt_linewidth"]  = 1.0
    config["xTitle"]         = "Energy (MeV)"
    config["yTitle"]         = "Cross Section (mb)"

    # ------------------------------------------------- #
    # --- [4] plot (whole data)                     --- #
    # ------------------------------------------------- #
    pngFile_ = pngFile.replace( ".png", "_whole.png" )
    fig      = pl1.plot1D( config=config, pngFile=pngFile_ )
    for ik,Data in enumerate( stack ):
        fig.add__plot( xAxis=Data[:,e_], yAxis=Data[:,cs_], label=labels[ik] )
    fig.set__axis()
    fig.add__legend()
    fig.save__figure()

    # ------------------------------------------------- #
    # --- [5] plot (log-log)                        --- #
    # ------------------------------------------------- #
    config["plt_xRange"] = [  1.0e0, 1.e2 ]
    config["plt_yRange"] = [  1.0e0, 1.e3 ]
    config["plt_xlog"]   = True
    config["plt_ylog"]   = True
    pngFile_ = pngFile.replace( ".png", "_xylog.png" )
    fig      = pl1.plot1D( config=config, pngFile=pngFile_ )
    for ik,Data in enumerate( stack ):
        fig.add__plot( xAxis=Data[:,e_], yAxis=Data[:,cs_], label=labels[ik] )
    fig.add__cursor( xAxis=[6.4], linestyle="--", color="gray", linewidth=0.6 )
    fig.set__axis()
    fig.add__legend()
    fig.save__figure()


    # # ------------------------------------------------- #
    # # --- [5] plot (closeup)                        --- #
    # # ------------------------------------------------- #
    # config["plt_xAutoRange"] = False
    # config["plt_yAutoRange"] = False
    # config["plt_linestyle"]  = "none"
    # config["plt_xRange"]     = [  0.0, 40.0  ]
    # config["plt_yRange"]     = [  0.0, 400.0 ]
    # config["xMajor_Nticks"]  = 5
    # config["yMajor_Nticks"]  = 11
    # pngFile_ = pngFile.replace( ".png", "_close.png" )
    # fig      = pl1.plot1D( config=config, pngFile=pngFile_ )
    # fig.add__plot( xAxis=Data[:,e_], yAxis=Data[:,cs_], \
    #                color="C0", linestyle="none", marker="o" )
    # fig.add__plot( xAxis=eAxis_    , yAxis=csAxis_    , \
    #                color="C0", linestyle="-", marker="none" )
    # fig.set__axis()
    # fig.save__figure()


# ========================================================= #
# ===   Execution of Pragram                            === #
# ========================================================= #

if ( __name__=="__main__" ):

    labels   = [ "2015", "2017", "2019", "2021", "2023" ]
    inpFiles = [ "dat/Ra226_gn_Ra225_TENDL__{}.dat".format( label ) for label in labels ]
    pngFile  = "png/Ra226_gn_Ra225_TENDL__compare.png"
    compare__cross_section( inpFiles=inpFiles, pngFile=pngFile, labels=labels )

    
