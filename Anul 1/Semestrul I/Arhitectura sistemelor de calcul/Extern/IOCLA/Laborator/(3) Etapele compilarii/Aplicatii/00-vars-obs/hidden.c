static int hidden_value;

void init(void)
{
	hidden_value = 0;
}

void set(int value)
{
	hidden_value = value;
}

int get(void)
{
	return hidden_value;
}
