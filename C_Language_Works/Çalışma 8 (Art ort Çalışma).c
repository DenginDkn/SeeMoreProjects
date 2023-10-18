#include <stdio.h>

int main(){
	int a,b,c,d,e;
	
	float  aritmetik;
	
	printf("Please enter 5 numbers:");
	scanf("%d %d %d %d %d",&a,&b,&c,&d,&e);
	aritmetik = (a+b+c+d+e)/5.0;
	printf("You will see aritmetik mean of your numbers %.2f",aritmetik);
	

	return 0;
}

