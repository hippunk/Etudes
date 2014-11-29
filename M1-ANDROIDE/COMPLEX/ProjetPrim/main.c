#include<stdio.h>
#include<stdlib.h>
#include"carmichael.h"
#include"test.h"

int main(){

	//test_premiers();
	printf("est carmichael : %i\n",iIs_carmichael(13));
	return EXIT_SUCCESS;
}
