/*
 * Author: Gabriel Mocanu <gabi.mocanu98@gmail.com>
 */

#include <stdio.h>

int main()
{
    static int x; // .bss section
    int y;
    printf("%d \n %d", x, y);
}
