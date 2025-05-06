#!/usr/local/bin/python3.10

import os, sys, subprocess, time, argparse
import datetime                              as dt
import nkScripts.materials__fromJSON         as mfj
import nkUtilities.show__section             as sct
import nkUtilities.precompile__parameterFile as ppf
import nkUtilities.command__postProcess      as cpp

# ========================================================= #
# ===  go__phits.py                                     === #
# ========================================================= #

def go__phits():
    
    # ------------------------------------------------- #
    # --- [1] arguments                             --- #
    # ------------------------------------------------- #
    
    # ------------------------------------------------- #
    # --- [2] configure settings                    --- #
    # ------------------------------------------------- #
    #  -- [2-1]  path designation                   --  #
    if ( args.phits_win is not None ):
        default_settings["phits_win"] = args.phits_win
    if ( args.phits_lin is not None ):
        default_settings["phits_lin"] = args.phits_lin

    #  -- [2-2]  directory & execution File path    --  #
    dirpath = os.path.dirname( os.path.abspath( inpFile ) )
    exeFile = os.path.join( dirpath, "execute_phits.inp"  )
    return()


# ========================================================= #
# ===   Execution of Pragram                            === #
# ========================================================= #

if ( __name__=="__main__" ):
    go__phits()
