#include<stdio.h>
#include<stdlib.h>
#include<gmp.h>
#include<math.h>
#include"arithZn.h"

void mpzExpo_mod(mpz_t result, mpz_t m, mpz_t e, mpz_t n){

	/*int i = 0;
	size_t fin = 0;

  	mpz_t t;
  	mpz_t m;
  	mpz_t tmp;

       	mpz_init (t);
       	mpz_init (tmp);

	mpz_set(t,m);
	mpz_set(result,b);

	fin = mpz_sizeinbase(e,2);

	for(i = 0;i < fin;i++){//Comparaison entre i et e
		if(
	}	


	mpz_clear(t);
	mpz_clear(tmp);*/
}


void mpz_max(mpz_t result, mpz_t a,mpz_t b){

	if(mpz_cmp(a,b)>=0)
		mpz_set(result,a);
	else
		mpz_set(result,b);
}


void mpz_min(mpz_t result, mpz_t a,mpz_t b){
	
	if(mpz_cmp(a,b)<=0)
		mpz_set(result,a);
	else
		mpz_set(result,b);
}

void mpzMy_pgcd(mpz_t result,mpz_t a, mpz_t b){
		mpz_t min;
  		mpz_t max;
  		mpz_t tmp;

       		mpz_init (min);
       		mpz_init (max);
       		mpz_init (tmp);

		mpzMy_pgcdMemSave(result,a,b,min,max,tmp);

		mpz_clear(min);
		mpz_clear(max);
		mpz_clear(tmp);
}

void mpzMy_pgcdMemSave(mpz_t result,mpz_t a, mpz_t b,mpz_t min,mpz_t max,mpz_t tmp){

	if(mpz_cmp(a,b)==0)
		mpz_set(result,a);
	else{


		mpz_max(max,a,b);
		mpz_min(min,a,b);
		mpz_sub(tmp,max,min);

		mpzMy_pgcdMemSave(result,tmp,min,min,max,tmp);
	

	}
}

void mpzFastExp(mpz_t result, mpz_t m, mpz_t e){
/*U ← 1 T ← m,
Pour i = 0 ` Nb − 1 Faire
a
Si ei = 1 alors U ← T · U mod N
T ← T · T mod N
Retourner U*/

	mpz_t u,t;
	mpz_set_str(u,"1",10);
	mpz_set(t,m);



	mpz_clear(u);
	mpz_clear(t);
}

void mpzMy_inverse(mpz_t result, mpz_t a, mpz_t n)
{
        mpz_t t, nt, r, nr, q, tmp,tmpa, tmpn;
       	mpz_init (t);
       	mpz_init (nt);
       	mpz_init (r);
       	mpz_init (nr);
	mpz_init (q);
	mpz_init (tmp);
	mpz_init (tmpa);
	mpz_init (tmpn);

       if (mpz_sgn(n) == -1) 
		mpz_neg(tmpn,n);

        if (mpz_sgn(a) == -1) {
		mpz_neg(tmpa,a);
		mpz_mod(tmpa,tmpa,n);
		mpz_sub(tmpa, n,tmpa);
	}

	mpz_set(tmpn,n);
	mpz_set(tmpa,a);
	mpz_set_str(nt,"1",10);
	mpz_set(r,tmpn);
	mpz_mod(nr,a,tmpn);

        while (mpz_sgn(nr) != 0) {
		mpz_tdiv_q(q,r,nr);

		mpz_set(tmp,nt);
		mpz_mul(nt,q,nt);
		mpz_sub(nt,t,nt);
		mpz_set(t,tmp); 

		mpz_set(tmp,nr);
          	mpz_mul(nr,q,nr);
		mpz_sub(nr,r,nr);
		mpz_set(r,tmp);
        }

        if (mpz_sgn(t) == -1){
 		mpz_add(t,t,tmpn);
		mpz_set(result,t);
	}

	mpz_set(result,t);		

        if (mpz_cmp_d(r,1.0) < 0){ /*plus grand que 1*/ 
		mpz_set_str(result,"-1",10);  /* No inverse */
	}

	mpz_clear(t);
	mpz_clear(nt);
	mpz_clear(r);
	mpz_clear(nr);
	mpz_clear(q);
	mpz_clear(tmp);
	mpz_clear(tmpa);
	mpz_clear(tmpn);
}

int iMod_exp(int m, int e, int n){

	int t = m;
	int i = 0;
	
	

	for(i = 1;i < e;i++){
		t = (t*m)%n;
	}	

	return t;
}

int iMy_pgcd(int a, int b){

	int result = 0;
	if(a == b)
		result = a;
	else
		result = iMy_pgcd(fmax(a,b)-fmin(a,b),fmin(a,b));

	return result;
}

int iMy_inverse(int a, int b)
{
	int t, nt, r, nr, q, tmp;
	if (b < 0) 
		b = -b;
        if (a < 0) 
		a = b - (-a % b);
        t = 0;  
	nt = 1;  
	r = b;  
	nr = a % b;

        while (nr != 0) {
          	q = r/nr;
	
          	tmp = nt;  
		nt = t - q*nt;
		t = tmp;
          
		tmp = nr;  
		nr = r - q*nr;  
		r = tmp;	
	}
        if (r > 1) 
		return -1;  // No inverse 

        if (t < 0) 
		t += b;


        return t;
}
