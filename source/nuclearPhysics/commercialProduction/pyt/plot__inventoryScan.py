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
    config   = lcf.load__config()
    datFiles = [ "dat/result_rec1000.dat",
                 "dat/result_rec0999.dat",
                 "dat/result_rec0990.dat",
                 "dat/result_rec0980.dat",
                 "dat/result_rec0950.dat",
                 "dat/result_rec0900.dat",
                 "dat/result_rec0800.dat", 
    ]
    labels   = [ "100(%)", "99.9(%)", "99(%)", "98(%)", "95(%)", "90(%)", "80(%)" ]
    pngFile  = "png/targetInventory.png"
    
    # ------------------------------------------------- #
    # --- [2] Fetch Data                            --- #
    # ------------------------------------------------- #
    import nkUtilities.load__pointFile as lpf
    DataList = [ lpf.load__pointFile( inpFile=datFile, returnType="point" )
                 for datFile in datFiles ]
    
    # ------------------------------------------------- #
    # --- [3] config Settings                       --- #
    # ------------------------------------------------- #
    config_  = {
        "figure.size"        : [4.5,4.5],
	"figure.position"    : [ 0.16, 0.16, 0.94, 0.94 ]    ,
        "ax1.y.normalize"    : 1.0e9, 
	"ax1.x.range"        : { "auto":False, "min":0.0, "max": 400.0, "num":5 },
	"ax1.y.range"        : { "auto":False, "min":0.0, "max":    12, "num":7 },
	"ax1.x.label"        : "Time (d)"                    ,
	"ax1.y.label"        : "Target Inventory (GBq)"      ,
	"legend.location"    : "lower left"                  ,
        "cursor.x"           : [ 365.0 ], 
        "legend.fontsize"    : 10.0, 
    }
    config = { **config, **config_ }
    
    # ------------------------------------------------- #
    # --- [4] plot Figure ( inventory )             --- #
    # ------------------------------------------------- #
    fig     = gpl.gplot1D( config=config, pngFile=pngFile )
    for ik,Data in enumerate(DataList):
        fig.add__plot( xAxis=Data[:,t_], yAxis=Data[:,RM_], label=labels[ik] )
    fig.set__axis()
    fig.set__legend()
    fig.save__figure()


# ======================================== #
# ===  実行部                          === #
# ======================================== #
if ( __name__=="__main__" ):
    display()

