import os, sys, json5
import numpy as np


# ========================================================= #
# ===  reduction__targetElement.py                      === #
# ========================================================= #

def reduction__targetElement():
    
    # ------------------------------------------------- #
    # --- [1] load setting File                     --- #
    # ------------------------------------------------- #
    settingFile = "dat/settings.json"
    with open( settingFile, "r" ) as f:
        settings = json5.load( f )
    
    # ------------------------------------------------- #
    # --- [2] trace schedule                        --- #
    # ------------------------------------------------- #
    remaining = 0.0
    t0h, t1h  = 0.0, 0.0
    
    for ik,key in enumerate( settings["series"] ):
        sched  = { **sched_base, **settings[key] }
        dt     = tinv * exchange__timeUnit( time=sched["dt"][time_], \
                                            unit=sched["dt"][unit_] )  # (?) -> (s) -> (tunit)
        t0h    = t1h          # (tunit)
        t1h    = t1h + dt     # (tunit)
        Y0h    = sched["beam.relint"] * Y0 * remaining

        

    return()
