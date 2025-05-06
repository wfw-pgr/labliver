import os, sys, json5
import numpy                      as np
import nkUtilities.plot1D         as pl1
import nkUtilities.load__config   as lcf
import nkUtilities.configSettings as cfs

min_, max_, num_ = 0, 1, 2

# ------------------------------------------------- #
# --- [1] constant                              --- #
# ------------------------------------------------- #
me               = 9.109e-31 # (kg)
qe               = 1.602e-19 # (C)
cv               = 2.998e+8  # (m/s)
epsilon0         = 8.854e-12 # (F/m)
amu              = 1.660e-27 # (kg)

# ------------------------------------------------- #
# --- [2] unit                                  --- #
# ------------------------------------------------- #
gcm3_kgm3        = 1.0e+3    # g/cm3 -> kg/m3
J2MeV            = 1.e-6/qe  # Joule -> MeV
MeV2J            = 1.e+6*qe  # MeV   -> Joule 
m2mm             = 1.0e+3    # m     -> mm


# ========================================================= #
# ===  display each formula                             === #
# ========================================================= #

def display():

    # ------------------------------------------------- #
    # --- [1] load parameters                       --- #
    # ------------------------------------------------- #
    inpFile = "dat/parameter__e_in_Ta.json"
    with open( inpFile, "r" ) as f:
        params = json5.load( f )
        
    # ------------------------------------------------- #
    # --- [2] energy axis                           --- #
    # ------------------------------------------------- #
    if ( params["Scol.eAxis.logarithm"] ):
        Rmaxmin = params["Scol.eAxis.MinMaxNum"][max_] / params["Scol.eAxis.MinMaxNum"][min_]
        seed    = np.linspace( 0.0, np.log10( Rmaxmin ), params["Scol.eAxis.MinMaxNum"][num_] )
        energy  = params["Scol.eAxis.MinMaxNum"][min_] * 10.0**( seed )
    else:
        energy  = np.linspace( *params["Scol.eAxis.MinMaxNum"] )
    
    # ------------------------------------------------- #
    # --- [3] calculate stopping power              --- #
    # ------------------------------------------------- #
    Scol  = Bethe_Bloch_Formula  ( energy=energy, params=params )
    # Srad  = Bethe_Heitler_Formula( energy=energy, params=params )
    Srad  = Bethe_Bloch_radiation( energy=energy, params=params )
    Stot  = Scol + Srad
    ratio = Srad / Stot * 100.0
    Data  = np.concatenate( [ energy[:,np.newaxis], Scol[:,np.newaxis], Srad [:,np.newaxis], \
                              Stot[:,np.newaxis]  , ratio[:,np.newaxis] ], axis=1 )
    import nkUtilities.save__pointFile as spf
    names = [ "energy", "Scol", "Srad", "Stot", "Srad/Stot" ]
    spf.save__pointFile( outFile=params["outFile"], Data=Data, names=names )


    # ------------------------------------------------- #
    # --- [4] plot (Scol,Srad,Stot)                 --- #
    # ------------------------------------------------- #
    config                   = lcf.load__config()
    config["FigSize"]        = (4.5,4.5)
    config["plt_position"]   = [ 0.18, 0.18, 0.94, 0.94 ]
    config["plt_xAutoRange"] = False
    config["plt_yAutoRange"] = False
    config["plt_xRange"]     = params["plot.xAxis.MinMaxNum"][0:2]
    config["plt_yRange"]     = params["plot.yAxis.MinMaxNum"][0:2]
    config["xMajor_Nticks"]  = params["plot.xAxis.MinMaxNum"][2]
    config["yMajor_Nticks"]  = params["plot.xAxis.MinMaxNum"][2]
    config["xTitle"]         = params["plot.xAxis.title"]
    config["yTitle"]         = params["plot.yAxis.title"]
    config["plt_xlog"]       = params["plot.xAxis.log"]
    config["plt_ylog"]       = params["plot.yAxis.log"]
    config["plt_marker"]     = "o"
    config["plt_markersize"] = 3.0
    config["plt_linestyle"]  = "-"
    config["plt_linewidth"]  = 2.0
    
    fig     = pl1.plot1D( config=config, pngFile=params["plot.pngFile"] )
    fig.add__plot( xAxis=energy, yAxis=Scol, label="Scol" )
    fig.add__plot( xAxis=energy, yAxis=Srad, label="Srad" )
    fig.add__plot( xAxis=energy, yAxis=Stot, label="Stot" )
    fig.set__axis()
    fig.add__legend()
    fig.save__figure()

    # ------------------------------------------------- #
    # --- [4] plot (fraction)                       --- #
    # ------------------------------------------------- #
    config["plt_xAutoRange"] = False
    config["plt_yAutoRange"] = False
    config["plt_xRange"]     = params["plot.xAxis.MinMaxNum"][0:2]
    config["plt_yRange"]     = [ 0.0, 120.0 ]
    config["xMajor_Nticks"]  = params["plot.xAxis.MinMaxNum"][2]
    config["yMajor_Nticks"]  = 7
    config["xTitle"]         = params["plot.xAxis.title"]
    config["yTitle"]         = "Radiation ratio (%)"
    config["plt_xlog"]       = params["plot.xAxis.log"]
    config["plt_ylog"]       = False
    config["plt_marker"]     = "o"
    config["plt_markersize"] = 3.0
    config["plt_linestyle"]  = "-"
    config["plt_linewidth"]  = 2.0
    
    fig     = pl1.plot1D( config=config, pngFile=params["plot.pngFile.ratio"] )
    fig.add__plot( xAxis=energy, yAxis=ratio )
    fig.set__axis()
    fig.save__figure()
    return()

    return()


