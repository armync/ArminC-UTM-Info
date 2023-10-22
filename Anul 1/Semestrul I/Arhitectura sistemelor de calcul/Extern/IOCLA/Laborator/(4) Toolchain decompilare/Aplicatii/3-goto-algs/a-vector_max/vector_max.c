// SPDX-License-Identifier: BSD-3-Clause

#include <stdio.h>

int main(void)
{
	int v[] = {4, 1, 2, -17, 15, 22, 6, 2};
	int max;
	unsigned int i;

	i = 0;
	max = v[0];

loop:

	if (v[i] <= max)
		goto smaller;

	max = v[i];

smaller:
	i++;

	if (i < sizeof(v) / sizeof(int))
		goto loop;

	printf("Max is %d\n", max);

	return 0;
}
