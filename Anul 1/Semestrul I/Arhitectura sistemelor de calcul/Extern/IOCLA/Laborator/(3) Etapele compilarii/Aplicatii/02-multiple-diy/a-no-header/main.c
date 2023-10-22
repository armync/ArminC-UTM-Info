// SPDX-License-Identifier: BSD-3-Clause

#include <stdio.h>

int mul(int a, int b);
int div(int a, int b);

int main(void)
{
	printf("mul(10, 5): %d\n", mul(10, 5));
	printf("div(10, 5): %d\n", div(10, 5));

	return 0;
}