# ========================================================= #
# ===  convert__energy2beta ( MeV -> beta )             === #
# ========================================================= #
def convert__energy2beta( kineticE=None, mi=None ):
    beta = np.sqrt( 1.0 - ( ( mi * cv**2 * J2MeV ) / ( kineticE + mi * cv**2 * J2MeV ) )**2 )
    return( beta )


# ========================================================= #
# ===  Bethe-Bloch Formula                              === #
# ========================================================= #
def Bethe_Bloch_Formula( energy=None, params=None ):
    A,Z,rho     = params["target.A"], params["target.Z"], params["target.rho"]
    mi, zi      = params["incident.mass"], params["incident.valent"]
    Iaep        = 10.0 * qe * Z
    ne          = ( Z/A ) * ( rho*gcm3_kgm3 /amu )  #  rho/amu: #.of nuclei, Z/A : nuclei -> e
    beta        = convert__energy2beta( kineticE=energy, mi=mi )
    prod1       = ( qe**2 / ( 4.0*np.pi * epsilon0 ) )**2
    prod2       = ( 4.0*np.pi * ne * zi**2 ) / ( me * beta**2 * cv**2 )
    logterm     = np.log( ( 2.0*me*beta**2*cv**2 ) / ( Iaep*( 1.0-beta**2 ) ) ) - beta**2
    ret         = prod1 * prod2 * logterm * J2MeV / m2mm
    return( ret )
        

# ========================================================= #
# ===  Bethe-Heitler Formula                            === #
# ========================================================= #
def Bethe_Heitler_Formula( energy=None, params=None ):
    A,Z,rho     = params["target.A"], params["target.Z"], params["target.rho"]
    mecv2       = me  * cv**2
    ne          = ( Z/A ) * ( rho*gcm3_kgm3 /amu )
    coef        = ne * (Z+1)/137.0 * ( qe**2/mecv2 )**2 * energy * MeV2J
    logterm     = 4.0 * np.log( 2.0 * energy * MeV2J / ( mecv2) ) - 4.0/3.0
    ret         = coef * logterm * J2MeV / m2mm
    print( coef )
    print( coef * J2MeV / m2mm )
    sys.exit()
    return( ret )


# ========================================================= #
# ===  Bethe-Bloch for radiation                        === #
# ========================================================= #
def Bethe_Bloch_radiation( energy=None, params=None ):
    coef        = 1.0 / 820.0
    mec2        = 0.511
    BetheBloch  = Bethe_Bloch_Formula( energy=energy, params=params )
    ret         = coef * params["target.Z"] * ( energy + mec2 ) * BetheBloch
    return( ret )


# ========================================================= #
# ===   Execution of Pragram                            === #
# ========================================================= #
if ( __name__=="__main__" ):
    display()
