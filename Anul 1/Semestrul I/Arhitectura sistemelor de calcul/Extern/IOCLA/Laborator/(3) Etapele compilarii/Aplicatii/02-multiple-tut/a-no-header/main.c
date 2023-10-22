#include <stdio.h>

int add(int a, int b);
int sub(int a, int b);

int main(void)
{
	printf("add(10, 3): %d\n", add(10, 3));
	printf("sub(10, 3): %d\n", sub(10, 3));

	return 0;
}
