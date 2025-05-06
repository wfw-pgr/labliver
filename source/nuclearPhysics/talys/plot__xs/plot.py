import os, sys
import numpy                      as np
import nkUtilities.load__config   as lcf
import nkUtilities.gplot1D        as gp1

en_, xs_, = 0, 1,

# ------------------------------------------------- #
# --- [1] load data                             --- #
# ------------------------------------------------- #
DataDict  = {}
inpFiles  = { "(g,n)" :"xs/xs__rp088225.tot", \
              "(g,2n)":"xs/xs__rp088224.tot", \
              "(g,3n)":"xs/xs__rp088223.tot", \
              "(g,p)" :"xs/xs__rp087225.tot", \
              "(g,2p)":"xs/xs__rp086224.tot", \
}
legends   = { "(g,n)" : "$\mathrm{^{226}Ra(\gamma,n)^{225}Ra}$" , \
              "(g,2n)": "$\mathrm{^{226}Ra(\gamma,2n)^{224}Ra}$", \
              "(g,3n)": "$\mathrm{^{226}Ra(\gamma,3n)^{223}Ra}$", \
              "(g,p)" : "$\mathrm{^{226}Ra(\gamma,p)^{225}Fr}$", \
              "(g,2p)": "$\mathrm{^{226}Ra(\gamma,2p)^{224}Rn}$", \
}

for tag,ifile in inpFiles.items():
    with open( ifile, "r" ) as f:
        DataDict[tag] = np.loadtxt( f )
        
# ------------------------------------------------- #
# --- [2] plot graph                            --- #
# ------------------------------------------------- #
config   = lcf.load__config()
config_  = {
    "figure.size"        : [4.5,4.5],
    "figure.pngFile"     : "Ra226_g.png", 
    "figure.position"    : [ 0.16, 0.16, 0.94, 0.94 ],
    "ax1.y.normalize"    : 1.0e0, 
    "ax1.x.range"        : { "auto":False, "min": 0.0, "max":50.0, "num": 6 },
    "ax1.y.range"        : { "auto":False, "min": 0.0, "max":500., "num": 6 },
    "ax1.x.label"        : "Energy (MeV)",
    "ax1.y.label"        : "Cross section (mb)",
    "ax1.x.minor.nticks" : 1, 
    "plot.marker"        : "o",
    "plot.markersize"    : 3.0,
    "legend.fontsize"    : 9.0, 
}
log_config_ = {
    "figure.pngFile"     : "Ra226_g_log.png", 
    "ax1.y.log"          : True,
    "ax1.y.range"        : { "auto":False, "min": 1.0, "max":1.e3, "num": 4 },
}

config = { **config, **config_ }
config = { **config, **log_config_ }
    
fig    = gp1.gplot1D( config=config )
for tag,Data in DataDict.items():
    fig.add__plot( xAxis=Data[:,en_], yAxis=Data[:,xs_], label=legends[tag] )
fig.set__axis()
fig.set__legend()
fig.save__figure()
