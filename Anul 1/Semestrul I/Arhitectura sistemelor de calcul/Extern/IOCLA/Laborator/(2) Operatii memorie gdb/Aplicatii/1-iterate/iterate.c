// SPDX-License-Identifier: BSD-3-Clause

#include <stdio.h>

int main(void)
{
	unsigned int i;
	int v[] = {0xCAFEBABE, 0xDEADBEEF, 0x0B00B135, 0xBAADF00D, 0xDEADC0DE};
	/*
	 * Vom folosi pointeri către elemente de dimensiuni diferite pentru a
	 * ușura afișarea elementelor de 1, 2 și 4 bytes.
	 */
	unsigned char *char_ptr = (unsigned char *) &v;
	unsigned short *short_ptr = (unsigned short *) &v;
	unsigned int *int_ptr = (unsigned int *) &v;

	// Parcurgem fiecare byte al vectorului v
	for (i = 0 ; i < sizeof(v) / sizeof(*char_ptr); ++i) {
		printf("%p -> 0x%x\n", char_ptr, *char_ptr);
		++char_ptr;
	}
	printf("-------------------------------\n");

	/*
	 * Parcurgem din 2 în 2 bytes, avem doar jumătate din pași fiindcă afișăm
	 * câte 2 bytes la fiecare pas.
	 */
	for (i = 0 ; i < sizeof(v) / sizeof(*short_ptr); ++i) {
		printf("%p -> 0x%x\n", short_ptr, *short_ptr);
		++short_ptr;
	}
	printf("-------------------------------\n");

	/*
	 * Parcurgem din 4 în 4 bytes, avem doar un sfert din pași fiindcă afișăm
	 * câte 4 bytes la fiecare pas.
	 */
	for (i = 0 ; i < sizeof(v) / sizeof(*int_ptr); ++i) {
		printf("%p -> 0x%x\n", int_ptr, *int_ptr);
		++int_ptr;
	}

	return 0;
}
