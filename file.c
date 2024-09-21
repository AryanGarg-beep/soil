/*
#include<stdio.h>
int main(){
	printf("hello\n");
	return 0;
}*/

#include<stdio.h>
struct test1{
	int a;
	int* b;
	int c;
};

struct test2{
	int a,c;
	int *b;
};



int main(){
	int size1,size2,*b;

	size1 = sizeof(struct test1);
	printf("%d\n",size1);
	size2 = sizeof(struct test2);
	printf("%d\n",size2);
}


