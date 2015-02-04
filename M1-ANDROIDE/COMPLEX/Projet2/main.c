#include <stdlib.h>
#include <stdio.h>
#include <math.h>   
#include <ctype.h>
#include "fonction.h"
#include <time.h>

int main(int argc, char** argv){
  /*
  // Test de my_pgcd(a,b) 
  printf("\n-----------------\n\n");
  int a1,b1;
  printf("Calcul du PGCD (entrez deux nombres) : ");
  scanf("%d %d",&a1,&b1);
  int t = my_pgcd(a1,b1);
   
  // Test de my_inverse(a,n) 
  printf("\n-----------------\n\n");
  int a,N;
  printf("Calcul de l'inverse a mod N  (entrez deux nombres) : ");
  scanf("%d %d",&a,&N);
  int k = my_inverse(a,N);

  // Test de expo_mod(m,e,N) 
  printf("\n-----------------\n\n");
  int m,e,n;
  printf("Calcul de l'exponentiation modulaire (Entrez trois nombres, m e et N) : ");
  scanf("%d %d %d",&m,&e,&n);
  int mu=expo_mod(m,e,n);
  printf("L'exponentiation modulaire de %d puissance %d modulo %d est : %d\n",m,e,n,mu);

  // Test de first_test(n) 
  printf("\n-----------------\n\n");
  int j;
  printf("Calcul de primalite de (entrez un entier) : ");
  scanf("%d",&j);
  int y=first_test(j);
  if(y==1)
    printf("%d est premier.\n",j);
  else
  printf("%d n'est pas premier.\n",j);

  // Test de is_Carmichael(n)
  printf("\n-----------------\n\n");
  int c;
  printf("Test de Carmichael (entrez un nombre) : ");
  scanf("%d",&c);
  int r=is_Carmichael(c);
  if(r==1)
    printf("%d est un nombre de Carmichael.\n",c);
  else
  printf("%d n'est pas un nombre de Carmichael.\n",c);*/

  srand(time(NULL));
  /*int r=GenPKRSA(50);

  printf("blabla %d\n",r);*/
  /* double t=experimental_Fermat(100000);
     printf("pourcentage d'erreur  %f\n",t);*/

  double t=experimental_RabinMiller(100000);
  printf("pourcentage d'erreur  %f\n",t);
  return 0;

   
}
