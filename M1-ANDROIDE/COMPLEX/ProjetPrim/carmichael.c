#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<gmp.h>
#include"carmichael.h"
#include"arithZn.h"
#include"naif.h"

int iIs_carmichael(int n){
	//int result = 1;
	if((n%2) == 0)
		return 0;
	int a = 0;
	
	for(a = 1;a < n;a++){
		if(((int)(pow(a,n-1)-1)%(n))!=0)
			return 0;
	}
	return 1;
}

void mpz_pow(mpz_t result,mpz_t e,mpz_t n){

	mpz_t a;
       	mpz_init (a);
	//gmp_printf("Dans pow : e = %Zd, n = %Zd\n",e,n);
 	mpz_set_str(a,"1",10);
 	mpz_set_str(result,"1",10);

	for(;mpz_cmp(a,n)<=0;mpz_add_ui(a,a,1)){
		mpz_mul(result,result,e);
	}

	mpz_clear(a);

}

int mpzIs_carmichael(mpz_t n){

	if(first_test(n) == 1){ //test si n premier a faire
		return 0;
	}

  	mpz_t tmp;
  	mpz_t a;

       	mpz_init (tmp);
       	mpz_init (a);

	mpz_set(tmp,n);

	mpz_set_str(a,"2",10);

	mpz_sub_ui(n,n,1);
	gmp_printf("n - 1 : %Zd\n",n);

	for(;mpz_cmp(a,n)<0;mpz_add_ui(a,a,1)){
	
		mpz_pow(tmp,a,n);
		gmp_printf("\n\na^n-1 : %Zd\n",tmp);
		mpz_sub_ui(tmp,tmp,1);
		gmp_printf("a^n-1 mod n-1 : %Zd\n",tmp);
		mpz_mod(tmp,tmp,n);
		gmp_printf("n - 1 : %Zd,a = %Zd\n\n",n,a);
		
		if(mpz_cmp(tmp,a)==0)
			return 0;
	}
	mpz_add_ui(n,n,1);
	mpz_clear(tmp);
	mpz_clear(a);

	return 1;
}
