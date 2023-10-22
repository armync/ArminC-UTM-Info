// SPDX-License-Identifier: BSD-3-Clause

#include <stdio.h>

static unsigned int price;
unsigned int qty;

void set_price(unsigned int v)
{
	price = v;
}

void print_price(void)
{
	printf("price is %u\n", price);
}

void print_quantity(void)
{
	printf("quantity is %u\n", qty);
}
