void super_log(unsigned long lon/g val);

int main(void)
{
	unsigned int a = 0x1234;
	super_log( (a & 0xff) << 8 );
	return 0;
}