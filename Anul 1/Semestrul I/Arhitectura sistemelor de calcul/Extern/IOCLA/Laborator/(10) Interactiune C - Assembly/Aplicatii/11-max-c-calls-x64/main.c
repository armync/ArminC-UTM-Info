// SPDX-License-Identifier: BSD-3-Clause

#include <stdio.h>

unsigned int get_max(unsigned int *arr, unsigned int len);

int main(void)
{
	unsigned int arr[] = { 19, 7, 129, 87, 54, 218, 67, 12, 19, 99 };
	unsigned int max;

	max = get_max(arr, 10);

	printf("max: %u\n", max);

	return 0;
}
