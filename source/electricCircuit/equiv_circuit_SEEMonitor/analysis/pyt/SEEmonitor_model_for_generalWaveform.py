import numpy as np


# ========================================================= #
# ===  SEEmonitor_model_graph.py                        === #
# ========================================================= #

def SEEmonitor_model_graph():

    ms             = 1.e-3
    t_, v_, i_, q_ = 0, 1, 2, 3
    
    # ------------------------------------------------- #
    # --- [1] def parameters                        --- #
    # ------------------------------------------------- #
    CC    = 2.5e-9
    RC    = 2.5
    CM    = 20.0e-12
    RM    = 1.0e6
    tau1  = 8.0e-3
    tau2  = 3.3e-3
    tau3  = 20.0e-3
    nT1   = 101
    nT2   = 101
    i0    = 0.71e-3
    
    # ------------------------------------------------- #
    # --- [2] calculation                           --- #
    # ------------------------------------------------- #
    tauRC = RM * ( CC + CM )
    t_pre = np.array( [-1e10, 0.0] )
    t1    = ( np.linspace(  0.0, tau1     , nT1 ) )[0:]
    # t2    = ( np.linspace( tau1, tau1+tau2, nT2 ) )[1:]
    t2    = ( np.linspace( tau1, tau3, nT2 ) )[1:]
    qchg  = tauRC * i0 * ( 1.0 - np.exp( - tau1  / tauRC ) )
    
    v1    = RM    * i0 * ( 1.0 - np.exp( - t1 / tauRC ) )
    i1    =         i0 * (       np.exp( - t1 / tauRC ) )
    q1    = tauRC * i0 * ( 1.0 - np.exp( - t1 / tauRC ) )
    v2    = qchg / (CC+CM) * ( np.exp( - ( t2 - tau1 ) / tauRC ) )
    i2    = qchg / tauRC   * ( np.exp( - ( t2 - tau1 ) / tauRC ) )
    q2    = qchg           * ( np.exp( - ( t2 - tau1 ) / tauRC ) )

    v_pre = np.array( [0.0,0.0] )
    i_pre = np.array( [0.0,0.0] )
    q_pre = np.array( [0.0,0.0] )
    
    time  = np.reshape( np.concatenate( [t_pre,t1,t2] ), [-1,1] )
    vt    = np.reshape( np.concatenate( [v_pre,v1,v2] ), [-1,1] )
    it    = np.reshape( np.concatenate( [i_pre,i1,i2] ), [-1,1] )
    qt    = np.reshape( np.concatenate( [q_pre,q1,q2] ), [-1,1] )
    Data  = np.concatenate( [time,vt,it,qt], axis=1 )
    print( Data.shape )
    
    # ------------------------------------------------- #
    # --- [3] save data in a file                   --- #
    # ------------------------------------------------- #
    import nkUtilities.save__pointFile as spf
    outFile   = "dat/SEEmonitor_model_graph.dat"
    spf.save__pointFile( outFile=outFile, Data=Data, names=["t","v(t)", "i(t)", "q(t)"] )

    # ------------------------------------------------- #
    # --- [4] display in a file                     --- #
    # ------------------------------------------------- #
    import nkUtilities.plot1D         as pl1
    import nkUtilities.load__config   as lcf
    import nkUtilities.configSettings as cfs
    x_,y_                    = 0, 1
    pngFile                  = "png/SEEmonitor_model_graph_v_vs_time.png"
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
    config["plt_linewidth"]  = 1.0
    config["xTitle"]         = "t"
    config["yTitle"]         = r"$v(t) / ( R_M i_0 \tau _1 / \tau _{RC} )$"
    fig     = pl1.plot1D( config=config, pngFile=pngFile )
    fig.add__plot( xAxis=Data[:,t_]/tau3, yAxis=Data[:,v_] / ( RM*i0 * tau1/tauRC ) )
    fig.set__axis()
    fig.save__figure()
    return()


# ========================================================= #
# ===   Execution of Pragram                            === #
# ========================================================= #

if ( __name__=="__main__" ):
    SEEmonitor_model_graph()
    
