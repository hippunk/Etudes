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