import numpy as np

# ========================================================= #
# ===  calculate__criticalEnergy.py                     === #
# ========================================================= #

def calculate__criticalEnergy( Z=None ):

    coef = 820.0
    mec2 = 0.511
    Ec   = coef / Z - mec2    
    return( Ec )


# ========================================================= #
# ===   Execution of Pragram                            === #
# ========================================================= #

if ( __name__=="__main__" ):
    
    ret_Ta = calculate__criticalEnergy( Z=73 )
    ret_Pt = calculate__criticalEnergy( Z=78 )

    print( "Ta :: {}".format( ret_Ta )  )
    print( "Pt :: {}".format( ret_Pt )  )
