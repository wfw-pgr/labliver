import numpy as np

# ========================================================= #
# ===  activity_to_thickness.py                         === #
# ========================================================= #

def activity_to_thickness():

    N_Avogadro = 6.02e23
    
    # ------------------------------------------------- #
    # --- [1] load parameters                       --- #
    # ------------------------------------------------- #
    import json, re
    inpFile = "dat/parameters.jsonc"
    with open( inpFile, "r" ) as f:
        text   = re.sub(r'/\*[\s\S]*?\*/|//.*', '', f.read() )
        params = json.loads( text )
    
    # ------------------------------------------------- #
    # --- [2] conversion                            --- #
    # ------------------------------------------------- #
    params["n.atoms/cm3"] = N_Avogadro * params["rho.g/cm3"] / params["M.g/mol"]
    params["lambda.s^-1"] = np.log(2.0) / params["T1/2.s"]
    params["thick.cm"]    = params["Q.Bq"] / ( params["lambda.s^-1"] * \
                                               params["n.atoms/cm3"] * params["S.cm2"] )
    
    # ------------------------------------------------- #
    # --- [3] write results                         --- #
    # ------------------------------------------------- #
    rformat = "{0:>30} :: {1}\n"
    texts   = "\n[results]\n"
    for key,val in params.items():
        texts += rformat.format( key, val )
    print( texts )
    with open( params["outFile"], "w" ) as f:
        f.write( texts )
    return( texts )


# ========================================================= #
# ===   Execution of Pragram                            === #
# ========================================================= #

if ( __name__=="__main__" ):
    activity_to_thickness()
    
