#!/bin/bash

BEAMOFF_VAL=8
SETTINGFILE="dat/settings__scheduleScan.json"
# SETTINGFILE="dat/settings__for0DayBeamOFF.json"
# SETTINGFILE="dat/settings__for1DayBeamOFF.json"
# SETTINGFILE="dat/settings__for2DayBeamOFF.json"


SEP_VAL=$((${BEAMOFF_VAL}-2))
sed -e s/@BEAMOFF/${BEAMOFF_VAL}/g ${SETTINGFILE} | sed -e s/@SEP/${SEP_VAL}/g > dat/settings__sch_temp.json

for ik in `seq 1 25`
do
    echo ${ik}
    sed -e s/@BEAMON/${ik}/g dat/settings__sch_temp.json > dat/sch/settings__sch_${ik}_${BEAMOFF_VAL}.json
    python3.10 pyt/estimate__time_vs_yield.py --settingFile dat/sch/settings__sch_${ik}_${BEAMOFF_VAL}.json
done


