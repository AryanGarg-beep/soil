#include<stdio.h>
 int main(){
	 int x = 10;
	 printf("%d\n",x++);
	 printf("%d\n",++x);
	 x = 10;
	 printf("%d\n",x++ + ++x);
	 return 0;
 }
