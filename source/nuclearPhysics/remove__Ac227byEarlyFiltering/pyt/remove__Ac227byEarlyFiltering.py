import sys, json5
import numpy                       as np
import nkUtilities.load__config    as lcf
import nkUtilities.plot1D          as pl1
import nkUtilities.configSettings  as cfs
import nkUtilities.save__pointFile as spf


# ========================================================= #
# ===  solve__cascadeReaction                           === #
# ========================================================= #

def solve__cascadeReaction( time=None, T_A=1.0, T_B=1.0, N_A0=1.0, unit=1.0 ):

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
    nRel_A   =   nNum_A / nNum_A[0]
    nRel_B   =   nNum_B / nNum_A[0]
    
    # ------------------------------------------------- #
    # --- [3] return                                --- #
    # ------------------------------------------------- #
    ret = { "nNum_A":nNum_A, "nNum_B":nNum_B, "radi_A":radi_A, "radi_B":radi_B, \
            "coef_A":coef_A, "atte_A":atte_A, "coef_B":coef_B, "atte_B":atte_B, \
            "nRel_A":nRel_A, "nRel_B":nRel_B, \
            "lambda_A":lambda_A, "lambda_B":lambda_B,  \
            "T_max":T_max, "T_A":T_A, "T_B":T_B, "time":time, "NB_max":NB_max }
    return( ret )
    

# ========================================================= #
# ===  remove__Ac227byEarlyFiltering                    === #
# ========================================================= #

def remove__Ac227byEarlyFiltering( inpFile="dat/parameters.json" ):

    na_ = np.newaxis
    
    # ------------------------------------------------- #
    # --- [1] load parameters                       --- #
    # ------------------------------------------------- #
    import nkUtilities.json__formulaParser as jso
    params = jso.json__formulaParser( inpFile=inpFile )
    time1  = np.linspace( params["time.min.01"], params["time.max.01"], params["time.num.01"] )
    time2  = np.linspace( params["time.min.02"], params["time.max.02"], params["time.num.02"] )
    time1  = time1 * params["time.unit.01"]
    time2  = time2 * params["time.unit.02"]

    # ------------------------------------------------- #
    # --- [2] calculation                           --- #
    # ------------------------------------------------- #
    ret1 = solve__cascadeReaction( time=time1, \
                                   T_A =params["halflife.1A"], T_B =params["halflife.1B"], \
                                   N_A0=params["produced.1A"], unit=params["halflife.unit"] )
    ret2 = solve__cascadeReaction( time=time2, \
                                   T_A =params["halflife.2A"], T_B =params["halflife.2B"], \
                                   N_A0=params["produced.2A"], unit=params["halflife.unit"] )
    
    # ------------------------------------------------- #
    # --- [3] preparation plot                      --- #
    # ------------------------------------------------- #
    names     = [ "name.1A", "name.1B", "name.2A", "name.2B" ]
    labels    = [ "$A_{"+"{}".format( params[name] )+"}$" for name in names ]
    labels[3] = labels[3] + " $/10^{-5}$"
    
    # ------------------------------------------------- #
    # --- [4] plot config                           --- #
    # ------------------------------------------------- #
    config                   = lcf.load__config()
    config                   = cfs.configSettings( configType="plot.def", config=config )
    config["FigSize"]        = (9.0,3.0)
    config["plt_position"]   = [ 0.08, 0.18, 0.97, 0.96 ]
    config["plt_xAutoRange"] = False
    config["plt_yAutoRange"] = False
    config["plt_marker"]     = "none"
    config["plt_linestyle"]  = "-"
    config["plt_linewidth"]  = 2.0
    config["xTitle"]         = "elapsed time (d)"
    config["yTitle"]         = "$A / A_0$ (a.u.)"

    # ------------------------------------------------- #
    # --- [5] plot                                  --- #
    # ------------------------------------------------- #
    config["plt_xRange"]     = [ 0.0, 40.0 ]
    config["plt_yRange"]     = [ 0.0, 1.0  ]
    config["xMajor_Nticks"]  =   9
    config["yMajor_Nticks"]  =   6
    time1 = time1/params["time.unit.01"]
    fig   = pl1.plot1D( config=config, pngFile=params["general.pngFile.01"] )
    fig.add__plot( xAxis=time1, yAxis=ret1["radi_A"], label=labels[0], color="C0" )
    fig.add__plot( xAxis=time1, yAxis=ret1["radi_B"], label=labels[1], color="C1" )
    fig.add__legend()
    fig.set__axis()
    fig.save__figure()

    config["plt_xRange"]     = [ 0.0, 0.2 ]
    config["plt_yRange"]     = [ 0.0, 1.0 ]
    config["xMajor_Nticks"]  =   11
    config["yMajor_Nticks"]  =   6
    time2 = time2 / params["time.unit.02"]
    fig   = pl1.plot1D( config=config, pngFile=params["general.pngFile.02"] )
    fig.add__plot( xAxis=time2, yAxis=ret2["radi_A"]/params["normalize.2A"], label=labels[2],\
                   color="C2" )
    fig.add__plot( xAxis=time2, yAxis=ret2["radi_B"]/params["normalize.2B"], label=labels[3],\
                   color="C3" )
    fig.add__legend()
    fig.set__axis()
    fig.save__figure()

    config["plt_xRange"]     = [ 0.0, 20.0 ]
    config["plt_yRange"]     = [ 0.0, 1.2  ]
    config["xMajor_Nticks"]  =   11
    config["yMajor_Nticks"]  =   7
    fig   = pl1.plot1D( config=config, pngFile=params["general.pngFile.03"] )
    fig.add__plot( xAxis=time2, yAxis=ret1["radi_A"], \
                   label=labels[0], color="C0" )
    fig.add__plot( xAxis=time2, yAxis=ret1["radi_B"], \
                   label=labels[1], color="C1" )
    fig.add__plot( xAxis=time2, yAxis=ret2["radi_A"]/params["normalize.2A"], \
                   label=labels[2], color="C2" )
    fig.add__plot( xAxis=time2, yAxis=ret2["radi_B"]/params["normalize.2B"], \
                   label=labels[3], color="C3" )
    fig.add__legend()
    fig.set__axis()
    fig.save__figure()

    # ------------------------------------------------- #
    # --- [6] save in a file                        --- #
    # ------------------------------------------------- #
    Data1 = [ time1[:,na_], \
              ret1["radi_A"][:,na_], ret1["radi_B"][:,na_], \
              ret1["nNum_A"][:,na_], ret1["nNum_B"][:,na_], \
              ret1["nRel_A"][:,na_], ret1["nRel_B"][:,na_] ]
    Data2 = [ time2[:,na_], \
              ret2["radi_A"][:,na_], ret2["radi_B"][:,na_], \
              ret2["nNum_A"][:,na_], ret2["nNum_B"][:,na_], \
              ret2["nRel_A"][:,na_], ret2["nRel_B"][:,na_] ]
    Data1 = np.concatenate( Data1, axis=1 )
    Data2 = np.concatenate( Data2, axis=1 )
    spf.save__pointFile( outFile=params["general.outFile.01"], Data=Data1 )
    spf.save__pointFile( outFile=params["general.outFile.02"], Data=Data2 )


# ========================================================= #
# ===   Execution of Pragram                            === #
# ========================================================= #

if ( __name__=="__main__" ):
    remove__Ac227byEarlyFiltering()
