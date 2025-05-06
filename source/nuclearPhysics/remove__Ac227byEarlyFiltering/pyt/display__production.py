import numpy                      as np
import nkUtilities.load__config   as lcf
import nkUtilities.plot1D         as pl1
import nkUtilities.configSettings as cfs


# ========================================================= #
# ===  display                                          === #
# ========================================================= #
def display():

    t_, A_, B_ = 0, 3, 4

    # ------------------------------------------------- #
    # --- [1] Arguments                             --- #
    # ------------------------------------------------- #
    config   = lcf.load__config()
    datFile1 = "dat/Ac225__woSep.dat"
    datFile2 = "dat/Ac227__woSep.dat"
    pngFile  = "png/noSeparation.png"

    # ------------------------------------------------- #
    # --- [2] Fetch Data                            --- #
    # ------------------------------------------------- #
    import nkUtilities.load__pointFile as lpf
    Data1       = lpf.load__pointFile( inpFile=datFile1, returnType="point" )
    Data2       = lpf.load__pointFile( inpFile=datFile2, returnType="point" )
    Ra225EOB    = np.max( Data1[:,A_] )
    Data1[:,A_] = Data1[:,A_] / Ra225EOB
    Data1[:,B_] = Data1[:,B_] / Ra225EOB
    Data2[:,A_] = Data2[:,A_] / Ra225EOB
    Data2[:,B_] = Data2[:,B_] / Ra225EOB
  
    # ------------------------------------------------- #
    # --- [3] config Settings                       --- #
    # ------------------------------------------------- #
    config                   = cfs.configSettings( configType="plot.def", config=config )
    config["FigSize"]        = (4.5,4.5)
    config["plt_position"]   = [ 0.16, 0.16, 0.94, 0.94 ]
    config["plt_xAutoRange"] = False
    config["plt_yAutoRange"] = False
    config["plt_xRange"]     = [    0.0,  30.0 ]
    config["plt_yRange"]     = [ 1.0e-6, 1.0e1 ]
    config["xMajor_Nticks"]  = 7
    config["yMajor_Nticks"]  = 8
    config["plt_marker"]     = "none"
    config["plt_markersize"] = 3.0
    config["plt_linestyle"]  = "-"
    config["plt_linewidth"]  = 2.0
    config["plt_ylog"]       = True
    config["xTitle"]         = "Elapsed time t (days)"
    config["yTitle"]         = "$A(t)\ /\ A_{Ra225}^{EOB}$"

    # ------------------------------------------------- #
    # --- [4] plot Figure                           --- #
    # ------------------------------------------------- #
    fig     = pl1.plot1D( config=config, pngFile=pngFile )
    fig.add__plot( xAxis=Data1[:,t_], yAxis=Data1[:,A_], label="Ra225" )
    fig.add__plot( xAxis=Data1[:,t_], yAxis=Data1[:,B_], label="Ac225" )
    fig.add__plot( xAxis=Data2[:,t_], yAxis=Data2[:,A_], label="Ra227" )
    fig.add__plot( xAxis=Data2[:,t_], yAxis=Data2[:,B_], label="Ac227" )
    fig.add__legend()
    fig.set__axis()
    fig.save__figure()


# ======================================== #
# ===  実行部                          === #
# ======================================== #
if ( __name__=="__main__" ):
    display()

