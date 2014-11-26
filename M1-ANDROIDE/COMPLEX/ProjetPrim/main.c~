#include<stdio.h>
#include<stdlib.h>
#include"arithZn.h"
#include<gmp.h>

int main(){

	printf("Hello World\n");

  	mpz_t integ1;
  	mpz_t integ2;
	mpz_t integ3;
  	mpz_t res;

       	mpz_init (integ1);
       	mpz_init (integ2);
       	mpz_init (integ3);
       	mpz_init (res);

	mpz_set_str(integ1,"4",10);
	mpz_set_str(integ2,"13",10);
	mpz_set_str(integ3,"497",10);

	mpzExpo_mod(res,integ1,integ2,integ3);
	
	printf("mod exp : ");	
	mpz_out_str(stdout, 10, res);
	printf("\n");

        printf("mod exp int :%i\n", iMod_exp(4, 13, 497));


	mpz_clear(integ1);
	mpz_clear(integ2);
       	mpz_clear(integ3);
	mpz_clear(res);

	return EXIT_SUCCESS;
}
