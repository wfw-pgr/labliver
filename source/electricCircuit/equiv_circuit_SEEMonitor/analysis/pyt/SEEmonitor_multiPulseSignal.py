import os, sys
import numpy as np

# ========================================================= #
# ===  calculate__past_kth_signal                       === #
# ========================================================= #

def calculate__past_kth_signal( time, tau1, tau2, tauRC, RM, i0, kth ):

    ret   = np.copy( time ) * 0.0
    t1    =  0.0 - kth*tau2
    t2    = tau1 - kth*tau2
    sig1  = time  * 0.0
    sig2  = RM*i0 * ( 1.0 - np.exp( (-1.0)*(time-t1)/tauRC ) )
    sig3  = RM*i0 * ( 1.0 - np.exp( (-1.0)*tau1/tauRC ) ) \
        * np.exp( (-1.0)*tau2/tauRC * kth ) \
        * np.exp( (-1.0)*(time)/tauRC )
    ret1  = np.where(   time< t1           , sig1, 0.0 )
    ret2  = np.where(  (time>=t1)&(time<t2), sig2, 0.0 )
    ret3  = np.where(   time>=t2           , sig3, 0.0 )
    ret   = ret1 + ret2 + ret3
    return( ret )

# ========================================================= #
# ===  SEEmonitor_multiPulseSignal.py                   === #
# ========================================================= #

def SEEmonitor_multiPulseSignal():

    ms          = 1.e-3
    t_, v_, o_  = 0, 1, 2
    
    # ------------------------------------------------- #
    # --- [1] def parameters                        --- #
    # ------------------------------------------------- #
    CC          = 8.4e-9
    RC          = 2.5
    CM          = 20.0e-12
    RM          = 1.0e+6
    tau1        = 3.0e-6
    tau2        = 3.333e-3
    tau3        = 20.0e-3
    nT1         = 11
    nT2         = 51
    I_SEE_ave   = 0.97e-6/200.0 * 210.0 * 1.57
    tau_beam    = 3.0e-6
    f_Repeat    = 300.0
    duty        = tau_beam * f_Repeat
    I_SEE_pulse = I_SEE_ave / duty
    i0          = I_SEE_pulse
    print( " i0 == {}".format( i0 ) )
    
    # ------------------------------------------------- #
    # --- [2] calculation                           --- #
    # ------------------------------------------------- #
    tauRC = RM * ( CC + CM )
    time    = np.linspace( -1.0*tau3, 1.0*tau3, 2001 )
    kth_list = np.arange( -200, 20 )
    vt    = np.copy( time ) * 0.0
    for kth in kth_list:
        vt_iter  = calculate__past_kth_signal( time, tau1, tau2, tauRC, RM, i0, kth )
        vt      += vt_iter

    a0    = RM*i0 * ( 1.0-np.exp( -1.0*tau1/tauRC ) )
    r     = np.exp( -1.0*tau2/tauRC )
    S_inf = a0 * r/( 1.0-r )
    v_ofs = np.zeros_like( time ) + S_inf

    time  = np.reshape(  time, [-1,1] )
    vt    = np.reshape(    vt, [-1,1] )
    vo    = np.reshape( v_ofs, [-1,1] )
    Data  = np.concatenate( [time,vt,vo], axis=1 )

    
    # ------------------------------------------------- #
    # --- [3] save data in a file                   --- #
    # ------------------------------------------------- #
    import nkUtilities.save__pointFile as spf
    outFile   = "dat/SEEmonitor__multiPulseSignal.dat"
    spf.save__pointFile( outFile=outFile, Data=Data, names=["t","v(t)", "i(t)", "q(t)"] )

    # ------------------------------------------------- #
    # --- [4] display in a file                     --- #
    # ------------------------------------------------- #
    import nkUtilities.plot1D         as pl1
    import nkUtilities.load__config   as lcf
    import nkUtilities.configSettings as cfs
    x_,y_                    = 0, 1
    pngFile                  = "png/SEEmonitor__multiPulseSignal.png"
    config                   = lcf.load__config()
    config                   = cfs.configSettings( configType="plot.def", config=config )
    config["FigSize"]        = (4.5,4.5)
    config["plt_position"]   = [ 0.16, 0.16, 0.94, 0.94 ]
    config["plt_xAutoRange"] = False
    config["plt_yAutoRange"] = False
    config["plt_xRange"]     = [ -2.0, +20.0 ]
    config["plt_yRange"]     = [ -0.5, +3.0  ]
    config["xMajor_Nticks"]  = 12
    config["yMajor_Nticks"]  = 8
    config["plt_marker"]     = "none"
    config["plt_markersize"] = 2.0
    config["plt_linestyle"]  = "-"
    config["plt_linewidth"]  = 1.0
    config["xTitle"]         = "$t \ \mathrm{(ms)}$"
    config["yTitle"]         = "$v(t) \ \mathrm{(V)}$"
    fig     = pl1.plot1D( config=config, pngFile=pngFile )
    fig.add__plot( xAxis=Data[:,t_]/ms, yAxis=Data[:,v_] )
    fig.add__plot( xAxis=Data[:,t_]/ms, yAxis=Data[:,o_], linestyle="--" )
    fig.set__axis()
    fig.save__figure()
    return()


# ========================================================= #
# ===   Execution of Pragram                            === #
# ========================================================= #

if ( __name__=="__main__" ):
    SEEmonitor_multiPulseSignal()
    
