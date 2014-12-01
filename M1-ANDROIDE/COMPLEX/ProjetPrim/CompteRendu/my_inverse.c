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
		mpz_set_str(result,"-1",10); /* No inverse */
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
