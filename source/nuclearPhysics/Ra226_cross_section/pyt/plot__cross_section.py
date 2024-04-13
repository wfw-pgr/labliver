import numpy as np
import scipy as sp
import scipy.interpolate

# ========================================================= #
# ===  plot__cross_section.py                           === #
# ========================================================= #

def plot__cross_section( inpFile=None, pngFile=None ):

    e_, cs_                  = 0, 1
    
    # ------------------------------------------------- #
    # --- [1] arguments                             --- #
    # ------------------------------------------------- #
    if ( inpFile is None ): sys.exit( "[plot__cross_section.py] inpFile == ???" )
    
    # ------------------------------------------------- #
    # --- [2] load cross-section Data               --- #
    # ------------------------------------------------- #
    import nkUtilities.load__pointFile as lpf
    Data    = lpf.load__pointFile( inpFile=inpFile, returnType="point" )
    cs      = scipy.interpolate.CubicSpline( Data[:,e_], Data[:,cs_] )
    eAxis_  = np.linspace( 0.0, 30.0, 101 )
    csAxis_ = cs( eAxis_ )
    
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
    config["plt_xAutoRange"] = True
    config["plt_yAutoRange"] = False
    config["plt_xRange"]     = [  0.0, 30.0  ]
    config["plt_yRange"]     = [  0.0, 400.0 ]
    config["xMajor_Nticks"]  = 11
    config["yMajor_Nticks"]  = 11
    config["plt_marker"]     = "o"
    config["plt_markersize"] = 3.0
    config["plt_linestyle"]  = "-"
    config["plt_linewidth"]  = 2.0
    config["xTitle"]         = "Energy (MeV)"
    config["yTitle"]         = "Cross-section (mb)"

    # ------------------------------------------------- #
    # --- [4] plot (whole data)                     --- #
    # ------------------------------------------------- #
    pngFile_ = pngFile.replace( ".png", "_whole.png" )
    fig      = pl1.plot1D( config=config, pngFile=pngFile_ )
    fig.add__plot( xAxis=Data[:,e_], yAxis=Data[:,cs_] )
    fig.set__axis()
    fig.save__figure()

    # ------------------------------------------------- #
    # --- [5] plot (closeup)                        --- #
    # ------------------------------------------------- #
    config["plt_xAutoRange"] = False
    config["plt_yAutoRange"] = False
    config["plt_linestyle"]  = "none"
    config["plt_xRange"]     = [  0.0, 40.0  ]
    config["plt_yRange"]     = [  0.0, 400.0 ]
    config["xMajor_Nticks"]  = 5
    config["yMajor_Nticks"]  = 11
    pngFile_ = pngFile.replace( ".png", "_close.png" )
    fig      = pl1.plot1D( config=config, pngFile=pngFile_ )
    fig.add__plot( xAxis=Data[:,e_], yAxis=Data[:,cs_], \
                   color="C0", linestyle="none", marker="o" )
    fig.add__plot( xAxis=eAxis_    , yAxis=csAxis_    , \
                   color="C0", linestyle="-", marker="none" )
    fig.set__axis()
    fig.save__figure()


# ========================================================= #
# ===   Execution of Pragram                            === #
# ========================================================= #

if ( __name__=="__main__" ):

    inpFile = "dat/Ra226_gn_Ra225_TENDL.dat"
    pngFile = "png/Ra226_gn_Ra225_TENDL.png"
    plot__cross_section( inpFile=inpFile, pngFile=pngFile )

    
