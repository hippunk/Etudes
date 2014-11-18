#include<stdio.h>
#include<stdlib.h>
#include"arithZn.h"
#include<gmp.h>

int main(){

	printf("Hello World\n");

  	mpz_t integ1;
  	mpz_t integ2;
  	mpz_t res;

       	mpz_init (integ1);
       	mpz_init (integ2);
       	mpz_init (res);

	mpz_set_str(integ1,"-486",10);
	mpz_set_str(integ2,"217",10);

	mpzMy_inverse(res,integ1,integ2);
	
	printf("L'inverse est : ");	
	mpz_out_str(stdout, 10, res);
	printf("\n");

        printf("%i\n", iMy_inverse(-486, 217));


	mpz_clear(integ1);
	mpz_clear(integ2);
	mpz_clear(res);

	return EXIT_SUCCESS;
}
