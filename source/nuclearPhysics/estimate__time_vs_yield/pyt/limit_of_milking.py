import os, sys, json5
import numpy                      as np
import nkUtilities.plot1D         as pl1
import nkUtilities.load__config   as lcf
import nkUtilities.configSettings as cfs


# ========================================================= #
# ===  limit_of_milking.py                              === #
# ========================================================= #

def limit_of_milking():
 
    n_,m_,t_ = 0, 1, 2
    T1       = 14.9        # days
    T2       = 9.9         # days
    day      = 24.0*3600.

    # ------------------------------------------------- #
    # --- [1] calculate constants                   --- #
    # ------------------------------------------------- #
    lamb1    = np.log(2.0) / ( T1*day )
    lamb2    = np.log(2.0) / ( T2*day )
    Tmax     = np.log( lamb1/lamb2 )  / ( lamb1 - lamb2 )
    e1       = np.exp( (-1.)*lamb1*Tmax )
    e2       = np.exp( (-1.)*lamb2*Tmax )
    limit    = lamb2/( lamb2-lamb1 ) * ( e1-e2 )/( 1.0-e1 )

    # ------------------------------------------------- #
    # --- [2] prepare nAxis and execution           --- #
    # ------------------------------------------------- #
    ntimes   = np.linspace( 1.0, 20.0, 20 )
    milkFunc = lambda n: lamb2/( lamb2-lamb1 )*( e1-e2 )*np.exp( -(n-1)*lamb1*Tmax )
    milked   = milkFunc ( ntimes   )
    total    = np.cumsum( milked )
    Data     = np.concatenate( [ ntimes[:,np.newaxis], milked[:,np.newaxis], \
                                 total[:,np.newaxis] ], axis=1 )

    # ------------------------------------------------- #
    # --- [3] plot 1d                               --- #
    # ------------------------------------------------- #
    pngFile                  = "png/limit_of_milking.png"
    config                   = lcf.load__config()
    config["FigSize"]        = (4.5,4.5)
    config["plt_position"]   = [ 0.16, 0.16, 0.94, 0.94 ]
    config["plt_xAutoRange"] = False
    config["plt_yAutoRange"] = False
    config["plt_xRange"]     = [ 0.0,  8.0 ]
    config["plt_yRange"]     = [ 0.0,  1.2 ]
    config["xMajor_Nticks"]  =  9
    config["yMajor_Nticks"]  =  7
    config["plt_marker"]     = "o"
    config["plt_markersize"] = 3.0
    config["plt_linestyle"]  = "-"
    config["plt_linewidth"]  = 2.0
    config["xTitle"]         = "n"
    config["yTitle"]         = "Normalized activity"

    fig     = pl1.plot1D( config=config, pngFile=pngFile )
    fig.add__plot( xAxis=Data[:,n_], yAxis=Data[:,t_], color="C1", \
                   label="$\sum _n \ A_{Ac-225}^{(n)}/A_{Ra-225}^{EOB}$" )
    fig.add__bar( xAxis=Data[:,n_], yAxis=Data[:,m_], color="C0",\
                  label="$A_{Ac-225}^{(n)}/A_{Ra-225}^{EOB}$" )
    fig.add__cursor( yAxis=0.802, color="Gray" , linestyle="--" )
    fig.add__cursor( yAxis=1.000, color="Green", linestyle="--" )
    fig.add__cursor( yAxis=0.640, color="C5"   , linestyle="--" )
    fig.set__axis()
    fig.add__legend()
    fig.save__figure()


    


# ========================================================= #
# ===   Execution of Pragram                            === #
# ========================================================= #

if ( __name__=="__main__" ):
    limit_of_milking()
