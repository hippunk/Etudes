#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include "Alex.h"


int curseur = 0;
char symbol[TAILLE];
elt_t pile[20];

char AlexID(int id){
	if(pile[id].type == -3)
		return pile[id].donnees.id;
	else
		exit(-1);
}

float AlexValeur(int id){
	if(pile[id].type == -2){
		float f = pile[id].donnees.ft;
		return f;
	}
	else
		exit(-1);
}

char lireCar()
{
	return texte[curseur++];
}

int classeCar(char car)
{
	if(isdigit(car))
		return DIGI;
	else if(car == '.')
		return POINT;
	else if(car == ' ' || car == '\n' || car == '\t')
		return BLANC;
	else if(isalpha(car))
		return CHAR;
	else if(car == '\0')
		return FF;
	else
		return BLANC;
}

void AlexAmorcer()
{//Initialisation de l'automate
						
	AEF[0][0]=1;	AEF[0][1]=-255;	AEF[0][2]=4;	AEF[0][3]=5;	AEF[0][4]=-255;	AEF[0][5]=0;
	
	AEF[1][0]=1;	AEF[1][1]=2;	AEF[1][2]=-255;	AEF[1][3]=-1;	AEF[1][4]=-1;	AEF[1][5]=-1;
	
	AEF[2][0]=3;	AEF[2][1]=-255;	AEF[2][2]=-255;	AEF[2][3]=-255;	AEF[2][4]=-255;	AEF[2][5]=-255;
	
	AEF[3][0]=3;	AEF[3][1]=-255;	AEF[3][2]=-255;	AEF[3][3]=-2;	AEF[3][4]=-2;	AEF[3][5]=-2;
	
	AEF[4][0]=-255;	AEF[4][1]=-255;	AEF[4][2]=4;	AEF[4][3]=-3;	AEF[4][4]=-3;	AEF[4][5]=-3;
	
	AEF[5][0]=-4;	AEF[5][1]=-4;	AEF[5][2]=-4;	AEF[5][3]=5;	AEF[5][4]=-4;	AEF[5][5]=-4;
}

void AlexInitialiser()
{	
	//printf("adresses : %p, %p\n",&fichIn,&texte);
	//printf("AlexInitAvant : %s\n", fichIn);
	FILE* codeObjet = fopen(fichIn, "r");
	int i = 0;
	char caractereActuel;
	if(codeObjet == NULL)
	{
		printf("Erreur : Le fichier source n'existe pas\n");
		exit(-1);
	}

	i = 0;


    do
    {
        caractereActuel = fgetc(codeObjet); // On lit le caractère
		texte[i] = caractereActuel;
		i++;

    } while (caractereActuel != EOF);

	texte[i-1] = '\0';
	fclose(codeObjet);
	//printf("AlexInitApres : %s\n", fichIn);

	//fgets(texte, TAILLE, codeObjet);
	//printf("Test lecure fichier :\n%s\n", texte);

	//strcpy(texte,"TOTO 9.42\nPAUL 9.52\nJULES 9.58\nTOTO 10.40\nJULES 10.52\nPAUL 11.50");
	//strcat(texte,'\0');
}

void lireSymbol(int c0, int c1)
{
	//printf("c0 : %i, c1 : %i\n",c0,c1);
	int i;
	for(i = 0; i < TAILLE; i++)
		symbol[i] = '\0';
	
	for(i = 0; i < (c1-c0); i++){
		//printf("carac : %c\n",texte[c0+i]);
		symbol[i] = texte[c0+i];
	}
	
	//printf("i : %i\n",i);	
	symbol[i] = '\0';
}

void AlexReconnaitre()
{
	int etat = 0;
	int etat0 = 0;
	int curseur0 = 0;
	char car = ' ';
	int classe;
	int etatprim;
	int i = 0;
	
	do
	{
		car = lireCar();
		//printf("Debug, car récupéré : %c\n", car);
		classe = classeCar(car);
		etatprim = etat;
		etat = AEF[etat][classe];
		//printf("Debug, curseur0 : %i, curseur : %i\n",curseur0,curseur);
		
		//printf("Debug, Etat : %i, Etat0 : %i Classe : %i\n\n", etat,etatprim, classe);
		if(etat <= 0)
		{
			//printf("	Debug, curseur0 : %i, curseur : %i\n",curseur0,curseur);
			lireSymbol(curseur0,curseur-1);
			//printf("	Symbol récupéré : %s etat : %i\n", symbol,etat);
			if(etat != -4 && etat !=0){
				pile[i].type = etat;
				if(etat == ID)
					pile[i].donnees.id=symbol[0];
				if(etat == REELS){
					sscanf(symbol,"%f",&pile[i].donnees.ft);
				}
				i++;
			}
			
			curseur0 = curseur-1;
			etat = AEF[etat0][classe];
			//printf("	Debug if etat, Etat : %i Classe : %i\n\n", etat, classe);
		}			
		
	}while(etat != 0);
	
	/*pile[i].type = ENTIERS;
	pile[i].donnees='33';
	i++;*/
	
	pile[i].type = FF;
	pile[i].donnees.fin='F';
	i++;
	
	int j = 0;
	for(j = 0;j<i;j++)
	{
		//printf("type elem : %i\n", pile[j].type);
		/*if(pile[j].type == -3)
			printf("	ID : %c\n", pile[j].donnees.id);
		if(pile[j].type == -2)
			printf("	ID : %.2f\n", pile[j].donnees.ft);*/
	}

}

int bAlex(int iD){
	return pile[iD].type;
}

int bAlexFF(int iD){
	return pile[iD].type == FF;
}



void AlexTester(int nJeton)
{

		//printf("AlexAmorcer\n");
	AlexAmorcer();
		
	//Affichage AEF
	/*	int i,j;
		for(i = 0;i < 6;i++)
		{	
			for(j = 0;j < 6;j++)
			{
				printf("%5i", AEF[i][j]);
			}	
			printf("\n");
		}*/
		//printf("AlexInitialiser\n");
	AlexInitialiser();
	//printf("AlexReconnaitre\n");
	AlexReconnaitre();
		
	//Test lireCar
		/*strcpy(texte,"toto est le plus beau !");
		printf("texte : %s\n",texte);
		char car = ' ';
		while(car != '\0')
		{
			car = lireCar();
			printf("car : %c \n",car);
		}*/

}
