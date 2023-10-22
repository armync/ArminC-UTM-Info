// SPDX-License-Identifier: BSD-3-Clause

#include <stdio.h>
#include "ops.h"

int main(void)
{
	set(10);
	printf("get(): %d\n", get());

	age = 33;
	print_age();

	return 0;
}
