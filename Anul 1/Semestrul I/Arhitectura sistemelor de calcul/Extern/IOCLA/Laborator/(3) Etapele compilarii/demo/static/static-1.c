/*
 * Author: Gabriel Mocanu <gabi.mocanu98@gmail.com>
 */

#include<stdio.h>
int fun()
{
	static int count = 0;
	count++;
	return count;
}
int fun2()
{
	static int count = 0;
	count++;
	return count;
}
int main()
{
	printf("%d ", fun());
	printf("%d ", fun2());
	return 0;
}
