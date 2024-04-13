import os, sys
import numpy                      as np
import nkUtilities.plot1D         as pl1
import nkUtilities.load__config   as lcf
import nkUtilities.configSettings as cfs

# ------------------------------------------------- #
# --- [1] parameters                            --- #
# ------------------------------------------------- #
pngFile   = "png/cs__BreitWigner_Ra226_gn_Ra225.png"
datFile   = "dat/cs__BreitWigner_Ra226_gn_Ra225.dat"
mb        = 1e-3
mb2cm2    = 1e-27
MeV       = 1e6
Er        = 13.45 # * MeV
Et        = 6.4   # * MeV
Gamma     = 3.97  # * MeV
sigma_r   = 520   # * mb
Emin      = 0.0   # * MeV
Emax      = 50.0  # * MeV
nE        = 501

# ------------------------------------------------- #
# --- [2] calculate Breit-Wigner Formula        --- #
# ------------------------------------------------- #
EAxis     = np.linspace( Emin, Emax, nE )
amp       = sigma_r * ( EAxis / Er )
res       = ( 0.5*Gamma )**2 / ( ( EAxis-Er )**2 + ( 0.5*Gamma )**2 )
thr       = ( EAxis-Et ) / ( Er-Et )
thr       = np.sqrt( np.where( thr >= 0.0, thr, 0.0 ) )
cs        = amp * res * thr

# ------------------------------------------------- #
# --- [3] configure plot                        --- #
# ------------------------------------------------- #
x_,y_                    = 0, 1
config                   = lcf.load__config()
config                   = cfs.configSettings( configType="plot.def", config=config )
config["FigSize"]        = (4.5,4.5)
config["plt_position"]   = [ 0.16, 0.16, 0.94, 0.94 ]
config["plt_xAutoRange"] = False
config["plt_yAutoRange"] = False
config["plt_xRange"]     = [ 0.0, 50.0  ]
config["plt_yRange"]     = [ 0.0, 600.0 ]
config["xMajor_Nticks"]  = 11
config["yMajor_Nticks"]  = 7
config["plt_marker"]     = "o"
config["plt_markersize"] = 1.0
config["plt_linestyle"]  = "-"
config["plt_linewidth"]  = 1.0
config["xTitle"]         = "Energy (MeV)"
config["yTitle"]         = "Cross-section (mb)"

# ------------------------------------------------- #
# --- [4] plot                                  --- #
# ------------------------------------------------- #
fig     = pl1.plot1D( config=config, pngFile=pngFile )
fig.add__plot( xAxis=EAxis, yAxis=cs, label="Breit-Wigner (226Ra (g,n) 225Ra)" )
fig.add__legend()
fig.set__axis()
fig.save__figure()

