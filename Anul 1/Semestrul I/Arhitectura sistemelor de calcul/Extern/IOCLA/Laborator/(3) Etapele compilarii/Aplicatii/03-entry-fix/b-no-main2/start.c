// SPDX-License-Identifier: BSD-3-Clause

#include <stdlib.h>

int my_main(void);

void _start(void)
{
	my_main();

	exit(0);
}
