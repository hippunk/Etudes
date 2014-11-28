#include <stdlib.h>
#include <stdio.h>
#include <math.h>   
#include <ctype.h>
#include <time.h>


int my_pgcd(tmp1,tmp2){
  // on identifie le plus grand nombre des deux 
  int a,b;
  if(tmp1>=tmp2){
    a=tmp1;
    b=tmp2;
  } else {
    a=tmp2;
    b=tmp1;
  }
  // declaration des variables  
  int i=1;
  int rplus=b;
  int u=0;
  int v=1;
  int r=a;
  int umoins=1;
  int vmoins=0;
  int q,rmoins;
  int vplus, uplus;
  while( (r != 0) || (r != 1) ){
    if(rplus==0)
      break;
    rmoins=r;
    r=rplus;
    q=rmoins/r;
    rplus=rmoins%r;
    uplus=umoins - q*u;
    vplus=vmoins - q*v;
    printf("i : %d || r-1 : %d || q : %d || r : %d || r+1 : %d || u+1 : %d || v+1 : %d\n",
	   i,rmoins,q,r,rplus,uplus,vplus);
    umoins=u;
    vmoins=v;
    v=vplus;
    u=uplus;
    i++;
  }
  printf("Le PGCD de %d et %d est : %d\n",a,b,r);
  return r;
}


int my_inverse(a,n){
/* Declaration des variables qui vont servir a calculer le PGCD de a et b et
     la relation de Bezout */
  int i=1;
  int rplus=n;
  int u=0;
  int v=1;
  int r=a;
  int umoins=1;
  int vmoins=0;
  int q,rmoins;
  int vplus, uplus;
  
  // Algo de calcul
  while( (r != 0) || (r != 1) ){
    if(rplus==0)
      break;
    rmoins=r;
    r=rplus;
    q=rmoins/r;
    rplus=rmoins%r;
    uplus=umoins - q*u;
    vplus=vmoins - q*v;
    umoins=u;
    vmoins=v;
    v=vplus;
    u=uplus;
    i++;
  }
  if(umoins<0)
    umoins=umoins+n;
  printf("L'inverse modulaire de %d modulo %d est : %d\n",a,n,umoins);
  return umoins;
}


int expo_mod(m,e,n){
  int u=m;
  int i;
  for(i=1;i<e;i++)
    u=(u*m)%n;
  return u;
}


int first_test(n){
  int i;
  int res=1;
  if(n%2==0 || n%5==0)
    return -1;
  double k=sqrt(n);
  int o=(int)k;
  for(i=2;i<=o;i++){
    if((n%i)==0)
      res=-1;
  }
  return res;
}


int is_Carmichael(n){
  int test=n-1;
  int res=-1;
  int i;
  int cpt=n;
  for(i=3;i<n;i+=2){
    if(first_test(i)==1){
      if(((n%i)==0) && (test%(i-1)==0)){
	cpt=cpt/i;
	/*printf("%d\n",i);*/
      }
    }
    if(cpt==1)
      break;
  }
  if(cpt==1)
    res=1;
  return res;
}

/*si on choisis (ici 70) un nb trop grand, c'est long..*/
int Gen_nombrePremier(){
  int p=1;
  int cpt;
  while(p==1){
    cpt=rand()%(70-3)+3;
    if(first_test(cpt)==1)
      p=-1;
  }
  return cpt;
}


int Gen_Carmichael(){
  time_t t;
  srand((unsigned) time(&t));
  int number;
  int tmp;
  int cpt=0;
  int c1;
  int c2;
  int c3;
  int test;
  while(cpt==0){
    tmp=0;
    srand((unsigned) time(&t));
    c1=Gen_nombrePremier();
    c2=Gen_nombrePremier();
    while(c2==c1)
      c2=Gen_nombrePremier();
    c3=Gen_nombrePremier();
    while(c3==c2 || c3==c1) 
      c3=Gen_nombrePremier();
    number=c1*c2*c3;
    test=number-1;
    
    if(number%2!=0){
      if(((number%c1)==0) && (test%((c1)-1)==0))
	tmp++;
      if(((number%c2)==0) && (test%((c2)-1)==0))
	tmp++;
      if(((number%c3)==0) && (test%((c3)-1)==0))
	tmp++;
	}
    
    if(tmp==3)
    cpt=1;
  }
  printf("%d\n",c1);
  printf("%d\n",c2);
  printf("%d\n",c3);
  return number;
}


