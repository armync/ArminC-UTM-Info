// SPDX-License-Identifier: BSD-3-Clause

#include <stdio.h>

int main(void)
{
	int v[] =  {1, 2, 15, 51, 53, 66, 202, 7000};
	int dest = v[2]; /* 15 */
	int start = 0;
	int end = sizeof(v) / sizeof(int) - 1;
	int middle;

loop:
	if (start == end)
		goto out;

	middle = (end + start) / 2;

	/* Search to the left */

	if (v[middle] < dest)
		goto bigger;

	end = middle;
	goto loop;

bigger:
	/* Search to the right */

	start = middle + 1;
	goto loop;

out:
	printf("Found dest %d on pos %d\n", dest, start);

	return 0;
}
