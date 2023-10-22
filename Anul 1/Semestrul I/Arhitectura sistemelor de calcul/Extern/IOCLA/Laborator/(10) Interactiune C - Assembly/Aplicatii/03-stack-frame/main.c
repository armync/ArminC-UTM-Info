// SPDX-License-Identifier: BSD-3-Clause

#include <stdio.h>

void print_hello(void);

void asm_call_wrapper(void)
{
	print_hello();
	printf(" world");
}


int main(void)
{
	asm_call_wrapper();
	printf("!\n");

	return 0;
}
