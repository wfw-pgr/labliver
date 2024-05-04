import json5
inpFile = "cnf/sample.json"
with open( inpFile, "r" ) as f:
    params = json5.load( f )

print( "\n", params, "\n" )
