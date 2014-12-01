#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define TAILLE 256

union data_u
{
	char id;
	float ft;
	int fin;
};  

typedef struct elt_s{
	int type;
	union data_u donnees; 
}elt_t;

//Classes
#define DIGI 0
#define POINT 1
#define CHAR 2
#define BLANC 3
#define AUTRE 4

#define FF 5

#define ENTIERS -1
#define REELS -2
#define ID -3
#define SEP -4

char texte[TAILLE];
int AEF[6][6];
char fichIn[TAILLE];
char fichOut[TAILLE];
char typeOut[TAILLE];

int bAlex();
int bAlexFF();
void AlexAmorcer();
float AlexValeur(int id);
char AlexID(int id);
void AlexInitialiser();
void AlexReconnaitre();
void AlexTester(int nJeton);

