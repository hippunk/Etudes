#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<gmp.h>
#include"carmichael.h"
#include"arithZn.h"
#include"naif.h"
#include<time.h>

/*int iIs_carmichael(int n){
	//int result = 1;
	if((n%2) == 0)
		return 0;
	int a = 0;
	
	for(a = 1;a < n;a++){
		if(((int)(pow(a,n-1)-1)%(n))=0)
			return 0;
	}
	return 1;
}*/



void mpz_pow(mpz_t result,mpz_t e,mpz_t n){

	mpz_t a;
       	mpz_init (a);
	mpz_t b;
       	mpz_init (b);
	mpz_t tmp;
       	mpz_init (tmp);

	mpz_set(a,e);
	mpz_set(b,n);

 	mpz_set_str(result,"1",10);

	while(mpz_cmp_ui(b,0)>0){
		mpz_mod_ui(tmp,b,2);
		if (mpz_cmp_ui(tmp,1)==0)
			mpz_mul(result,result,a);
		mpz_tdiv_q_ui(b,b,2);
		mpz_mul(a,a,a);
	}

	mpz_clear(a);
	mpz_clear(b);
	mpz_clear(tmp);

	/*int expo(int a, int b){
	  int result = 1;

	  while (b){
	    if (b%2==1){
	      result *= a;
	    }
	    b /= 2;
	    a *= a;
	  }

	  return result;
	}*/
}

void mpzGen_carmichael(mpz_t n){

	mpz_t tmp;
	mpz_t integ2;
	mpz_t tab[9592];
	int i = 0;
	int j = 0;
	int k = 0;
	int cpt = 0;
	int prem = 0;

       	mpz_init (tmp);
       	mpz_init (integ2);
	for(i = 0;i<9592;i++)
		mpz_init(tab[i]);

	mpz_set_str(integ2,"2",10);


	//Génération de la liste de premiers
	printf("Génération de la liste de premiers : \n");

	for(prem = 0;mpz_cmp_si(integ2,100)<=0;mpz_add_ui(integ2,integ2,1)){ 
		//gmp_printf("Debug compteur : %Zd\n", integ2);
		//first_test(integ2);		
		if(first_test(integ2)){
					
			mpz_set(tab[cpt],integ2);
			cpt++;
		}
	}

	printf("Fin calcul %i\n",cpt);

	//Calcul carmichael
	for(i = 0;i<cpt;i++){
		for(j = i;j<cpt;j++){
			for(k = j;k<cpt;k++){
							
				mpz_set(tmp,tab[i]);
				//gmp_printf("tmp : %Zd\n",tmp);
				mpz_mul(tmp,tmp,tab[j]);
				mpz_mul(tmp,tmp,tab[k]);
				gmp_printf("%Zd x %Zd x %Zd : %Zd\n",tab[i],tab[j],tab[k],tmp);
				if(mpzIs_carmichael(tmp));
				//	gmp_printf("Est carmichael : %Zd\n",tmp);
				//printf("test : %i, %i, %i\n",i,j,k);
			}
		}
	}


       	mpz_clear (tmp);
	mpz_clear (integ2);
	for(i = 0;i<9592;i++)
		mpz_clear(tab[i]);
}

void mpzGen_carmichalol(mpz_t n){

	srand(time(NULL));
	char buff[256];
	int nb = rand()%42+1;
	int i = 0;
	FILE* fichier = NULL;

	fichier = fopen("liste_carmichael", "r");
	if (fichier != NULL)
	{
		for(i = 0;i<nb;i++)
			fscanf(fichier, "%s", buff);
		
		printf("ligne : %s", buff);
	 
		fclose(fichier);
	}
}

int mpzIs_carmichael(mpz_t n){

	if(first_test(n) == 1 || mpz_cmp_ui(n,1) <= 0){ //test si n premier
		return 0;
	}

  	mpz_t tmp;
  	mpz_t a;
  	mpz_t pgcd;
	int nbd = 0;
       	mpz_init (tmp);
       	mpz_init (a);
       	mpz_init (pgcd);

	mpz_set(tmp,n);

	mpz_set_str(a,"3",10);

	for(;mpz_cmp(a,n)<0;mpz_add_ui(a,a,2)){

		//pgcd n et a doit être 1
		mpz_gcd(tmp,a,n);
		

		if(mpz_cmp_ui(tmp,1)==0){
			
			//nbd = 1;
			mpz_sub_ui(n,n,1);//n = n-1
			mpz_pow(tmp,a,n);//a^(n-1)
			//gmp_printf("a^n : %Zd\n",tmp);
			mpz_sub_ui(tmp,tmp,1);//a^(n-1)-1
			//gmp_printf("a^n-1 : %Zd\n",tmp);

			mpz_add_ui(n,n,1);

			mpz_mod(tmp,tmp,n);
			//gmp_printf("tmp = %Zd\n\n",tmp);
		
			

			if(mpz_cmp_ui(tmp,0)!=0)
				return 0;
		}
	}
	//if(!nbd)
	//	return 0;
	
	mpz_clear(tmp);
	mpz_clear(a);

	return 1;
}
