#include<stdio.h>
int main(){
	
	int midterm1,midterm2,final;
	float classmean;
	
	printf("Enter your first midterm note:");
	scanf("%d",&midterm1);
	printf("Enter your second midterm note:");
	scanf("%d",&midterm2);
	printf("Enter your final note:");
	scanf("%d",&final);
	
	classmean = (midterm1 + midterm2 + final) /3.0;
	
	if(classmean > 60) 	printf("You will pass your class.");
		
		
	
	else	printf("You dont pass your class.");
	
	
	
	return 0;
}
