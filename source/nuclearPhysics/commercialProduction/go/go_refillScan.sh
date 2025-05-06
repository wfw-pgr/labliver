#!/bin/bash

SETTINGBASE="dat/settings__refill_base.json"
MIDFILE="dat/settings__refill_temp.json"
REC_LIST=(0.999 0.990 0.98 0.95 0.90 0.80)
RECNAME_LIST=(0999 0990 0980 0950 0900 0800)
INTERVAL_LIST=(100 27 18 14 11 9 8 7 6 5 1)
INTERVALNAME_LIST=(0 1 2 3 4 5 6 7 8 10 52)

for ir in `seq ${#REC_LIST[@]}`
do
    REC=${REC_LIST[ir-1]}
    RECNAME=${RECNAME_LIST[ir-1]}
    sed -e s/@REC/${REC}/g ${SETTINGBASE} > ${MIDFILE}
    
    for ii in `seq ${#INTERVAL_LIST[@]}`
    do
	INTERVAL=${INTERVAL_LIST[ii-1]}
	INTERVAL_NAME=${INTERVALNAME_LIST[ii-1]}
	ID=${RECNAME}"_"${INTERVAL_NAME}
	SETTINGFILE="dat/refill/settings__refill_"${ID}".json"
	echo ${SETTINGFILE}
	sed -e s/@INTERVAL/${INTERVAL}/g ${MIDFILE} | sed -e s/@ID/${ID}/g > ${SETTINGFILE}
	
    	python3.10 pyt/estimate__time_vs_yield.py --settingFile ${SETTINGFILE}
    done
done

