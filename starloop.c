#include<stdio.h>
void loop(int num){
	int i,j;
	for(i=1;i<=num;i++){
                for(j=1;j<=i;j++){
                        printf("*");
                }
		printf("\n");
	}
}
	
int main(){
	int num;
	printf("Enter limit: ");
	scanf("%d",&num);
	loop(num);
	}

