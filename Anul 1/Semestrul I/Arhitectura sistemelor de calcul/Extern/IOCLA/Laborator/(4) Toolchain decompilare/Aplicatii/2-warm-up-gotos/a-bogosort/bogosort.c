// SPDX-License-Identifier: BSD-3-Clause

#include <stdio.h>
#include <stdlib.h>

/* checks if the array is sorted */
static int is_sorted(int a[], int n)
{
	int i;

	for (i = 1; i < n; i++)
		if (a[i] < a[i-1])
			return 0;

	return 1;
}

/* shuffle an array */
static void shuffle(int a[], int n)
{
	int i;
	int t, r;

	for (i = 0; i < n; i++) {
		t = a[i];
		r = rand() % n;
		a[i] = a[r];
		a[r] = t;
	}
}

int main(void)
{
	int numbers[] = {1, 13, 2,  5, 3, -7};
	int i;

	while (1) {
		shuffle(numbers, 6);

		if (is_sorted(numbers, 6))
			/* TODO use goto instead of break */
			break;
	}

	for (i = 0; i < 6; i++)
		printf("%d ", numbers[i]);
	printf("\n");

	return 0;
}
