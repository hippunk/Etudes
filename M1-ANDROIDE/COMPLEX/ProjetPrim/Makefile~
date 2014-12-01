# définition des variables
CC = gcc
CFLAGS = -O3 -lgmp -lm -Wall

# désactivation des règles implicites
.SUFFIXES:

all: main.o test.o carmichael.o arithZn.o naif.o
	$(CC) $(CFLAGS) main.o test.o carmichael.o arithZn.o naif.o -o projetPrim
 
main.o: main.c arithZn.h
	$(CC) $(CFLAGS) -c main.c -o main.o 
  
test.o: test.c 
	$(CC) $(CFLAGS) -c test.c -o test.o

carmichael.o: carmichael.c 
	$(CC) $(CFLAGS) -c carmichael.c -o carmichael.o

arithZn.o: arithZn.c 
	$(CC) $(CFLAGS) -c arithZn.c -o arithZn.o

naif.o: naif.c 
	$(CC) $(CFLAGS) -c naif.c -o naif.o


# suppression des fichiers temporaires
clean:
	rm -rf *.o
 
# suppression de tous les fichiers, sauf les sources,
# en vue d'une reconstruction complète
mrproper: clean
	rm -rf Programme
