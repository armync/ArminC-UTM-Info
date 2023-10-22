#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

void usage(void)
{
	printf("Usage: ./crackme <password>\n");
	exit(0);
}

int main(int argc, char *argv[])
{

	if (argc == 2) {
		uint32_t len = strlen(argv[1]);

		if (len == 8) {
			if (*(argv[1] + 3) == 'E') {
				printf("Good job!\n");
				exit(0);
			}
		}
		printf("Try again!\n");
	} else
		usage();

	return 0;
}
