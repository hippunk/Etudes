#include<stdio.h>
#include<stdlib.h>
#include<gmp.h>
#include<math.h>
#include"arithZn.h"

void mpz_max(mpz_t a, mpz_t b,mpz_t result){

	if(mpz_cmp(a,b)>=0)
		mpz_set(result,a);
	else
		mpz_set(result,b);
}

void mpz_min(mpz_t a, mpz_t b,mpz_t result){
	
	if(mpz_cmp(a,b)<=0)
		mpz_set(result,a);
	else
		mpz_set(result,b);
}

void mpzMy_pgcd(mpz_t result,mpz_t a, mpz_t b){

	if(mpz_cmp(a,b)==0)
		mpz_set(result,a);
	else
		mpz_set(result,mpzMy_pgcd(a, b));

}

int iMy_pgcd(int a, int b){

	int result = 0;
	if(a == b)
		result = a;
	else
		result = iMy_pgcd(fmax(a,b)-fmin(a,b),fmin(a,b));

	return result;
}

