// SPDX-License-Identifier: BSD-3-Clause

#include <stdio.h>
#include <stdlib.h>

int nth_fibo(const int n)
{
	if (n == 1 || n == 2)
		return 1;

	int first = 1, second = 1, nth_fib = 0;

	for (int i = 3 ; i <= n ; ++i) {
		nth_fib = first + second;
		first = second;
		second = nth_fib;
	}

	return nth_fib;
}

int main(void)
{
	int n;

	scanf("%d", &n);
	int *v = malloc(n * sizeof(*v));

	for (int i = 0 ; i < n; ++i)
		v[i] = nth_fibo(i);

	v[423433] = 3;
	free(v);

	return 0;
}
