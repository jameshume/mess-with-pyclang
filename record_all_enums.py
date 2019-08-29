import clang.cindex
import sys

index = clang.cindex.Index.create()
tu = index.parse('test_files/test2.c')

"""
The options, of interest at least to me, appear to be
1. A "bare" enum with a name. For example enum bare_named { ... };
   In this case:
      * There is only one enum decl
      * cursor.spelling = "bare_named"
      * cursor.type.spelling = "enum bare_named"
      * cursor.is_anonymous() = False
2. A typedef'ed enum with a name. For example typedef enum named_and_typedefed { ... } type_t;
   In this case:
      * There are two enum decls - one for the enum alone, and one as a child of the typedef. 
      * cursor.spelling = "named_and_typedefed"
      * cursor.type.spelling = "enum named_and_typedefed"
      * cursor.is_anonymous() = False
3. A typedef'ed anonymouse enum. For example typedef enum  { ... } type_t;
   In this case:
      * cursor.spelling = ""
      * cursor.type.spelling = "type_t"
      * cursor.is_anonymous() = False << Presumably because it is referenced by the type created.
4. An anonymous enum. For example enum { ... };
   In this case:
      * cursor.spelling = ""
      * cursor.type.spelling = "name enum (anonymous"
      * cursor.is_anonymous() = True

So, it seems like with typedef'ed anonymous enums we need to be able to cope with the definnition
twice.

Must relate typedef's to enum types. Where enum is typedef'ed anon then relate typedef's to enum-named-as-typedef
"""

enum_defs = {}
for cur in tu.cursor.walk_preorder():
	if cur.kind == clang.cindex.CursorKind.ENUM_DECL:
		enum_name = cur.spelling
		if cur.is_anonymous():
			# We will ignore anonymous enums
			continue

		if len(enum_name) == 0:
			# We must be encased in a typedef. Our typename is that of the
			# the typedef enclosing us
			enum_name = cur.type.spelling
