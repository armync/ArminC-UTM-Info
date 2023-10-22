// SPDX-License-Identifier: BSD-3-Clause

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

static void success(void)
{
	puts("Great success!");
}

static void fail(void)
{
	puts("Epic failure!");
}

static void check_string(const char *str)
{
	unsigned int flag = 0x12345678;
	char buffer[32];

	strcpy(buffer, str);
	buffer[15] = str[1];

	if (flag == 0x4e305250)
		success();
	else
		fail();
}

int main(int argc, char **argv)
{
	if (argc != 2) {
		fprintf(stderr, "Usage: %s <string>\n", argv[0]);
		exit(EXIT_FAILURE);
	}

	check_string(argv[1]);

	return 0;
}
