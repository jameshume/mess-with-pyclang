#include "fake_include.h"

typedef enum {
	ANON_BUT_TYPEDEFED_1,
	ANON_BUT_TYPEDEFED_2,
} x_anonymous_but_typedefed_t;

typedef enum named_and_typedefed {
	NAMED_AND_TYPEDEFED_1,
	NAMED_AND_TYPEDEFED_2,
} x_named_and_typedefed_t;

enum bare_named_enum {
	BARE_NAMED_1,
	BARE_NAMED_2,
};

enum {
	ANON_1,
	ANON_2,
};

typedef enum bare_named_enum type_the_bare_enum_t;


x_named_and_typedefed_t test_named_and_typedefed_through_typedef;
enum named_and_typedefed test_named_and_typedefed_through_enum;