import os, sys, json, re
import numpy                      as np
import nkUtilities.plot1D         as pl1
import nkUtilities.load__config   as lcf
import nkUtilities.configSettings as cfs


# ========================================================= #
# ===  acquire__irradiatedAmount                        === #
# ========================================================= #

def acquire__irradiatedAmount( A0=0.0, tH_A=0.0, Y0=0.0, t0=0.0, t1=0.0, unit=None ):
    
    # ------------------------------------------------- #
    # --- [1] Arguments                             --- #
    # ------------------------------------------------- #
    if ( tH_A <= 0.0  ): sys.exit( "[acquire__irradiatedAmount] tH_A <= 0.0" )
    if ( t1   <  t0   ): sys.exit( "[acquire__irradiatedAmount] t1   <= t0 " )
    if ( unit is None ): sys.exit( "[acquire__irradiatedAmount] unit is not designated...." )

    ld_A = convert__tHalf2lambda( tH=tH_A, unit=unit )
    conv = exchange__timeUnit   ( time=1., unit=unit, direction="convert" )
        
    # ------------------------------------------------- #
    # --- [2] calculate time evolution              --- #
    # ------------------------------------------------- #
    func = lambda t: A0*np.exp( -ld_A*conv*(t-t0) ) \
        + (Y0/ld_A)*( 1.0-np.exp( -ld_A*conv*(t-t0) ) )
    Arad = func( t1 )
    return( Arad, func )


# ========================================================= #
# ===  acquire__decayedAmount                           === #
# ========================================================= #

def acquire__decayedAmount( A0=0.0, B0=0.0, tH_A=0.0, tH_B=0.0, Y0=0.0, \
                            t0=0.0, t1=0.0, unit=None ):

    # ------------------------------------------------- #
    # --- [1] Arguments                             --- #
    # ------------------------------------------------- #
    if ( tH_A <= 0.0  ): sys.exit( "[acquire__irradiatedAmount] tH_A <= 0.0" )
    if ( tH_B <= 0.0  ): sys.exit( "[acquire__irradiatedAmount] tH_B <= 0.0" )
    if ( t1   <  t0   ): sys.exit( "[acquire__irradiatedAmount] t1   <= t0 " )
    if ( unit is None ): sys.exit( "[acquire__irradiatedAmount] unit is not designated...." )
    ld_A = convert__tHalf2lambda( tH=tH_A, unit=unit )
    ld_B = convert__tHalf2lambda( tH=tH_B, unit=unit )
    conv = exchange__timeUnit   ( time=1., unit=unit, direction="convert" )

    # ------------------------------------------------- #
    # --- [2] calculate time evolution              --- #
    # ------------------------------------------------- #
    coef1   = B0
    coef2   = ( ld_A*A0 - Y0 ) / ( ld_B - ld_A )
    coef3   = Y0 / ld_B
    func    = lambda t: coef1*np.exp( - ld_B*conv*(t-t0) ) \
        + coef2*( np.exp( - ld_A*conv*(t-t0) ) - np.exp( - ld_B*conv*(t-t0) ) ) \
        + coef3*( 1.0-np.exp( - ld_B*conv*(t-t0) ) )
    Brad    = func( t1 )
    return( Brad, func )


# ========================================================= #
# ===  unit_in_sec                                      === #
# ========================================================= #

def exchange__timeUnit( time=0.0, unit=None, direction="convert" ):

    if ( unit is None ): sys.exit( "[exchange__timeUnit] unit is not designated...." )

    # -- convert :: unit -> [s]
    # --  invert :: [s]  -> unit 
    
    cdict = { "y":365.0*24*60*60, "d":24*60*60.0, "h":60*60.0, "m":60.0, "s":1.0 }
    coeff = cdict[ unit.lower() ]
    if   ( direction=="convert" ):
        return( time * coeff )
    elif ( direction=="invert"  ):
        return( time / coeff )
    

# ========================================================= #
# ===  convert__tHalf2lambda                            === #
# ========================================================= #

def convert__tHalf2lambda( tH=0.0, unit=None ):

    if ( unit is None ): sys.exit( "[convert__tHalf2lambda] unit is not designated...." )
    tH_ = exchange__timeUnit( time=tH, unit=unit, direction="convert" )
    ld  = np.log(2.0) / ( tH_ )   # unit :: [s^-1]
    return( ld )


