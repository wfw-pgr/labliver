#!/bin/bash

SETTINGBASE="dat/settings__alternating_base.json"
MIDFILE="dat/settings__alternating_temp.json"
NBEAM_LIST=(2 3 4 5 6 7 8 9 10)

BOA_LIST=('\/\/' '')
BOA_NAME=("before" "after")

for ir in `seq ${#BOA_LIST[@]}`
do
    BOA=${BOA_LIST[ir-1]}
    BOAID=${BOA_NAME[ir-1]}
    sed -e s/@BOA/${BOA}/g ${SETTINGBASE} > ${MIDFILE}
    
    for ii in `seq ${#NBEAM_LIST[@]}`
    do
	NBEAM=${NBEAM_LIST[ii-1]}
	NBEAM_NAME=${NBEAMNAME_LIST[ii-1]}
	ID=${BOAID}"_"${NBEAM}
	SETTINGFILE="dat/alternating/settings__alternating_"${ID}".json"
	echo ${SETTINGFILE}
	sed -e s/@NBEAM/${NBEAM}/g ${MIDFILE} | sed -e s/@ID/${ID}/g > ${SETTINGFILE}
	
    	python3.10 pyt/estimate__time_vs_yield.py --settingFile ${SETTINGFILE}
    done
done

