import os, sys, subprocess

settingBase = "dat/settings__1target_2sep_scheduleScan_base.json"
beamonList  = list( range( 2, 24+1 ) )
beamoffList = list( range( 2, 6+1  ) )
prep        = 0.5

for beamoff in beamoffList:
    sep_val = beamoff - prep
    command =  "sed -e s/@BEAMOFF/{0}/g {1} | sed -e s/@SEP/{2}/g > dat/settings__1target_2sep_temp.json".format( beamoff, settingBase, sep_val )
    print( command )
    subprocess.run( command, shell=True )
    for beamon in beamonList:
        command = "sed -e s/@BEAMON/{0}/g dat/settings__1target_2sep_temp.json > dat/1target_2sep/settings__1target_2sep_{0}_{1}.json".format( beamon, beamoff )
        print( command )
        subprocess.run( command, shell=True )
        command = "python3.10 pyt/estimate__time_vs_yield.py --settingFile dat/1target_2sep/settings__1target_2sep_{0}_{1}.json".format( beamon, beamoff )
        print( command )
        subprocess.run( command, shell=True )


