// SPDX-License-Identifier: BSD-3-Clause

extern int puts(const char*);
static void hi(void)
{
	puts("Hi!");
}

static void bye(void)
{
	puts("Bye!");
}

int main(void)
{
	hi();
	bye();
}
