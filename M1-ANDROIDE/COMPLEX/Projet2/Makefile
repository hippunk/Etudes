
#C_FLAGS = -Wall -g -Wl,--no-as-needed
C_FLAGS = -O2 -Wall -g -lm

all:  main

fonction.o : fonction.h fonction.c
	gcc ${C_FLAGS} -c fonction.c

main.o : fonction.h main.c
	gcc ${C_FLAGS} -c main.c

main : main.o fonction.o
	gcc ${C_FLAGS} -o main main.o fonction.o

clean : 
	rm -f *.o fonction main
