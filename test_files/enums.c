enum {
	ANON_ENUM_1,
	ANON_ENUM_2,
	ANON_ENUM_3
};

enum Bare_Named_Enum {
	BARE_NAMED_ENUM_1,
	BARE_NAMED_ENUM_2,
	BARE_NAMED_ENUM_3
};

typedef enum {
	TYPEDEF_ANON_ENUM_1,
	TYPEDEF_ANON_ENUM_2,
	TYPEDEF_ANON_ENUM_3
} Typedef_Anonymouse_Enum_t;

typedef enum Typdef_Named_enum {
	TYPEDEF_NAMED_ENUM_1,
	TYPEDEF_NAMED_ENUM_2,
	TYPEDEF_NAMED_ENUM_3
} Typedef_Named_Enum_t;

struct thestruct
{
	enum enum_in_struct
	{
		ENUM_IN_STRUCT_1, ENUM_IN_STRUCT_2
	} val;
};

void func(void)
{
	typedef enum enum_in_func {
		E_IN_FUNC_1,
		E_IN_FUNC_2
	} Enum_In_Func_t;
}