# ========================================================= #
# ===  acquire__timeSeries                              === #
# ========================================================= #

def acquire__timeSeries( settingFile=None ):
    
    # ------------------------------------------------- #
    # --- [1] load config                           --- #
    # ------------------------------------------------- #
    with open( settingFile, "r" ) as f:
        text      = re.sub(r'/\*[\s\S]*?\*/|//.*', '', f.read() )
        settings = json.loads( text )
        
    # ------------------------------------------------- #
    # --- [2] iterate according to beam schedule    --- #
    # ------------------------------------------------- #
    A0_loc     = settings["A0.init"]
    B0_loc     = settings["B0.init"]
    tH_A       = settings["tHalf.A"]
    tH_B       = settings["tHalf.B"]
    unit       = settings["t.unit"]
    ld_A       = convert__tHalf2lambda( tH=tH_A, unit=unit )
    ld_B       = convert__tHalf2lambda( tH=tH_B, unit=unit )
    Y0         = settings["Y.efficiency"] * settings["Y.ingredient.Bq"] \
        * settings["Y.beamcurrent.uA"] / ( 3600.0 * ld_B ) / settings["Y.peakRatio.B/A"]
    stack      = []
    milked_B   = 0.0
    for ik,key in enumerate( settings["series"] ):
        # -- preparation -- #
        sched  = settings[key]
        t0h    = sched["t0"]
        t1h    = sched["t1"]
        Y0h    = sched["Yr"] * Y0
        # -- milking :: [B]->0.0]  -- #
        if ( "milking" in sched ):
            if ( sched["milking"] ):
                milked_B += B0_loc
                B0_loc    = 0.0
        # -- update [A] -- #
        A0_loc_, func_A = acquire__irradiatedAmount( A0=A0_loc, tH_A=tH_A, \
                                                     unit=unit, Y0=Y0h, t0=t0h, t1=t1h )
        # -- update [B] -- #
        B0_loc_, func_B = acquire__decayedAmount( A0=A0_loc, B0=B0_loc, tH_A=tH_A, tH_B=tH_B,\
                                                  unit=unit, Y0=Y0h, t0=t0h, t1=t1h )
        # -- Data sampling -- #
        t_loc          = np.linspace( t0h, t1h, sched["nps"] )
        Anum, Bnum     = func_A( t_loc ), func_B( t_loc )
        Aact, Bact     = ld_A*Anum, ld_B*Bnum
        A0_loc, B0_loc = A0_loc_, B0_loc_
        stack         += [ np.concatenate( [ t_loc[:,np.newaxis], \
                                             Anum [:,np.newaxis], Bnum[:,np.newaxis],
                                             Aact [:,np.newaxis], Bact[:,np.newaxis]], axis=1) ]
        
    tEvo = np.concatenate( stack, axis=0 )
    return( tEvo )


# ========================================================= #
# ===  draw__figure                                     === #
# ========================================================= #

