#include<stdio.h>
#include<stdlib.h>
#include"carmichael.h"
#include"test.h"

int main(){

	//test_premiers();
	mpz_t nb;

       	mpz_init (nb);
       	
       	mpz_set_str(nb,"14",10);
	test_pow();
	printf("est carmichael 13 : %i\n",iIs_carmichael(15));
	printf("est carmichael 561 : %i\n",iIs_carmichael(561));
	printf("est carmichael 560 : %i\n",iIs_carmichael(560));
	printf("est carmichael : %i\n",mpzIs_carmichael(nb));//mpzIs_carmichael(13));
	//printf("Calcul test : %i\n",6);
	mpz_clear(nb);
	
	return EXIT_SUCCESS;
}
