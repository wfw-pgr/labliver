import os, sys
import numpy as np
import nkUtilities.load__config   as lcf
import nkUtilities.gplot1D        as gp1

flu_   = 4
labels = [ "0-10 degree", "10-20 degree", "20-30 degree", "30-40 degree", "50-60 degree" ]

# ------------------------------------------------- #
# --- [1] Data Loading                          --- #
# ------------------------------------------------- #
import nkUtilities.load__pointFile as lpf
inpFile = "dat/energy_vs_photons__requested.dat"
Data    = lpf.load__pointFile( inpFile=inpFile, returnType="structured" )
eAxis   = 0.5 * ( Data[0,:,2] + Data[0,:,3] )

# ------------------------------------------------- #
# --- [2] plot                                  --- #
# ------------------------------------------------- #
config   = lcf.load__config()
config_  = {
    "figure.size"        : [4.5,4.5],
    "figure.pngFile"     : "png/fluence_vs_angle.png", 
    "figure.position"    : [ 0.16, 0.16, 0.94, 0.94 ],
    "ax1.y.normalize"    : 1.0e0, 
    "ax1.x.range"        : { "auto":False, "min": 0.0, "max":50, "num":6 },
    "ax1.y.range"        : { "auto":False, "min": 1.0, "max":1.0e15, "num":6 },
    "ax1.x.label"        : "Energy (MeV)",
    "ax1.y.label"        : "Photons Rate (ph/s)",
    "ax1.y.log"          : True,
    "ax1.x.minor.nticks" : 1, 
    "plot.marker"        : "o",
    "plot.markersize"    : 3.0,
    "legend.fontsize"    : 9.0, 
}
config = { **config, **config_ }
    
fig    = gp1.gplot1D( config=config )
for ik,label in enumerate( labels ):
    fig.add__plot( xAxis=eAxis, yAxis=Data[ik,:,flu_], label=label )
fig.set__axis()
fig.set__legend()
fig.save__figure()
