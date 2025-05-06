import json5
import scipy as sp
import numpy                      as np
import nkUtilities.load__config   as lcf
import nkUtilities.gplot1D        as gpl
import nkUtilities.configSettings as cfs


# ========================================================= #
# ===  display                                          === #
# ========================================================= #
def display():
    
    t_, NA_, NB_, AA_, AB_, CB_, RM_ = 0, 1, 2, 3, 4, 5, 6
    
    # ------------------------------------------------- #
    # --- [1] Arguments                             --- #
    # ------------------------------------------------- #
    datFiles = [ "dat/result_rec0999_sch43.dat",
                 "dat/result_rec0990_sch43.dat",
                 "dat/result_rec0980_sch43.dat",
                 "dat/result_rec0950_sch43.dat",
                 "dat/result_rec0900_sch43.dat",
                 "dat/result_rec0800_sch43.dat", 
    ]
    labels   = [ "99.9(%)", "99(%)", "98(%)", "95(%)", "90(%)", "80(%)" ]

    # ------------------------------------------------- #
    # --- [2] Fetch Data                            --- #
    # ------------------------------------------------- #
    import nkUtilities.load__pointFile as lpf
    DataList = [ lpf.load__pointFile( inpFile=datFile, returnType="point" )
                 for datFile in datFiles ]

    p365 = []
    recl = [ 99.9, 99, 98, 95, 90, 80 ]
    for ik,Data in enumerate(DataList):
        func1 = sp.interpolate.interp1d( Data[:,t_], Data[:,CB_], kind="nearest" )
        func2 = sp.interpolate.interp1d( Data[:,t_], Data[:,RM_], kind="nearest" )
        p365 += [ [ recl[ik], func1(365.0), func2(365.0) ] ]
    p365 = np.array( p365 )

    # ------------------------------------------------- #
    # --- [3] theoretical limit of recyling         --- #
    # ------------------------------------------------- #
    assume = { "Ra226.Bq"     : 11.1e9,
               "dt.s"         : 6.0*24.0*3600.0,
               "Ibeam.uA"     : 300.0,
               "tHalf.Ra-226" : 1600 * 365*24*3600.0, 
               "tHalf.Ra-225" :       14.9*24*3600.0,
               "Y.efficiency" : 1.38e-8,   # Bq(Ra225) / ( Bq(Ra226).uA.s )
    }
    yielded    = assume["Y.efficiency"]*assume["Ra226.Bq"]*assume["Ibeam.uA"]*assume["dt.s"]
    Ra226_loss = assume["tHalf.Ra-225"] / assume["tHalf.Ra-226"] * yielded
    rec_limit  = ( assume["Ra226.Bq"] - Ra226_loss ) / assume["Ra226.Bq"] * 100
    
    print( "converted Ra-225              (MBq)   :: {}".format( yielded/1e6    ) )
    print( "converted Ra-226 loss         (MBq)   :: {}".format( Ra226_loss/1e6 ) )
    print( "theoretical limit of recycling  (%)   :: {}".format( rec_limit      ) )

        
    # ------------------------------------------------- #
    # --- [3] plot Figure ( time-inventory )        --- #
    # ------------------------------------------------- #
    config   = lcf.load__config()
    config_  = {
        "figure.size"        : [4.5,4.5],
        "figure.pngFile"     : "png/time_vs_inventory.png", 
	"figure.position"    : [ 0.16, 0.16, 0.94, 0.94 ]    ,
        "ax1.y.normalize"    : 1.0e9, 
	"ax1.x.range"        : { "auto":False, "min":0.0, "max": 400.0, "num":5 },
	"ax1.y.range"        : { "auto":False, "min":0.0, "max":    12, "num":7 },
	"ax1.x.label"        : "Time (d)"                    ,
	"ax1.y.label"        : "Target Inventory (GBq)"      ,
	"legend.location"    : "lower left"                  ,
        "ax1.cursor.x"       : [ 365.0 ], 
        "legend.fontsize"    : 10.0, 
    }
    config = { **config, **config_ }
    
    fig     = gpl.gplot1D( config=config )
    for ik,Data in enumerate(DataList):
        fig.add__plot( xAxis=Data[:,t_], yAxis=Data[:,RM_], label=labels[ik] )
    fig.set__axis()
    fig.set__legend()
    fig.save__figure()

    # ------------------------------------------------- #
    # --- [4] plot Figure ( time-cumulate )         --- #
    # ------------------------------------------------- #
    config   = lcf.load__config()
    config_  = {
        "figure.size"        : [4.5,4.5],
        "figure.pngFile"     : "png/time_vs_cumulate_byRecycle.png", 
	"figure.position"    : [ 0.16, 0.16, 0.94, 0.94 ],
        "ax1.y.normalize"    : 1.0e9, 
	"ax1.x.range"        : { "auto":False, "min":0.0, "max": 400.0, "num":5 },
	"ax1.y.range"        : { "auto":False, "min":0.0, "max":1000.0, "num":6 },
	"ax1.x.label"        : "Time (d)",
	"ax1.y.label"        : "Cumulative Production (GBq)",
	"legend.location"    : "best",
        "ax1.cursor.x"       : [ 365.0 ], 
        "legend.fontsize"    : 10.0, 
    }
    config = { **config, **config_ }
    
    fig     = gpl.gplot1D( config=config )
    for ik,Data in enumerate(DataList):
        fig.add__plot( xAxis=Data[:,t_], yAxis=Data[:,CB_], label=labels[ik] )
    fig.set__axis()
    fig.set__legend()
    fig.save__figure()

    # ------------------------------------------------- #
    # --- [4] plot Figure ( inventory )             --- #
    # ------------------------------------------------- #
    config   = lcf.load__config()
    config_  = {
        "figure.size"        : [4.5,4.5],
        "figure.pngFile"     : "png/recycle_vs_cumulate.png", 
	"figure.position"    : [ 0.16, 0.16, 0.84, 0.84 ],
        "ax1.y.normalize"    : 1.0e9, 
        "ax2.y.normalize"    : 1.0e9, 
	"ax1.x.range"        : { "auto":False, "min":70.0, "max": 110.0, "num":5 },
	"ax1.y.range"        : { "auto":False, "min": 0.0, "max":1000.0, "num":6 },
	"ax2.y.range"        : { "auto":False, "min": 0.0, "max":  20.0, "num":5 },
	"ax1.x.label"        : "Recycle factor (%)",
	"ax1.y.label"        : "Production (GBq/y)",
	"ax2.y.label"        : "Inventory (GBq)",
        "plot.marker"        : "o",
        "plot.markersize"    : 3.0,
        "ax1.cursor.x"       : [ 100.0 ], 
        "ax2.cursor.y"       : [ 11.1 ], 
    }
    config = { **config, **config_ }
    
    
    fig      = gpl.gplot1D( config=config )
    fig.add__plot ( xAxis=p365[:,0], yAxis=p365[:,1], label="Production", color="C0" )
    fig.add__plot2( xAxis=p365[:,0], yAxis=p365[:,2], label="Inventory" , color="C1" )
    fig.set__axis()
    fig.set__legend()
    fig.save__figure()

    

# ======================================== #
# ===  実行部                          === #
# ======================================== #
if ( __name__=="__main__" ):
    display()

