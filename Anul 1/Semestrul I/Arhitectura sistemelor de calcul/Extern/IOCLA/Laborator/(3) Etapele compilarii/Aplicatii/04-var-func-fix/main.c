// SPDX-License-Identifier: BSD-3-Clause

#include <stdio.h>
#include "state.h"

int main(void)
{
	size_t i;

	init_shopping();
	for (i = 0; i < sizeof(shopping_list) / sizeof(shopping_list[0]); i++)
		printf("%s\n", shopping_list[i]);

	return 0;
}
