import os, sys
import numpy as np
import nkUtilities.load__config   as lcf
import nkUtilities.gplot1D        as gp1

R_tally  = 50.0
S_tally  = np.pi * R_tally**2
distance = 0.999

# ------------------------------------------------- #
# --- [1] fetch and rearange data               --- #
# ------------------------------------------------- #
import nkUtilities.load__pointFile as lpf
inpFiles  = [ "dat/angle/fluence_vs_angle_30MeV.dat", "dat/angle/fluence_vs_angle_35MeV.dat", \
              "dat/angle/fluence_vs_angle_40MeV.dat", "dat/angle/fluence_vs_angle_45MeV.dat", \
              "dat/angle/fluence_vs_angle_50MeV.dat", ]
engLabels = [ "30 MeV","35 MeV","40 MeV","45 MeV","50 MeV", ]

fluxList, rerrList = [], []
for ik,ifile in enumerate( inpFiles ):
    Data      = lpf.load__pointFile( inpFile=ifile, returnType="point" )
    alower    = ( Data[:,0] ) [:,np.newaxis]
    aupper    = ( Data[:,1] ) [:,np.newaxis]
    Sregion   = ( distance * np.tan( Data[:,1]/180.0*np.pi )**2 -
                  distance * np.tan( Data[:,0]/180.0*np.pi )**2 ) * np.pi
    fluxList += [ ( S_tally * Data[:,2] / Sregion )[:,np.newaxis] ] 
    rerrList += [ (           Data[:,3]           )[:,np.newaxis] ]
flux   = np.concatenate( fluxList, axis=1 )
rerr   = np.concatenate( rerrList, axis=1 )
Data   = np.concatenate( [ alower, aupper, flux, rerr ], axis=1 )

import nkUtilities.save__pointFile as spf
outFile   = "dat/angle/fluence_vs_angle.dat"
names     = [ "alower", "aupper",
              "photon(30MeV)", "photon(35MeV)", "photon(40MeV)",
              "photon(45MeV)", "photon(50MeV)",
              "rerr(30MeV)", "rerr(35MeV)", "rerr(40MeV)", "rerr(45MeV)", "rerr(50MeV)"  ]
spf.save__pointFile( outFile=outFile, Data=Data, names=names )


# ------------------------------------------------- #
# --- [2] plot data                             --- #
# ------------------------------------------------- #
config   = lcf.load__config()
config_  = {
    "figure.size"        : [4.5,4.5],
    "figure.pngFile"     : "png/fluence_vs_angle.png", 
    "figure.position"    : [ 0.16, 0.16, 0.94, 0.94 ],
    "ax1.y.normalize"    : 1.0e0, 
    "ax1.x.range"        : { "auto":False, "min": 0.0 , "max": 60.0, "num":7 },
    "ax1.y.range"        : { "auto":False, "min": 1.e11, "max":1.e15, "num":5 },
    "ax1.x.label"        : "Angle (deg.)",
    "ax1.y.label"        : "Fluence rate $\mathrm{(cm^{-2} MeV^{-1} s^{-1})}$",
    "ax1.x.minor.nticks" : 1,
    "ax1.y.log"          : True,
    "plot.marker"        : "o",
    "plot.markersize"    : 3.0,
    "legend.fontsize"    : 9.0, 
}
config = { **config, **config_ }

fig    = gp1.gplot1D( config=config )
energy = 0.5 * ( Data[:,0] + Data[:,1] )
for ik,label in enumerate( engLabels ):
    fig.add__plot( xAxis=energy, yAxis=Data[:,2+ik], label=label )
fig.set__axis()
fig.set__legend()
fig.save__figure()
