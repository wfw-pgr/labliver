#!../../bin/linux-arm/lightupLED

#- You may have to change lightupLED to something else
#- everywhere it appears in this file

< envPaths
# -- n.k. -- #
epicsEnvSet("STREAM_PROTOCOL_PATH", ".:../../protocols")

cd "${TOP}"

## Register all support components
dbLoadDatabase "dbd/lightupLED.dbd"
lightupLED_registerRecordDeviceDriver pdbbase

## Load record instances
#dbLoadRecords("db/xxx.db","user=epics")

# -- n.k. -- #
dbLoadRecords( "db/lightupLED.db" )
drvAsynSerialPortConfigure ("PS1","/dev/ttyACM0")
asynSetOption( "PS1", 0, "baud", "19200" )

cd "${TOP}/iocBoot/${IOC}"
iocInit

## Start any sequence programs
#seq sncxxx,"user=epics"
