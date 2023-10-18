#include <stdio.h>
#include <math.h>
int main(){
	int a,b,c;
	float x1,x2;
	float delta;
	
	printf("Enter your a value for your equation:");
	scanf("%d",&a);
	printf("Enter your b value for your equation:");
	scanf("%d",&b);
	printf("Enter your c value for your equation:");
	scanf("%d",&c);
	
	delta = b*b-4*a*c;
	x1 = (-b + (sqrt(delta)) ) /2*a;
	x2 = (-b - (sqrt(delta)) ) /2*a;
	printf("This is a first value of equation %.1f, This is second value of equation %.1f",x1,x2);
	

	
	
	return 0;
}
