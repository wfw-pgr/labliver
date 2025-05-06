import os, sys, json5
import numpy                      as np
import nkUtilities.plot1D         as pl1
import nkUtilities.load__config   as lcf
import nkUtilities.configSettings as cfs
import nkUtilities.load__pointFile as lpf

# ========================================================= #
# ===  display each formula                             === #
# ========================================================= #

def display():

    energy_, Scol_, Srad_, Stot_, ratio_ = 0, 1, 2, 3, 4
    min_,max_,num_ = 0, 1, 2
            
    # ------------------------------------------------- #
    # --- [1] calculate stopping power              --- #
    # ------------------------------------------------- #
    pngFile1   = "png/compare__TaPt_value.png"
    pngFile2   = "png/compare__TaPt_ratio.png"
    inpFiles   = [ "dat/stoppingPower__e_in_Ta.dat", 
                   "dat/stoppingPower__e_in_Pt.dat" ]
    keys       = [ "Ta", "Pt" ]
    DataDict   = {}

    # ------------------------------------------------- #
    # --- [2] load parameter                        --- #
    # ------------------------------------------------- #
    paramFile  = "dat/parameter__e_in_Ta.json"
    with open( paramFile, "r" ) as f:
        params = json5.load( f )

    # ------------------------------------------------- #
    # --- [3] setup energy axis                     --- #
    # ------------------------------------------------- #
    if ( params["Scol.eAxis.logarithm"] ):
        Rmaxmin = params["Scol.eAxis.MinMaxNum"][max_] / params["Scol.eAxis.MinMaxNum"][min_]
        seed    = np.linspace( 0.0, np.log10( Rmaxmin ), params["Scol.eAxis.MinMaxNum"][num_])
        energy  = params["Scol.eAxis.MinMaxNum"][min_] * 10.0**( seed )
    else:
        energy  = np.linspace( *params["Scol.eAxis.MinMaxNum"] )

    # ------------------------------------------------- #
    # --- [4] plot (Scol,Srad,Stot)                 --- #
    # ------------------------------------------------- #
    config                   = lcf.load__config()
    config["FigSize"]        = (4.5,4.5)
    config["plt_position"]   = [ 0.18, 0.18, 0.94, 0.94 ]
    config["plt_xAutoRange"] = False
    config["plt_yAutoRange"] = False
    config["plt_xRange"]     = params["plot.xAxis.MinMaxNum"][0:2]
    config["plt_yRange"]     = params["plot.yAxis.MinMaxNum"][0:2]
    config["xMajor_Nticks"]  = params["plot.xAxis.MinMaxNum"][2]
    config["yMajor_Nticks"]  = params["plot.xAxis.MinMaxNum"][2]
    config["xTitle"]         = params["plot.xAxis.title"]
    config["yTitle"]         = params["plot.yAxis.title"]
    config["plt_xlog"]       = params["plot.xAxis.log"]
    config["plt_ylog"]       = params["plot.yAxis.log"]
    config["plt_marker"]     = "none"
    config["plt_markersize"] = 0.0
    config["plt_linewidth"]  = 2.0
    
    fig     = pl1.plot1D( config=config, pngFile=pngFile1 )
    for ik,inpFile in enumerate(inpFiles):
        Data = lpf.load__pointFile( inpFile=inpFile, returnType="point" )
        name = "({})".format( keys[ik] ) 
        fig.add__plot( xAxis=Data[:,energy_], yAxis=Data[:,Scol_], label="Scol"+name, \
                       color="C{}".format(ik), linestyle="--" )
        fig.add__plot( xAxis=Data[:,energy_], yAxis=Data[:,Srad_], label="Srad"+name, \
                       color="C{}".format(ik), linestyle=":" )
        fig.add__plot( xAxis=Data[:,energy_], yAxis=Data[:,Stot_], label="Stot"+name, \
                       color="C{}".format(ik), linestyle="-" )
    fig.set__axis()
    fig.add__legend()
    fig.save__figure()

    # ------------------------------------------------- #
    # --- [4] plot (fraction)                       --- #
    # ------------------------------------------------- #
    config["plt_xAutoRange"] = False
    config["plt_yAutoRange"] = False
    config["plt_xRange"]     = params["plot.xAxis.MinMaxNum"][0:2]
    config["plt_yRange"]     = [ 0.0, 120.0 ]
    config["xMajor_Nticks"]  = params["plot.xAxis.MinMaxNum"][2]
    config["yMajor_Nticks"]  = 7
    config["xTitle"]         = params["plot.xAxis.title"]
    config["yTitle"]         = "Radiation ratio (%)"
    config["plt_xlog"]       = params["plot.xAxis.log"]
    config["plt_ylog"]       = False
    config["plt_marker"]     = "o"
    config["plt_markersize"] = 3.0
    config["plt_linestyle"]  = "-"
    config["plt_linewidth"]  = 2.0
    
    fig     = pl1.plot1D( config=config, pngFile=pngFile2 )
    for ik,inpFile in enumerate(inpFiles):
        name = "({})".format( keys[ik] ) 
        Data = lpf.load__pointFile( inpFile=inpFile, returnType="point" )
        fig.add__plot( xAxis=Data[:,energy_], yAxis=Data[:,ratio_], label=name, \
                       color="C{}".format(ik), linestyle="-" )
    fig.set__axis()
    fig.add__legend()
    fig.save__figure()

    return()



# ========================================================= #
# ===   Execution of Pragram                            === #
# ========================================================= #
if ( __name__=="__main__" ):
    display()
