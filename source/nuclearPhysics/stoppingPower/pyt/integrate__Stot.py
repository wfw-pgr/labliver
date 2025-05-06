import os, sys
import numpy as np
import scipy.interpolate

# ========================================================= #
# ===  integrate__Stot.py                               === #
# ========================================================= #

def integrate__Stot():
    
    E0         = 44.5
    # Ecut       = 1.0e-3
    Ecut       = 10.7  # Ec for Ta #
    Ecut       = 10.0  # Ec for Pt #
    nE         = 1001

    dEdxInv    = Bethe_Bloch_forStotInv( E0 )
    print( "E0          :: {}".format( E0 ) )
    print( "1/<dE/dx>   :: {}".format( dEdxInv ) )
    print( "E0/<dE/dx>  :: {}".format( E0*dEdxInv ) )
    
    # ------------------------------------------------- #
    # --- [1] define data                           --- #
    # ------------------------------------------------- #
    energy  = np.linspace( Ecut, E0, nE )
    StotInv = Bethe_Bloch_forStotInv( energy )

    # ------------------------------------------------- #
    # --- [2] integrate data                        --- #
    # ------------------------------------------------- #
    simps   = scipy.integrate.simpson( StotInv, energy )
    gquad   = scipy.integrate.quad( Bethe_Bloch_forStotInv, Ecut, E0 )
    print( "simpson     :: {}".format( simps ) )
    print( "gauss-quad  :: {}".format( gquad ) )
    return()



# ========================================================= #
# ===  Bethe-Bloch for Stot                             === #
# ========================================================= #
def Bethe_Bloch_forStotInv( energy ):

    # ------------------------------------------------- #
    # --- [1] parameters                            --- #
    # ------------------------------------------------- #
    # -- Pt -- #
    A         = 193.0
    Z         = 78.0
    rho       = 21.45
    # -- Ta -- #
    # A         = 181.0
    # Z         = 73.0
    # rho       = 16.65
    
    mi        = 9.109e-31
    zi        = 1.0
    
    # ------------------------------------------------- #
    # --- [2] constant                              --- #
    # ------------------------------------------------- #
    me        = 9.109e-31 # (kg)
    qe        = 1.602e-19 # (C)
    cv        = 2.998e+8  # (m/s)
    epsilon0  = 8.854e-12 # (F/m)
    amu       = 1.660e-27 # (kg)
    
    # ------------------------------------------------- #
    # --- [3] unit                                  --- #
    # ------------------------------------------------- #
    gcm3_kgm3 = 1.0e+3    # g/cm3 -> kg/m3
    J2MeV     = 1.e-6/qe  # Joule -> MeV
    MeV2J     = 1.e+6*qe  # MeV   -> Joule 
    m2mm      = 1.0e+3    # m     -> mm
    
    # ------------------------------------------------- #
    # --- [4] Scol calculation                      --- #
    # ------------------------------------------------- #
    Iaep      = 10.0 * qe * Z
    ne        = ( Z/A ) * ( rho*gcm3_kgm3 /amu )  #  rho/amu: #.of nuclei, Z/A : nuclei -> e
    beta      = np.sqrt( 1.0 - ( ( mi*cv**2*J2MeV ) / ( energy + mi*cv**2*J2MeV ) )**2 )
    prod1     = ( qe**2 / ( 4.0*np.pi * epsilon0 ) )**2
    prod2     = ( 4.0*np.pi * ne * zi**2 ) / ( me * beta**2 * cv**2 )
    logterm   = np.log( ( 2.0*me*beta**2*cv**2 ) / ( Iaep*( 1.0-beta**2 ) ) ) - beta**2
    Scol      = prod1 * prod2 * logterm * J2MeV / m2mm

    # ------------------------------------------------- #
    # --- [5] Srad calculation                      --- #
    # ------------------------------------------------- #
    coef        = 1.0 / 820.0
    mec2        = 0.511
    Srad        = coef * Z * ( energy + mec2 ) * Scol
    
    # ------------------------------------------------- #
    # --- [6] Stot calculation                      --- #
    # ------------------------------------------------- #
    Stot        = Scol + Srad
    # StotInv     = 1.0 / Scol
    # StotInv     = 1.0 / Srad
    StotInv     = 1.0 / Stot
    return( StotInv )



# ========================================================= #
# ===   Execution of Pragram                            === #
# ========================================================= #

if ( __name__=="__main__" ):
    integrate__Stot()
