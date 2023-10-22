// SPDX-License-Identifier: BSD-3-Clause

#include <stdio.h>

char v[] = "ana are mere";
char *p = "ana are mere";

int main(void)
{
	printf("sizeof(v): %zu\n", sizeof(v));
	printf("sizeof(p): %zu\n", sizeof(p));

	printf("v[1]: %c\n", v[1]);
	printf("p[1]: %c\n", p[1]);

	v[1] = 'd';
	//p[1] = 'd'; /* this seg faults */

	return 0;
}
