import numpy as np


# ========================================================= #
# ===  display__generalWaveform.py                      === #
# ========================================================= #

def display__generalWaveform():

    t_,v_ = 0, 1
    CC    = 2.5e-9
    CM    = 20.0e-12
    RM    = 1.0e6
    tauRC = RM * ( CC + CM )
    i0    = 0.71e-3
    tau1  = np.array( [ 0.0, 1.0e-3, 2.0e-3, 4.0e-3, 8.0e-3 ] )
    tau3  = 20.0e-3
    coef  = RM * i0 * tau1/tauRC
    
    # ------------------------------------------------- #
    # --- [1] import file                           --- #
    # ------------------------------------------------- #
    import nkUtilities.load__pointFile as lpf
    inpFile1 = "dat/SEEmonitor_tau_5percent.dat"
    inpFile2 = "dat/SEEmonitor_tau_10percent.dat"
    inpFile3 = "dat/SEEmonitor_tau_20percent.dat"
    inpFile4 = "dat/SEEmonitor_tau_40percent.dat"
    Data1    = lpf.load__pointFile( inpFile=inpFile1, returnType="point" )
    Data2    = lpf.load__pointFile( inpFile=inpFile2, returnType="point" )
    Data3    = lpf.load__pointFile( inpFile=inpFile3, returnType="point" )
    Data4    = lpf.load__pointFile( inpFile=inpFile4, returnType="point" )
    
    # ------------------------------------------------- #
    # --- [2] display in a file                     --- #
    # ------------------------------------------------- #
    import nkUtilities.plot1D         as pl1
    import nkUtilities.load__config   as lcf
    import nkUtilities.configSettings as cfs
    x_,y_                    = 0, 1
    pngFile                  = "png/SEEmonitor_generalWaveform.png"
    config                   = lcf.load__config()
    config                   = cfs.configSettings( configType="plot.def", config=config )
    config["FigSize"]        = (4.5,4.5)
    config["plt_position"]   = [ 0.16, 0.16, 0.94, 0.94 ]
    config["plt_xAutoRange"] = False
    config["plt_yAutoRange"] = False
    config["plt_xRange"]     = [ -0.2, +1.0 ]
    config["plt_yRange"]     = [ -0.2, +1.2 ]
    config["xMajor_Nticks"]  = 7
    config["yMajor_Nticks"]  = 8
    config["plt_marker"]     = "none"
    config["plt_markersize"] = 4.0
    config["plt_linestyle"]  = "-"
    config["plt_linewidth"]  = 1.6
    config["xTitle"]         = r"$t \ / \ \tau _2$"
    config["yTitle"]         = r"$v(t) \ / \ ( R_M i_0 \tau _1 / \tau _{RC} )$"
    fig     = pl1.plot1D( config=config, pngFile=pngFile )
    fig.add__plot( xAxis=Data1[:,t_]/tau3, yAxis=Data1[:,v_] / coef[1], \
                   label=r"$\tau_1/\tau_{RC}=0.4$" )
    fig.add__plot( xAxis=Data2[:,t_]/tau3, yAxis=Data2[:,v_] / coef[2], \
                   label=r"$\tau_1/\tau_{RC}=0.8$")
    fig.add__plot( xAxis=Data3[:,t_]/tau3, yAxis=Data3[:,v_] / coef[3], \
                   label=r"$\tau_1/\tau_{RC}=1.6$") 
    fig.add__plot( xAxis=Data4[:,t_]/tau3, yAxis=Data4[:,v_] / coef[4], \
                   label=r"$\tau_1/\tau_{RC}=3.2$")
    fig.add__text( xpos=0.05, ypos=0.92, text=r"$\tau _{RC}=R_M (C_C+C_M)$", fontsize=12 )
    fig.set__axis()
    fig.add__legend()
    fig.save__figure()
    return()


# ========================================================= #
# ===   Execution of Pragram                            === #
# ========================================================= #

if ( __name__=="__main__" ):
    display__generalWaveform()
                   
