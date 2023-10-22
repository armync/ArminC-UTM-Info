// SPDX-License-Identifier: BSD-3-Clause

#include <stdio.h>
#include <stdlib.h>

void *find_max(void *arr, int n, size_t element_size,
				int (*compare)(const void *, const void *))
{
	void *max_elem = arr;

	for (int i = 0; i < n; i++) {
		void *cur_element = (char *)arr + i * element_size;

		if (compare(cur_element, max_elem) > 0)
			max_elem = cur_element;
	}

	return max_elem;
}

int compare(const void *a, const void *b)
{
	return *(int *)a > *(int *)b ? 1 : 0;
}

int main(void)
{
	int n;

	int *arr = malloc(n * sizeof(*arr));

	if (arr == NULL) {
		perror("malloc");
		exit(1);
	}

	scanf("%d", &n);

	for (int i = 0 ; i < n; i++)
		scanf("%d", &arr[i]);

	int *max_elem = (int *)find_max(arr, n, sizeof(*arr), compare);

	printf("Elementul maxim este: %d\n", *max_elem);

	free(arr);
	return 0;
}
