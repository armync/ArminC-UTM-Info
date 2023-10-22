// SPDX-License-Identifier: BSD-3-Clause

extern unsigned int qty;

void set_price(unsigned int v);
void print_price(void);
void print_quantity(void);

int main(void)
{
	/*
	 * TODO: Make it so you print:
	 *    price is 21
	 *    quantity is 42
	 * without directly calling a printing function from an existing
	 * library(do NOT use printf, fprintf, fwrite, ...).
	 */
	qty = 42;
	set_price(21);
	print_price();
	print_quantity();

	return 0;
}
