// SPDX-License-Identifier: BSD-3-Clause

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void magic_function(void)
{
	system("cowsay -f tux 'Good job there, my friend'");
}

char read_buffer(void)
{
	int n;
	unsigned int disorienting_var = 0xDEADBEEF;
	char buffer[64] = "\0";
	size_t i, len;

	printf("insert buffer length: ");
	scanf("%d", &n);
	getc(stdin);

	printf("\nn is %d\n", n);
	printf("insert buffer string: ");
	fgets(buffer, n, stdin);

	printf("\nn is %x\n", n);
	printf("buffer is: ");
	len = strlen(buffer);
	for (i = 0; i < len + 2; i++)
		printf(" %02X(%c)", buffer[i], buffer[i]);
	puts("");

	printf("stack variable: %X\n", disorienting_var);
	buffer[2] = disorienting_var;

	return buffer[0];
}

int main(void)
{
	read_buffer();

	return 0;
}
