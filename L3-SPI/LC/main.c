#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "Alex.h"
#include "Asyn.h"

int main(int argc, char * argv[])
{		

	if(argc > 4 || argc < 3)
	{
		printf("Erreur :\n Utilisation : <prgm> <TypeSortie>(-o pour code objet, -c pour compile) <FichierEntree> <FichierSortie>(Si non indique, nom \"coureur\" choisi par defaut)\n");
		exit(-1);	
	}

	if(argc == 2)
		strcpy(fichOut,"coureur");
	else
		strcpy(fichOut,argv[3]);

	strcpy(fichIn,argv[2]);
	strcpy(typeOut,argv[1]);


	//printf("Arguments : %s %s %s\n",fichIn,fichOut,typeOut);

	AlexTester(0);
	AsynTester();
	return EXIT_SUCCESS;
}

