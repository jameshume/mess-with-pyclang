#include <stdint.h>

static const int test_static_global = 1;

enum MyTestEnum {
	TEST_ENUM_1,
	TEST_ENUM_2,
	TEST_ENUM_3
};

typedef enum {
	XTEST_ENUM_1,
	XTEST_ENUM_2,
	XTEST_ENUM_3
} xenum_t;

typedef enum MySecondTestEnum {
	TEST_SECOND_ENUM_1,
	TEST_SECOND_ENUM_2,
	TEST_SECOND_ENUM_3
} MySecondTestEnum_t;

typedef struct tstruct {
	int a;
} tstruct_t;

void do_something(enum MyTestEnum a, int b, char c)
{
	printf("%u %d, %hhu", a, b, c);
}

#define TEST_MACRO(x) (x)

int MainFunction(const int param1)
{
	static const int test_static_local = 1;
	enum MyTestEnum testEnum1 = TEST_ENUM_2;
	MySecondTestEnum_t testEnum2 = TEST_SECOND_ENUM_3;

	const int testShift = (test_static_local & 0x1f) << 16;
	const int testMacro = TEST_MACRO(33);

	const int testArray[] = {1,2,3,4};

	do_something(testEnum1, 101, 'f');

	UNDEF1(testEnum1, 2, "String literal test blah blah blah", UNDEF2(testEnum1,2,3) | UNDEF2(test_static_local,2,3));
	UNDEF1(testEnum1, 2, "String literal test blah blah blah", UNDEF2(testEnum1,2,3));
	UNDEF1(testEnum1, 2, "String literal test blah blah blah", 0);
}
