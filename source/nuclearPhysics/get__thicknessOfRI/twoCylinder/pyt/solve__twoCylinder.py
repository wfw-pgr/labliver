import json5
import numpy          as np
import scipy.optimize as opt

# ========================================================= #
# ===  solve__twoCylinder.py                            === #
# ========================================================= #

def solve__twoCylinder( paramsFile="dat/parameters_twoCylinder.json" ):

    x_, y_, z_ = 0, 1, 2
    NA         = 6.02e23
    mm2cm      = 0.1
    
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
    V0    = numer / denom # cm3

    # ------------------------------------------------- #
    # --- [3] calculate surface area                --- #
    # ------------------------------------------------- #
    S_disk_front = 0.25*np.pi*params["container.D1"]**2 * mm2cm**2
    S_disk_back  = 0.25*np.pi*params["container.D2"]**2 * mm2cm**2
    S_side_1     = np.pi * params["container.D1"] * params["container.H1"] * mm2cm**2
    S_side_2     = np.pi * params["container.D2"] * params["container.H2"] * mm2cm**2
    S0           = S_disk_front + S_disk_back + S_side_1 + S_side_2     # cm2

    # ------------------------------------------------- #
    # --- [4] calculate container volume            --- #
    # ------------------------------------------------- #
    V_front      = 0.25*np.pi*params["container.D1"]**2 * params["container.H1"] * mm2cm**3
    V_back       = 0.25*np.pi*params["container.D2"]**2 * params["container.H2"] * mm2cm**3
    V_total      = V_front + V_back
    print(  )
    
    # ------------------------------------------------- #
    # --- [4] calculate thickness                   --- #
    # ------------------------------------------------- #
    t0 = V0 / S0
    print()
    print( " t :: {0} (cm) ".format( t0 ) )
    print( " S :: {0} (cm2)".format( S0 ) ) 
    print( " V :: {0} (cm3)".format( V0 ) )
    print( " V (vessel) :: {0} (cm3)".format( V_total ) )
    print()
    ret = [ t0, S0, V0 ]
    return( ret )


# ========================================================= #
# ===   Execution of Pragram                            === #
# ========================================================= #

if ( __name__=="__main__" ):
    paramsFile = "dat/parameters_twoCylinder.json"
    ret = solve__twoCylinder( paramsFile=paramsFile )
    print( ret )
