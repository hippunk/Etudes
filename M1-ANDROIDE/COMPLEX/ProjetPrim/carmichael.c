#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<gmp.h>
#include"carmichael.h"
#include"arithZn.h"
#include"naif.h"

int iIs_carmichael(int n){

	//int result = 1; 

	if() //test si n premier a faire
		return 0;

	int a = 0;
	for(a = 2;a < n;a++){
		if(iMy_pgcd(a,n)==1) 		
			if(((int)(pow(a,n-1)-1)%(n-1))==a)
		 		return 0;
	}
	
	return 1;
}

/*int mpzIs_carmichael(mpz_t n){

	if(first_test(n) == 1) //test si n premier a faire
		return 0;

  	mpz_t tmp;
  	mpz_t a;

       	mpz_init (tmp);
       	mpz_init (a);

	mpz_set(t,m);

	mpz_set_str(a,"2",10);

	for(;mpz_cmp(a,n)<0;mpz_add_ui(a,a,1)){
		//pour tout a premier avec n 


		if(((int)(pow(a,n-1)-1)%(n-1))==a)
			return 0;
	}
	
	mpz_clear(t);
	mpz_clear(a);

	return 1;
}*/