def draw__figure( Data=None, settings=None, settingFile=None ):

    t_, NA_, NB_, AA_, AB_ = 0, 1, 2, 3, 4
    min_, max_, num_       = 0, 1, 2

    if ( settings is None ):
        if ( settingFile is None ):
            sys.exit( "[dray__figure] settings & settingFile == None " )
        else:
            with open( settingFile, "r" ) as f:
                text     = re.sub(r'/\*[\s\S]*?\*/|//.*', '', f.read() )
                settings = json.loads( text )
    
    # ------------------------------------------------- #
    # --- [1] Data                                  --- #
    # ------------------------------------------------- #
    config                   = lcf.load__config()
    config                   = cfs.configSettings( configType="plot.def", config=config )
    config["FigSize"]        = (4.5,4.5)
    config["plt_position"]   = [ 0.16, 0.16, 0.94, 0.94 ]
    config["plt_xAutoRange"] = settings["figure.xAutoRange"]
    config["plt_yAutoRange"] = settings["figure.yAutoRange"]
    config["xMajor_Nticks"]  =  6
    config["yMajor_Nticks"]  = 11
    config["plt_marker"]     = "none"
    config["plt_markersize"] = 0.0
    config["plt_linestyle"]  = "-"
    config["plt_linewidth"]  = 1.6

    # ------------------------------------------------- #
    # --- [3] plot ( Number of Atoms )              --- #
    # ------------------------------------------------- #
    config["xTitle"]         =   settings["figure.num.xTitle"]
    config["yTitle"]         =   settings["figure.num.yTitle"]
    config["plt_xRange"]     = [ settings["figure.num.xMinMaxNum"][min_],
                                 settings["figure.num.xMinMaxNum"][max_] ]
    config["plt_yRange"]     = [ settings["figure.num.yMinMaxNum"][min_],
                                 settings["figure.num.yMinMaxNum"][max_] ]
    config["xMajor_Nticks"]  =   settings["figure.num.xMinMaxNum"][num_]
    config["yMajor_Nticks"]  =   settings["figure.num.yMinMaxNum"][num_]
    fig     = pl1.plot1D( config=config, pngFile=settings["figure.num.pngFile"] )
    fig.add__plot( xAxis=Data[:,t_], yAxis=Data[:,NA_]/settings["figure.num.y.normalize"], \
                   color="C0", label=settings["figure.num.label.A"] )
    fig.add__plot( xAxis=Data[:,t_], yAxis=Data[:,NB_]/settings["figure.num.y.normalize"], \
                   color="C1", label=settings["figure.num.label.B"] )
    fig.add__legend()
    fig.set__axis()
    fig.save__figure()

    # ------------------------------------------------- #
    # --- [4] plot ( Activity )                     --- #
    # ------------------------------------------------- #
    config["xTitle"]         =   settings["figure.act.xTitle"]
    config["yTitle"]         =   settings["figure.act.yTitle"]
    config["plt_xRange"]     = [ settings["figure.act.xMinMaxNum"][min_],
                                 settings["figure.act.xMinMaxNum"][max_] ]
    config["plt_yRange"]     = [ settings["figure.act.yMinMaxNum"][min_],
                                 settings["figure.act.yMinMaxNum"][max_] ]
    config["xMajor_Nticks"]  =   settings["figure.act.xMinMaxNum"][num_]
    config["yMajor_Nticks"]  =   settings["figure.act.yMinMaxNum"][num_]
    fig     = pl1.plot1D( config=config, pngFile=settings["figure.act.pngFile"] )
    fig.add__plot( xAxis=Data[:,t_], yAxis=Data[:,AA_]/settings["figure.act.y.normalize"],\
                   color="C0", label=settings["figure.act.label.A"] )
    fig.add__plot( xAxis=Data[:,t_], yAxis=Data[:,AB_]/settings["figure.act.y.normalize"],\
                   color="C1", label=settings["figure.act.label.B"] )
    fig.add__legend()
    fig.set__axis()
    fig.save__figure()

    
    return()


# ========================================================= #
# ===   Execution of Pragram                            === #
# ========================================================= #

if ( __name__=="__main__" ):

    # ------------------------------------------------- #
    # --- [1] parameters set                        --- #
    # ------------------------------------------------- #
    settingFile = "cnf/settings.jsonc"
    with open( settingFile, "r" ) as f:
        text     = re.sub(r'/\*[\s\S]*?\*/|//.*', '', f.read() )
        settings = json.loads( text )
    A0      = settings["A0.init"]
    B0      = settings["B0.init"]
    tH_A    = settings["tHalf.A"]
    tH_B    = settings["tHalf.B"]
    unit    = settings["t.unit"]
    Y0      = 1.0
    t0      = 0.0
    t1      = 1.0
        
    # ------------------------------------------------- #
    # --- [2] calculate singla response             --- #
    # ------------------------------------------------- #
    Arad,funcA = acquire__irradiatedAmount( A0=A0, tH_A=tH_A, Y0=Y0, \
                                            t0=t0, t1=t1, unit=unit )
    Brad,funcB = acquire__decayedAmount   ( A0=A0, B0=B0, tH_A=tH_A, tH_B=tH_B, Y0=Y0, \
                                            t0=t0, t1=t1, unit=unit )

    # ------------------------------------------------- #
    # --- [3] calcualte time series                 --- #
    # ------------------------------------------------- #
    tEvo = acquire__timeSeries( settingFile=settingFile )

    # ------------------------------------------------- #
    # --- [4] draw figure                           --- #
    # ------------------------------------------------- #
    ret = draw__figure( Data=tEvo, settingFile=settingFile )
    
