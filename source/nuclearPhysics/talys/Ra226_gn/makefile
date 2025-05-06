# ---------------------------------------- #
# ---     makefile for TALYS           --- #
# ---------------------------------------- #

INPUT =Ra226_gn.inp
EXEC  =talys
OUTPUT=output

$(OUTPUT): $(INPUT)
	$(EXEC) < $(INPUT) > $(OUTPUT)

clean:
	rm -f $(OUTPUT) *.tot energy *.fis

all: clean $(OUTPUT)

