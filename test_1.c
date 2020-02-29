#include<stdio.h>
int main()
{
	char m[10]="Hello";
	int start=0;
	int end=4;
	printf("The array before reversing is %s\n",m);
	while(start<=end)
	{
		char temp=m[start];
		m[start]=m[end];
		m[end]=temp;
		start++;
		end--;
	}
	printf("The array after reversing is:\n");
	printf("%s",m);
	return 0;
}