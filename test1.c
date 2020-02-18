#include<stdio.h>

struct employee{
	int id;
	char name[100];
};

int main()
{
	printf("Hello World\n");
	struct employee e1={1,"Bapan"};
	printf("%d\t%s",e1.id,e1.name);
	return 0;
}