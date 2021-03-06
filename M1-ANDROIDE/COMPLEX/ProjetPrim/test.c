#include<stdio.h>
#include<stdlib.h>
#include"arithZn.h"
#include"naif.h"
#include "test.h"
#include "carmichael.h"
#include<gmp.h>
#include <sys/time.h>

double chrono(){

	static struct timeval old;
	struct timeval tmp;
	gettimeofday(&tmp,NULL);
	
	double time = ((double)tmp.tv_sec+(double)tmp.tv_usec/1000000)-((double)old.tv_sec+(double)old.tv_usec/1000000);

	old = tmp;

	return time;
}

void test_premiers(){
  	mpz_t integ2;
       	mpz_init (integ2);
	mpz_set_str(integ2,"0",10);

	int prem;
	int cpt = 0;

	for(prem = 0;mpz_cmp_si(integ2,100000)<=0;mpz_add_ui(integ2,integ2,1)){
		prem = first_test(integ2);
		//gmp_printf ("\nDebug compteur : %Zd\n", integ2);
		if(prem){
			gmp_printf ("Est premier : %Zd\n", integ2);
			cpt++;
		}
	}
	printf ("Nombre de premiers trouvé : %i\n", cpt);
	mpz_clear(integ2);
}

void test_carmichael(){
  	mpz_t integ2;
       	mpz_init (integ2);
	mpz_set_str(integ2,"3",10);

	int prem;
	int cpt = 0;

	for(prem = 0;mpz_cmp_si(integ2,10000000000)<=0;mpz_add_ui(integ2,integ2,2)){
		prem = mpzIs_carmichael(integ2);
		//gmp_printf ("\nDebug compteur : %Zd\n", integ2);
		if(prem){
			gmp_printf ("Est carmichael : %Zd\n", integ2);
			cpt++;
		}
	}
	printf ("Nombre de premiers trouvé : %i\n", cpt);
	mpz_clear(integ2);
}

void test_5min_carmichael(){
  	mpz_t integ2;
       	mpz_init (integ2);
	mpz_set_str(integ2,"3",10);

	int prem;
	int cpt = 0;
	chrono();
	double chr = 0.0;

	for(prem = 0;chr < 300.0;mpz_add_ui(integ2,integ2,2)){
		prem = mpzIs_carmichael(integ2);
		//gmp_printf ("\nDebug compteur : %Zd\n", integ2);
		if(prem){
			gmp_printf ("Est carmichael : %Zd\n", integ2);
			cpt++;
		}

		chr += chrono();
	}
	printf ("Nombre de premiers trouvé : %i\n", cpt);
	mpz_clear(integ2);
}

void test_1min_premiers(){
  	mpz_t integ2,res;
       	mpz_init (integ2);
	mpz_init (res);
	mpz_set_str(integ2,"0",10);

	int prem;
	chrono();
	double chr = 0.0;
	for(prem = 0;chr < 60.0;mpz_add_ui(integ2,integ2,1)){

		prem = first_test(integ2);

		if(prem)
			mpz_set(res,integ2);

		chr += chrono();
		//printf("Debug chrono : %lf\n",chr);
		
	}
	gmp_printf ("Dernier premier trouvé en 1 min: %Zd\n", res);
	mpz_clear(integ2);
}
