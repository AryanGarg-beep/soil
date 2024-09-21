#include<iostream>
using namespace std;

union test{
	int a;
	bool b;
};

int main(){
	cout << ("%d",sizeof(union test));
			}
