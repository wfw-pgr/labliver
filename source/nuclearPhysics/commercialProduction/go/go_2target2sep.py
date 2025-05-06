import os, sys, subprocess

cycles       = list( range( 1, 2+1 ) )
settingBases = [ "dat/settings__2target_2sep_cycle{}_base.json".format( ik ) for ik in cycles ]
beamonList   = list( range( 2, 10+1 ) )
prep         = 1.25

for ik,settingBase in enumerate(settingBases):
    cycleNum = cycles[ik]
    for beamon in beamonList:
        # -- 
        beamoff = beamon
        sep_val = beamoff - prep
        # -- 
        command =  "sed -e s/@BEAMOFF/{0}/g {1} | sed -e s/@SEP/{2}/g | sed -e s/@BEAMON/{3}/g > dat/2target_2sep/settings__2target_2sep_{3}_{0}_cycle{4}.json".format( beamoff, settingBase, sep_val, beamon, cycleNum )
        print( command )
        subprocess.run( command, shell=True )
        # -- 
        command = "python3.10 pyt/estimate__time_vs_yield.py --settingFile dat/2target_2sep/settings__2target_2sep_{0}_{1}_cycle{2}.json".format( beamon, beamoff, cycleNum )
        print( command )
        subprocess.run( command, shell=True )
    
