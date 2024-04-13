import sys
import numpy                      as np
import nkUtilities.load__config   as lcf
import nkUtilities.plot1D         as pl1
import nkUtilities.configSettings as cfs


# ========================================================= #
# ===  calculate__radiativeEquilibrium                  === #
# ========================================================= #

def calculate__radiativeEquilibrium( name_A="A", name_B="B", time=None, \
                                     T_A=1.0, T_B=1.0, N_A0=1.0, unit=1.0 ):

    # ------------------------------------------------- #
    # --- [1] arguments                             --- #
    # ------------------------------------------------- #
    if ( time is None ): time = np.linspace( 0.0, 10.0*np.max( [T_A, T_B] ), 101 )

    # ------------------------------------------------- #
    # --- [2] calculation                           --- #
    # ------------------------------------------------- #
    lambda_A = np.log( 2.0 ) / ( T_A * unit )
    lambda_B = np.log( 2.0 ) / ( T_B * unit )
    A0       = N_A0 / lambda_A
    T_max    = ( np.log( lambda_A/lambda_B ) ) / ( lambda_A - lambda_B ) / unit
    NB_max   = lambda_B / ( lambda_B - lambda_A ) * N_A0 \
        * ( np.exp( - lambda_A * T_max * unit ) - np.exp( - lambda_B * T_max * unit ) )
    coef_A   = A0
    coef_B   = lambda_A / ( lambda_B - lambda_A ) * A0
    atte_A   =   np.exp( - lambda_A * time * unit )
    atte_B   = ( np.exp( - lambda_A * time * unit ) - np.exp( - lambda_B * time * unit ) )
    nNum_A   =   coef_A * atte_A
    nNum_B   =   coef_B * atte_B
    radi_A   = lambda_A * nNum_A
    radi_B   = lambda_B * nNum_B
    
    # ------------------------------------------------- #
    # --- [3] return                                --- #
    # ------------------------------------------------- #
    ret = { "name_A":name_A, "name_B":name_B, \
            "nNum_A":nNum_A, "nNum_B":nNum_B, "radi_A":radi_A, "radi_B":radi_B, \
            "coef_A":coef_A, "atte_A":atte_A, "coef_B":coef_B, "atte_B":atte_B, \
            "lambda_A":lambda_A, "lambda_B":lambda_B, \
            "T_max":T_max, "T_A":T_A, "T_B":T_B, "time":time, "NB_max":NB_max }
    return( ret )
    

# ========================================================= #
# ===  plot__radiativeEquilibrium                       === #
# ========================================================= #

def plot__radiativeEquilibrium( name_A="A", name_B="B", T_A=1.0, T_B=1.0, N_A0=1.0, time=None, \
                                pngFile="png/out.png", unit=None ):
    
    # ------------------------------------------------- #
    # --- [1] calculation and expansion             --- #
    # ------------------------------------------------- #
    ret    = calculate__radiativeEquilibrium( name_A=name_A, name_B=name_B, \
                                              time=time, T_A=T_A, T_B=T_B, \
                                              N_A0=N_A0, unit=unit )
    time    = ret["time"]
    radi_A  = ret["radi_A"]
    radi_B  = ret["radi_B"]
    label_A = "$N_{}$".format( "{" + ret["name_A"] + "}" )
    label_B = "$N_{}$".format( "{" + ret["name_B"] + "}" )

    # ------------------------------------------------- #
    # --- [2] plot config                           --- #
    # ------------------------------------------------- #
    config                   = lcf.load__config()
    config                   = cfs.configSettings( configType="plot.def", config=config )
    config["FigSize"]        = (4.5,4.5)
    config["plt_position"]   = [ 0.16, 0.16, 0.94, 0.94 ]
    config["plt_xAutoRange"] = False
    config["plt_yAutoRange"] = False
    config["plt_xRange"]     = [  0.0, +80.0 ]
    config["plt_yRange"]     = [  0.0, +1.0  ]
    config["xMajor_Nticks"]  = 9
    config["yMajor_Nticks"]  = 11
    config["plt_marker"]     = "none"
    config["plt_markersize"] = 3.0
    config["plt_linestyle"]  = "-"
    config["plt_linewidth"]  = 2.0
    config["xTitle"]         = "elapsed days (d)"
    config["yTitle"]         = "radioactivity (Bq)"

    # ------------------------------------------------- #
    # --- [3] plot                                  --- #
    # ------------------------------------------------- #
    fig     = pl1.plot1D( config=config, pngFile=pngFile )
    fig.add__plot( xAxis=time, yAxis=radi_A, label=label_A )
    fig.add__plot( xAxis=time, yAxis=radi_B, label=label_B )
    fig.add__legend()
    fig.set__axis()
    fig.save__figure()


    
# ========================================================= #
# ===   Execution of Pragram                            === #
# ========================================================= #

if ( __name__=="__main__" ):

    day     = 24 * 60 * 60.0
    pngFile = "png/radiative_equilibrium_basic_Ra225_Ac225.png"

    # ------------------------------------------------- #
    # --- [1] parameters                            --- #
    # ------------------------------------------------- #
    unit   = day
    N_A0   =  1.0
    name_A = "Ra-225"
    name_B = "Ac-225"
    T_A    = 14.9 # day
    T_B    =  9.9 # day
    t_Min  =  0.0 # day
    t_Max  = 80.0 # day
    nTime  = 101
    time   = np.linspace( t_Min, t_Max, nTime )

    # ------------------------------------------------- #
    # --- [2] calculation                           --- #
    # ------------------------------------------------- #
    ret = calculate__radiativeEquilibrium( name_A=name_A, name_B=name_B, \
                                           T_A=T_A, T_B=T_B, N_A0=N_A0, unit=unit )
    
    print( " T_A      :: {} (d)    ".format(   ret["T_A"]      ) )
    print( " T_B      :: {} (d)    ".format(   ret["T_B"]      ) )
    print( " lambda_A :: {} (s^-1) ".format(   ret["lambda_A"] ) )
    print( " lambda_B :: {} (s^-1) ".format(   ret["lambda_B"] ) )
    print( " T_max    :: {} (d)    ".format(   ret["T_max"]    ) )
    print( " NB_max   :: {} (Bq)   ".format(   ret["NB_max"]   ) )

    # ------------------------------------------------- #
    # --- [3] plot                                  --- #
    # ------------------------------------------------- #
    plot__radiativeEquilibrium( name_A=name_A, name_B=name_B, \
                                T_A=T_A, T_B=T_B, N_A0=N_A0, time=time, unit=unit, \
                                pngFile=pngFile )
