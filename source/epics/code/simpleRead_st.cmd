#!../../bin/linux-arm/simpleRead

#- You may have to change simpleRead to something else
#- everywhere it appears in this file

< envPaths

# -- n.k. added -- #
epicsEnvSet("STREAM_PROTOCOL_PATH", ".:../../protocols")

cd "${TOP}"

## Register all support components
dbLoadDatabase "dbd/simpleRead.dbd"
simpleRead_registerRecordDeviceDriver pdbbase

## Load record instances
#dbLoadRecords("db/xxx.db","user=epics")
# -- n.k. added -- #
dbLoadRecords ("db/simpleRead.db")

# drvGenericSerialConfigure( "PS1", "/dev/ttyACM0" )
# asynSetPortOption( "PS1", "baud", "19200" )
drvAsynSerialPortConfigure ("PS1","/dev/ttyACM0")
asynSetOption ("PS1", 0, "baud", "19200")
# -- n.k. added -- #

cd "${TOP}/iocBoot/${IOC}"
iocInit

## Start any sequence programs
#seq sncxxx,"user=epics"
