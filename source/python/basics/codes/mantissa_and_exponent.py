
def mantissa_and_exponent( value ):
    import math
    if ( value == 0 ):
        return( 0, 0 )
    else:
        exponent = math.floor( math.log10( abs( value ) ) )
        mantissa = value / ( 10**exponent )
        return( mantissa, exponent )

# ========================================================= #
# ===   Execution of Pragram                            === #
# ========================================================= #

if ( __name__=="__main__" ):
    print( mantissa_and_exponent( 1.38e23 ) )
