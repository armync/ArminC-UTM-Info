#include <stdio.h>

static void second_func(int *p, int a)
{
	*p += a;
}

static int first_func(int a)
{
	int b = 3;

	puts("Hello, World!");
	second_func(&a, b);

	return a;
}

int main(void)
{
	printf("Value returned is: %d\n", first_func(15));
	return 0;
}