/*fonctionne mais on met 45 min à calculer ça quoi..*/
int list_Carmichael(k){
  if(k<561){
    printf("Le plus petit nombre de Carmichael est 561");
    return -1;
  }
  int cpt=0;
  int i;
  for(i=561;i<=k;i+=2){
    if(is_Carmichael(i)==1){
      printf("%d\n",i);
      cpt++;
    }
  }
  return cpt;
}


int test_Fermat(n){
  int a;
  a=rand()%((n-1)-2)+2;
  return expo_mod(a,n-1,n);
}

double experimental_Fermat(nbtirage){
  int k=100000;
  int i;
  int nb_erreur=0;
  int nb_fois=0;
  int tmp;
  for(i=0;i<nbtirage;i++){
    tmp=rand()%(k-3)+3;
    // printf("%d\n",tmp);
    if(test_Fermat(tmp)==1){
      nb_fois++;
      //printf("%d\n",nb_fois);
      if(first_test(tmp)!=1)
	nb_erreur++;
     
    }
  }
  printf("%d\n",nb_erreur);
  printf("%d\n",nb_fois);
  double f=nb_erreur*100.0;
  double p=nb_fois;
  double res=f/p;
  
  return res;
}
  

int TestRabinMiller(n){
  if(n%2==0){
    // printf("il faut un nombre impaire\n");
    return 0;
  }
  int k=n-1;
  int cpt=1;
  int s=1;
  int r=1;
  int a=rand()%(k-2)+2;
  while(cpt==1){
    r=1;
    while((pow(2,s)*r)<k){
      r=r+2;
    }
    if((pow(2,s)*r)==k)
      cpt=-1;
    else
      s+=1;
  }
  //printf("s: %d     r: %d\n",s,r);
  int reste=expo_mod(a,r,n);
  if(reste==1 || reste==-1){
    printf("premier\n");
    return 1;
  }
  else {
    int j=1;
    while(j<=s-1 && (reste!=1 || reste!=-1)){
      reste=expo_mod(reste,2,n);
      if(reste==1){
	printf("composé\n");
	return -1;
      }
      j++;
    }
  }
  if(reste!=-1){
    printf("composé\n");
    return -1;
  }
  printf("premier");
  return 1;
}


double experimental_RabinMiller(nbtirage){
  int k=100000;
  int i;
  int nb_erreur=0;
  int nb_fois=0;
  int tmp;
  for(i=1;i<nbtirage;i+=2){
    tmp=rand()%(k-3)+3;
    if(TestRabinMiller(tmp)==1){
      nb_fois++;
      if(first_test(tmp)!=1)
	nb_erreur++;
    }
  }
  printf("%d\n",nb_erreur);
  printf("%d\n",nb_fois);
  double f=nb_erreur*100.0;
  double p=nb_fois;
  double res=f/p;
  return res;
}

int GenPKRSA(int t){
  int p,q,n;
  int cpt=1;
  int h=pow(2,t);
  while(cpt==1){
    int tmp=rand()%(h-3)+3;
    if(TestRabinMiller(tmp)==1 && test_Fermat(tmp)==1){
      cpt=2;
      p=tmp;
    }
  }
  while(cpt==2){
    int tmp=rand()%(h-3)+3;
     if(TestRabinMiller(tmp)==1 && test_Fermat(tmp)==1){
       cpt=3;
       q=tmp;
     }
  }
  printf("p: %d    q: %d\n",p,q);
  n=p*q;
  return n;
}


    

  

