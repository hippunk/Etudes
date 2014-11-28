#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include"carmichael.h"
#include"naif.h"

int iIs_carmichael(int n){

	//int result = 1; 

	if((n%2) == 0)
		return 0;

	int a = 0;
	for(a = 1;a < n;a++){
		if(((int)(pow(a,n-1)-1)%(n-1))==a)
			return 0;
	}
	
	return 1;
}

