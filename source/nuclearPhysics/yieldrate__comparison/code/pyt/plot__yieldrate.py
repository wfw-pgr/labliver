import numpy as np
import nkUtilities.load__config   as lcf
import nkUtilities.gplot1D        as gp1

# ========================================================= #
# ===  plot__yieldrate.py                               === #
# ========================================================= #

def plot__yieldrate():

    x_, y_ = 0, 1
    
    # ------------------------------------------------- #
    # --- [1] data                                  --- #
    # ------------------------------------------------- #
    xAxis      = np.linspace( 0.0, 150.0, 101 )
    rate1      = 16.0    # (nCi/mg/uA/h)
    rate2      =  2.7
    p1         = 10.5    # (kW)
    p2         = 125.0
    kW2uA      = 1.0e3 / 40.0e6 / 1e-6
    nCi2GBq    = 1e-9  * 37e9 / 1e9
    duration   = 24.0    # (h)
    amount     = 300.0   # (mg)
    coef1      = rate1 * nCi2GBq * kW2uA * duration * amount
    coef2      = rate2 * nCi2GBq * kW2uA * duration * amount
    scaling1   = coef1 * xAxis
    scaling2   = coef2 * xAxis
    pt1        = np.array( [ p1, coef1*p1 ] )
    pt2        = np.array( [ p2, coef2*p2 ] )
    print( pt1 )
    print( pt2 )
    
    # ------------------------------------------------- #
    # --- [2] plotting                              --- #
    # ------------------------------------------------- #
    config   = lcf.load__config()
    config_  = {
        "figure.size"        : [4.5,4.5],
        "figure.pngFile"     : "png/plot__yieldrate.png", 
        "figure.position"    : [ 0.16, 0.16, 0.94, 0.94 ],
        "ax1.y.normalize"    : 1.0e0, 
        "ax1.x.range"        : { "auto":False, "min": 0.0, "max":140.0, "num": 8 },
        "ax1.y.range"        : { "auto":False, "min": 0.0, "max":  5.0, "num":11 },
        "ax1.x.label"        : "Beam power (kW)",
        "ax1.y.label"        : "Yield Amount (GBq/d)",
        "ax1.x.minor.nticks" : 1, 
        "plot.marker"        : None,
        "plot.markersize"    : 6.0,
        "legend.fontsize"    : 9.0, 
    }
    config = { **config, **config_ }
    fig    = gp1.gplot1D( config=config )
    fig.add__plot( xAxis=xAxis, yAxis=scaling1 , color="C0", linestyle="--" )
    fig.add__plot( xAxis=xAxis, yAxis=scaling2 , color="C1", linestyle="--" )
    fig.add__plot( xAxis=pt1[x_], yAxis=pt1[y_], color="C0", marker="D", linestyle=None )
    fig.add__plot( xAxis=pt2[x_], yAxis=pt2[y_], color="C1", marker="o", linestyle=None )
    fig.set__axis()
    fig.save__figure()


# ========================================================= #
# ===   Execution of Pragram                            === #
# ========================================================= #

if ( __name__=="__main__" ):
    plot__yieldrate()
