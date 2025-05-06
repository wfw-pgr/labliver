import json5
import numpy          as np
import scipy.optimize as opt


# ========================================================= #
# ===  solve__thickOfCone.py                            === #
# ========================================================= #

def solve__thickOfCone( paramsFile="dat/parameters_cone.json" ):

    x_, y_, z_ = 0, 1, 2
    NA         = 6.02e23
    
    # ------------------------------------------------- #
    # --- [1] load parameters                       --- #
    # ------------------------------------------------- #
    with open( paramsFile, "r" ) as f:
        params = json5.load( f )
    timeUnit = { "y":365.0*24*3600., "d": 24*3600., "h": 3600., "m":60.0, "s":1.0 }
    Thalf    = params["target.halftime"][0] * timeUnit[ params["target.halftime"][1] ]
    
    # ------------------------------------------------- #
    # --- [2] calculate volume                      --- #
    # ------------------------------------------------- #
    numer = params["target.g/mol"] * params["target.activity"] * Thalf
    denom = params["target.density"] * NA * np.log(2)
    V0    = numer / denom
    
    # ------------------------------------------------- #
    # --- [3] calculate height                      --- #
    # ------------------------------------------------- #
    mm2cm = 0.1
    R3    = 0.5 * params["container.D3"] * mm2cm
    R1    = 0.5 * params["container.D1"] * mm2cm
    H0    =       params["container.H0"] * mm2cm
    c3    = ( R3-R1 )**2
    c2    = ( R3-R1 )*R1*3.0
    c1    = 3.0*R1
    c0    = (-3.0) * V0 / ( np.pi * H0 )
    args  = ( c3, c2, c1, c0 )

    def func( x, c3, c2, c1, c0 ):
        return( c3 * x**3 + c2 * x**2 + c1 * x + c0 )
    
    h     = opt.brentq( func, 0.0, H0, args=args )
    R2    = ( R3-R1 )/H0 * h + R1
    R2_mm = R2 * 10.0
    h__mm =  h * 10.0
    ret   =  [ h__mm, R2_mm ]
    print( " h  :: {0} (mm)  = {1} (cm) ".format( h__mm, h  ) )
    print( " R2 :: {0} (mm)  = {1} (cm) ".format( R2_mm, R2 ) )
    return( ret )


# ========================================================= #
# ===   Execution of Pragram                            === #
# ========================================================= #

if ( __name__=="__main__" ):
    paramsFile = "dat/parameters_cone.json"
    ret = solve__thickOfCone( paramsFile=paramsFile )
    print( ret )
