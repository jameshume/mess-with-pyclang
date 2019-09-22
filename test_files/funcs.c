static void static_void_func_no_params(void);
void void_func_no_params(void);
long func_with_params(char a, short b, int c);


static void static_void_func_no_params(void)
{

}


void void_func_no_params(void)
{
	static_void_func_no_params();
}


long func_with_params(char a, short b, int c)
{
	return a * b * c;
}

void call_func_with_params(void)
{
	long a;
	a = func_with_params('c', 10, 100);
}

void use_a_function_pointer(void)
{
	void(*ptr)(char a, short b, int c);

	ptr = &func_with_params;

	struct
	{
		void(*ptr)(char a, short b, int c);
	} s;

	s.ptr = &func_with_params;

	ptr(1, 2, 3);
}