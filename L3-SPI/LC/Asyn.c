#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <time.h>
#include <sys/wait.h>
#include <unistd.h> 
#include "Asyn.h"
#include "Alex.h"

/*
S->T
T->F+K
K->Id.Reel.T
F->"FF"
*/

typedef struct tds_s{
	float h_depart;
	float h_arrivee;
	
}tds_t;

tds_t tdsTableau[26];

int bS(int iD,int * piF);
int bT(int iD,int * piF);
int bK(int iD,int * piF);
int bI(int iD,int * piF);
int bR(int iD,int * piF);
int bF(int iD,int * piF);
int bMotConforme(int iD, int *piF);
int bTDSajouter(int iD,int iR);

void AsynAmorcer()
{

}

void AsynInitialiser()
{
	int i;
	for(i = 0; i < 26;i++)
	{
		tdsTableau[i].h_depart = -1.0;
		tdsTableau[i].h_arrivee = -1.0;
	}
}

void AsynReconnaitre()
{
	//init
	int iD = 0;
	int iF = 0;
	int bSucces;
	bSucces = bMotConforme(iD,&iF);
	
	if(!bSucces){
		printf("Le code n'est pas systaxiquement correcte\n");
		exit(-1);	
	}
}

int bMotConforme(int iD, int *piF){
	int bSucces;
	bSucces = bS(iD, piF);
	return(bSucces);
}

int bS(int iD,int * piF){
	int bSucces;
	bSucces = bT(iD, piF);
	return(bSucces);
}

int bT(int iD,int * piF){
	int bSucces;
	int tmp;
	int iF = 0;
	tmp = bAlexFF(iD);
	if(tmp)
		bSucces = bF(iD,&iF);
	else
		bSucces = bK(iD,&iF);
		
	*piF = (bSucces)?iF:iD;
	return bSucces;
}

int bK(int iD,int * piF){
	int bSucces;
	int iR = 0, iM = 0,iF = 0;
	bSucces = (bI(iD,&iR) && bR(iR,&iM) && bTDSajouter(iD,iR) && bT(iM,&iF));
	*piF = (bSucces)?iF:iD;
	return bSucces;
}

int bTDSajouter(int iD,int iR){
	int bSucces = 1;
	if(tdsTableau[AlexID(iD)-'A'].h_depart == -1.0)
		tdsTableau[AlexID(iD)-'A'].h_depart=AlexValeur(iR);
	else
		tdsTableau[AlexID(iD)-'A'].h_arrivee=AlexValeur(iR);
		
	return bSucces;
}

int bI(int iD,int * piF){
	int bSucces;
	if(bSucces = (bAlex(iD) == ID))
		*piF = iD+1;
	else
		*piF = iD;
	
	return bSucces;
}

int bR(int iD,int * piF){
	int bSucces;
	if(bSucces = (bAlex(iD) == REELS))
		*piF = iD+1;
	else
		*piF = iD;
	
	return bSucces;
}

int bF(int iD,int * piF){
	int bSucces;
	if(bSucces = (bAlex(iD) == FF))
		*piF = iD+1;
	else
		*piF = iD;
	
	return bSucces;
}

void AsynGenerer(){
	//printf("FichIn : %s\n",fichIn);
	strcat(fichIn,".c");
	//printf("FichIn : %s\n",fichIn);
	FILE* codeObjet = fopen(fichIn, "w+");
	int i;
	int cpt0 = 0;
	char instruction[TAILLE];
	//printf("printf(\"Classement :\\n\");\n");
	fputs("#include <stdio.h>\n", codeObjet);
	fputs("#include <stdlib.h>\n", codeObjet);
	fputs("int main(){\n", codeObjet);
	
	while(cpt0 < 26)
	{
		cpt0 = 0;
		int iMin;
		float min = D_MAX;
		float arrivee;
		float depart;
	
		for(i = 0; i < 26;i++)
		{
			arrivee = tdsTableau[i].h_arrivee;
			depart = tdsTableau[i].h_depart;
			//printf("Tour %c : %2f %2f\n", 'A'+i,arrivee, depart);
			
			if(arrivee == -1.0)
				cpt0++;
			
			if(arrivee < depart){
				tdsTableau[i].h_arrivee = -1.0;
				tdsTableau[i].h_depart = -1.0;
				arrivee = -1.0;
				depart = -1.0;
			}

			if((arrivee-depart) < min && arrivee != -1.0 && depart != -1.0){
				min = (arrivee-depart);
				iMin = i;
			}			
		}
		if(min != D_MAX){

			//printf("Min %c : %.2f cpt0 : %i\n",'A'+i,min,cpt0);
			//printf("printf(\"Courreur : %c, Temps : %.2f \\n\");\n",'A'+iMin,min);
			sprintf(instruction,"printf(\"Courreur : %c, Temps : %.2f \\n\");\n",'A'+iMin,min);
			fputs(instruction,codeObjet);
			tdsTableau[iMin].h_arrivee = -1.0;
			tdsTableau[iMin].h_depart = -1.0;
		}

	}

	fputs("return EXIT_SUCCESS;}\n", codeObjet);
	fclose(codeObjet);

	if(strcmp(typeOut,"-c") == 0){
		//printf("Dans -c\n");
		pid_t pid;
		switch(pid = fork())
		{
			case 0:
				execlp("gcc", "gcc","-o",fichOut,fichIn,NULL);
		}

		wait(&pid);

		switch(pid = fork())
		{
			case 0:
				execlp("rm", "rm",fichIn,NULL);
		}
		wait(&pid);
	}

	//system("gcc -o coureur coureur.c");
	
}

void AsynTester()
{
	//printf("Entree : %s, Sortie : %s\n",fichIn,fichOut);
	//printf("AsynAmorcer\n");
	AsynAmorcer();
	//printf("AsynInitialiser\n");
	AsynInitialiser();
	//printf("AsynReconnaitre\n");
	AsynReconnaitre();
	
	/*int i;
	for(i = 0; i < 26;i++)
	{
		if(tdsTableau[i].h_depart != -1.0)
		printf("tdsTab : id : %c, hd : %.2f ha : %.2f\n",i+'A',tdsTableau[i].h_depart,tdsTableau[i].h_arrivee);
	}*/
	
	//printf("AsynGenerer\n");
	AsynGenerer();
	
}
