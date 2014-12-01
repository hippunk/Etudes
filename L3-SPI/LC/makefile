fich_obj = main.o Alex.o Asyn.o

#
# Options for compilation
#

GCCOBJ = gcc -c 
GCCLNK = gcc 


# Option for debugger
opt = -g -Wall -D_DEBUG_
# opt = -O2 -Wall
#
#
#

#
#-------- Mains ---------------
#

main : $(fich_obj)
	$(GCCLNK) $(fich_obj) $(opt) -o main -I ./

main.o : main.c 
	$(GCCOBJ) $(opt) main.c -o main.o -I ./

#
#-------- Modules -------------
#

Alex.o : Alex.c Alex.h 
	$(GCCOBJ) $(opt) Alex.c -o Alex.o -I ./

Asyn.o : Asyn.c Asyn.h 
	$(GCCOBJ) $(opt) Asyn.c -o Asyn.o -I ./

#
#-------- Headers -------------
#

#
#-------- Clean objects -------
#

clean : 
	rm -f *.{o,c~} 

#
#-------- All executables -------
#

all :   main 

#
#-------- All tests -------
#

#
#-------- Tags -------
#

tags :
	etags *.c 
