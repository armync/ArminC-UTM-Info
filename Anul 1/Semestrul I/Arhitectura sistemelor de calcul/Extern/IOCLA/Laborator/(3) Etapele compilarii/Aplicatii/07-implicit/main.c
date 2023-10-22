// SPDX-License-Identifier: BSD-3-Clause

#include <stdio.h>

unsigned long long compute_double(unsigned long long val);

int main() {
	unsigned long long val = 0xFFFFFFFF;
	unsigned long long double_val;

	double_val = compute_double(val);

	printf("2 * %llx = %llx\n", val, double_val);

	return 0;
}
