#include <stdio.h>

int main() {
		
	int n;
	int fact = 1;
	
	printf("Faktoriyel istediginiz sayi:");
	scanf("%d",&n);
	
	while (n != 0) {
		printf("%d\n",n);
		fact = fact *n;
		
		
		n--;
	
	}
	printf("Sonuc:%d ",fact);

	return 0;
}
