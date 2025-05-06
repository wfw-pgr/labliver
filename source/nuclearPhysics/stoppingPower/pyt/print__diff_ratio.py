import numpy as np
import nkUtilities.load__pointFile as lpf

ratio_   = 4
inpFile1 = "dat/stoppingPower__e_in_Ta.dat"
inpFile2 = "dat/stoppingPower__e_in_Pt.dat"
Data1    = lpf.load__pointFile( inpFile=inpFile1, returnType="point" )
Data2    = lpf.load__pointFile( inpFile=inpFile2, returnType="point" )

diff     =  Data1[:,ratio_] - Data2[:,ratio_]
print( np.max( np.abs(diff) ) )




