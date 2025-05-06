# ---------------------------------------- #
# ---     makefile for TALYS           --- #
# ---------------------------------------- #

INPUT=Ra226_gp.inp

EXEC=talys
OUTPUT=output

$(OUTPUT): $(INPUT)
	$(EXEC) < $(INPUT) > $(OUTPUT)

all: clean $(OUTPUT)
