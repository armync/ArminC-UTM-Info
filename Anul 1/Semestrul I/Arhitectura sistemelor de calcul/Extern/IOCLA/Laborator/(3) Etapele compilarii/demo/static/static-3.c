/*
 * Author: Gabriel Mocanu <gabi.mocanu98@gmail.com>
 */

#include<stdio.h>

int initializer(void)
{
    return 50;
}

int main()
{
    static int i = initializer();
    printf(" value of i = %d", i);
    getchar();
    return 0;
}
