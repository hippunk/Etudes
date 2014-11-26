#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include <string.h>
#include <math.h>
#include <sys/time.h>


int **creerListeObjet(int nbObjets);
int sommeLigne(int * tab,int taille);
int * creerLigneValeurs(int taille);
void detruireLigneValeurs(int ** tab);
void detruireListeObjet(int *** tab);
void afficherListeObjet(int ** tab,int taille);
void afficherLigneValeurs(int * tab,int taille);
int * dynamiqueMin(int ** tab,int taille);



double chrono(){

	static struct timeval old;
	struct timeval tmp;
	gettimeofday(&tmp,NULL);
	
	double time = ((double)tmp.tv_sec+(double)tmp.tv_usec/1000000)-((double)old.tv_sec+(double)old.tv_usec/1000000);

	old = tmp;

	return time;
}

int **creerListeObjet(int nbObjets){
		
	int i = 0;
	int ** tab;
	tab = malloc(sizeof(int*)*2);

	for(i = 0;i<2;i++){
		tab[i] = malloc(sizeof(int)*nbObjets);
	}	
	return tab;
}

int sommeLigne(int * tab, int taille){
	int i = 0;
	int somme = 0;

	for(i = 0;i<taille;i++)
		somme += tab[i];
	return somme;
}

int * creerLigneValeurs(int taille){
	int * tab;	
	tab = malloc(sizeof(int)*taille);
	return tab;
}

void detruireLigneValeurs(int ** tab){	
	free(*tab);
	*tab = NULL;
}


void detruireListeObjet(int *** tab){
	free((*tab)[0]);
	free((*tab)[1]);
	free(*tab);
	*tab = NULL;	
} 

void afficherListeObjet(int ** tab,int taille){
	int i = 0;
	printf("Tableau des valeurs : ");
	for(i = 0;i < taille;i++)
		printf("%3i",tab[0][i]);
	printf("\nTableau des poids   : ");
	for(i = 0;i < taille;i++)
		printf("%3i",tab[1][i]);
	printf("\n");
}

void afficherLigneValeurs(int * tab,int taille){
	int i = 0;
	printf("Ligne Valeurs : ");
	for(i = 0;i < taille;i++)
		printf("%i:%i ",i,tab[i]);
	printf("\n");
}

int min(int a,int b){
	int resultat = 0;
	if(a<b)
		resultat = a;
	else
		resultat = b;
		
	return resultat; 
}

int * eurApprox(int ** tab, int taille,float epsilon){
	int vMax = sommeLigne(tab[0],taille)+1;
	float k = (epsilon*vMax)/taille;
	//printf("Debug k : %f\n", k);
	//afficherListeObjet(tab,taille);
	int i = 0;
	for(i = 0; i<taille;i++){
		tab[0][i] = round(tab[0][i]/k);
	}
	//afficherListeObjet(tab,taille);
	int * objetsDyn = dynamiqueMin(tab,taille);
	return objetsDyn;
}

int * dynamiqueMin(int ** tab,int taille){

	int vMax = sommeLigne(tab[0],taille)+1;
	//int[][] P=new int[nbObjet][Vmax+1];
	int * p1 = creerLigneValeurs(vMax);
	int * p2 = creerLigneValeurs(vMax);

		// On remplit la premiere ligne comme ceci
	int j = 0;

        while(j<vMax){p1[j] = 1000000;j+=1;}
        p1[0] = 0;
      	p1[tab[0][0]] = tab[1][0];
        
        
        int i = 0;
        int h = 0;
     // Ensuite on remplit les autres lignes du tableau
        for(i=1;i<taille;i++){
		for(h=0;h<j;h++){
			if(tab[0][i]>h)
                		p2[h]=p1[h];
            		else
                    		p2[h] = min(p1[h], p1[h-tab[0][i]]+tab[1][i]);
          	}

            	memcpy(p1,p2,sizeof(int)*vMax);

        }
	free(p2);
	
	return p1;	
}

int valeurOptimale(int * tab, int poidsMax,int taille){

	int i = 0;
        int opti=-1;
        
        for(i=0;i<taille;i++){
        	if(tab[i]<=poidsMax && opti<i){
        	       	opti=i;  
        	} 
        }
        return opti;
}

int aleatoire(int val){
	return rand()%val;
}

void genererListe(int ** tab,int * S,int nbObjet,int range,int typeGen,int seed,int noTest){
	
	srand(seed);
	int r1 = range/10;
	int valeur = 0;
	int sum = 0;
	int resultTest = 0;
	int i = 0;
	for(i = 0;i< nbObjet;i++)
	{
		tab[1][i] = aleatoire(range) +1;
		switch(typeGen){
			case 1:
				valeur = aleatoire(seed+1);
				break;
			case 2:
				valeur = aleatoire(2*r1+1)+tab[1][i]-r1;
				if (valeur <= 0) 
					valeur = 1;
				break;
			case 3:
				valeur = tab[1][i]+10;
				break;
			case 4:
				valeur = tab[1][i];
				break;
		}
		tab[0][i] = valeur;
		sum += tab[1][i];
	}
	
	resultTest = (seed*sum)/(noTest+1);
	if(resultTest <= range)
		resultTest = range+1;
		
	*S = resultTest;
}

int main(){
	
	//Nombre d'objets
	chrono();
	int taille = 100;
	int S = 0;
	
	while(1){
		
		//Création liste objet vide
		int ** listeObjets=creerListeObjet(taille);
	
		//instance dynamique
		genererListe(listeObjets,&S,taille,10,2,10000,1000);
	
		//afficherListeObjet(listeObjets,taille);
	
		//récupération de la dernière ligne instanciée par dynamique min
		int * objetsDyn = dynamiqueMin(listeObjets,taille);
	
		//Récupération de la valeur optimale
		int vMax = sommeLigne(listeObjets[0],taille)+1;
		int opti = valeurOptimale(objetsDyn,10,vMax);
	
		//printf("Valeur Optimale : %i\n", opti);
		//printf("Nb obj : Temps d'execution");
		printf("%i %f\n",taille,chrono());
		
		//Nettoyage de la mémoire
		detruireListeObjet(&listeObjets);
		detruireLigneValeurs(&objetsDyn);
		taille+=100;
	}
	
	
	return EXIT_SUCCESS;
}
