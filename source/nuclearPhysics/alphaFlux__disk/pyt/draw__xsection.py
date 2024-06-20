import numpy                      as np
import nkUtilities.load__config   as lcf
import nkUtilities.plot1D         as pl1
import nkUtilities.configSettings as cfs

# ========================================================= #
# ===  display                                          === #
# ========================================================= #
def display( datFile=None, pngFile=None ):

    e_, xs_ = 0, 1

    # ------------------------------------------------- #
    # --- [1] Arguments                             --- #
    # ------------------------------------------------- #
    config  = lcf.load__config()
    if ( datFile is None ): sys.exit( "[draw__xsection.py] datFile == ???" )
    if ( pngFile is None ): sys.exit( "[draw__xsection.py] pngFile == ???" )
    
    # ------------------------------------------------- #
    # --- [2] Fetch Data                            --- #
    # ------------------------------------------------- #
    import nkUtilities.load__pointFile as lpf
    Data   = lpf.load__pointFile( inpFile=datFile, returnType="point" )
    
    # ------------------------------------------------- #
    # --- [3] config Settings                       --- #
    # ------------------------------------------------- #
    config                   = cfs.configSettings( configType="plot.def", config=config )
    config["FigSize"]        = (3.5,3.5)
    config["plt_position"]   = [ 0.18, 0.18, 0.94, 0.94 ]
    config["plt_xAutoRange"] = False
    config["plt_yAutoRange"] = False
    config["plt_xRange"]     = [  0.0, 80.0  ]
    config["plt_yRange"]     = [  1.0e-3, 1.0e3 ]
    config["xMajor_Nticks"]  = 9
    config["yMajor_Nticks"]  = 5
    config["plt_marker"]     = "o"
    config["plt_markersize"] = 3.0
    config["plt_linestyle"]  = "-"
    config["plt_linewidth"]  = 2.0
    config["plt_ylog"]       = True
    config["xTitle"]         = "Energy (MeV)"
    config["yTitle"]         = "Cross-section (mb)"

    # ------------------------------------------------- #
    # --- [4] plot Figure                           --- #
    # ------------------------------------------------- #
    fig     = pl1.plot1D( config=config, pngFile=pngFile )
    fig.add__plot( xAxis=Data[:,e_], yAxis=Data[:,xs_] )
    fig.set__axis()
    fig.save__figure()


# ======================================== #
# ===  実行部                          === #
# ======================================== #
if ( __name__=="__main__" ):

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument( "--datFile", help="input  file name." )
    parser.add_argument( "--pngFile", help="output file name." )
    args   = parser.parse_args()
    if ( args.datFile is None ):
        print( "[draw__xsection.py] datFile == ???" )
        sys.exit()
    if ( args.pngFile is None ):
        args.pngFile = "xsection.png"
    display( datFile=args.datFile, pngFile=args.pngFile )
