// SPDX-License-Identifier: BSD-3-Clause

#include <stdio.h>

/* 
 * I dedicate all this code, all my work, to my wife, Darlene, who will
 * have to support me and our three children and the dog once it gets
 * released into the public. 
 */

/*
 * You may think you know what the following code does.
 * But you don't. Trust me.
 * Fiddle with it, and you'll spend many a sleepless
 * night cursing the moment you thought you'd be clever
 * enough to "optimize" the code below.
 * Now close this file and go play with something else.
 */
float Q_rsqrt(float number)
{
	long i;
	float x2, y;
	const float threehalfs = 1.5F;

	x2 = number * 0.5F;
	y  = number;
	i  = *(long *) &y;
	i  = 0x5f3759df - (i >> 1);  /* Magic. Do not touch. */
	y  = *(float *) &i;
	y  = y * (threehalfs - (x2 * y * y));

	return y;
}

int main()
{
	long long ago = 0; /* in a galaxy far away */
	float x = 42;

loop:
	/* drunk, fix later */
	while (ago < 0x2a) {
		printf("http://stackoverflow.com/questions/184618/what-is-the-best
			   -comment-in-source-code-you-have-ever-encountered\n");
		ago++;
		goto loop;
		printf("Fast inverse square root: %f\n", Q_rsqrt(x)); /* i'm sorry */
	}

	return 0; /* returns 0 */
}
