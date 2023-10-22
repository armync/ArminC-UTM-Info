/*
 * Author: Gabriel Mocanu <gabi.mocanu98@gmail.com>
 */

#include <stdio.h>

int main() {

    int nr = 1;
    int i = 0;

loop:

    if (i < 10) {
        i++;
        nr *= 2;
        goto loop;
    }

    printf("nr = %d\n", nr);

    return 0;
}
