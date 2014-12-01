#include<stdio.h>
#include<stdlib.h>
#include"fermat.h"
#include<gmp.h>
#include<time.h>

int mpzTestFermat(mpz_t n){


	gmp_randstate_t state;
	mpz_t tmp;
	mpz_t a;
	mpz_t tmp2;
	mpz_init(tmp2);
	mpz_init(tmp);
	mpz_init(a);
	gmp_randinit_mt(state);
	gmp_randseed_ui(state,time(NULL));
	mpz_set_str(tmp,"100",10);

	do{
		mpz_urandomm(a,state,tmp);
		mpz_gcd(tmp,a,n);
		gmp_printf("A random : %Zd, gcd(%Zd,%Zd) = %Zd\n",a,a,n,tmp);

	}while(mpz_cmp_ui(tmp,1)!=0);//choisir aléatoirement un A premier avec n


	mpz_sub_ui(tmp,n,1);

	mpz_powm(tmp2,a,tmp,n);

	gmp_printf("powm : %Zd,a : %Zd, n : %Zd, n-1 : %Zd\n",tmp2,a,n,tmp);

	if(mpz_cmp_ui(tmp2,1)!=0){
		mpz_clear(tmp2);
		mpz_clear(tmp);
		mpz_clear(a);

		return 0;	
	}


	mpz_clear(tmp2);
	mpz_clear(tmp);
	mpz_clear(a);

	return 1;
}

