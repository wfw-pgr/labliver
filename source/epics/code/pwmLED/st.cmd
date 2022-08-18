#!../../bin/linux-arm/pwmLED

#- You may have to change pwmLED to something else
#- everywhere it appears in this file

< envPaths
epicsEnvSet("STREAM_PROTOCOL_PATH", ".:../../protocols")

cd "${TOP}"

## Register all support components
dbLoadDatabase "dbd/pwmLED.dbd"
pwmLED_registerRecordDeviceDriver pdbbase

## Load record instances
#dbLoadRecords("db/xxx.db","user=epics")

dbLoadRecords( "db/pwmLED.db" )
drvAsynSerialPortConfigure ("PS1","/dev/ttyACM0")
asynSetOption( "PS1", 0, "baud", "19200" )


cd "${TOP}/iocBoot/${IOC}"
iocInit

## Start any sequence programs
#seq sncxxx,"user=epics"
