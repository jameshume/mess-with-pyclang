import clang.cindex
import sys

index = clang.cindex.Index.create()
tu = index.parse('test_files/test2.c')
print(type(tu),":")
print(dir(tu))
print("\n\n")
print(type(tu.cursor),":")
print(dir(tu.cursor))
print("\n\n")
print(tu.cursor.get_children())
print("\n\n")
for a in tu.cursor.get_children():
   print(a)
print("\n\n")
print(tu.cursor.walk_preorder())
print(next(tu.cursor.walk_preorder()))

print('-'*80)
for cur in tu.cursor.walk_preorder():
	print(cur.kind, cur.spelling)
	if cur.kind == clang.cindex.CursorKind.TYPEDEF_DECL:
		print("  - spelling:", cur.spelling)
		print("  - type.spelling:", cur.type.spelling)
		print("  - underlying_typedef_type", cur.underlying_typedef_type.spelling)

print('-'*80)

prev_enum_decl = None

def tree(children, level):
	global prev_enum_decl
	for cur in children:
		if cur.kind == clang.cindex. CursorKind.ENUM_DECL:
			print("\n\n")
		print(">" * (level * 4), "NODE: obj=", cur, "type=", cur.type, "kind =", "n/a" if cur.kind is None else cur.kind, "spel =", cur.spelling, len(cur.spelling))
		if cur.kind == clang.cindex.CursorKind.INTEGER_LITERAL:
			print(" " * (level * 4), "  - tokens:", [a.spelling for a in cur.get_tokens()])
		elif cur.kind == clang.cindex.CursorKind.BINARY_OPERATOR:
			print(" " * (level * 4), "  - tokens:", [a.spelling for a in cur.get_tokens()])
		elif cur.kind == clang.cindex.CursorKind.VAR_DECL:
			print(" " * (level * 4), "  - type:", cur.type, "=", cur.type.spelling, "| const?:", cur.type.is_const_qualified() , ", pod?:", cur.type.is_pod(), ", volatile?:", cur.type.is_volatile_qualified())
		elif cur.kind == clang.cindex.CursorKind.TYPEDEF_DECL:
			print(" " * (level * 4), "  - referenced", cur.referenced, cur.referenced.spelling)
			print(" " * (level * 4), "  - spelling:", cur.spelling)
			print(" " * (level * 4), "  - type.spelling:", cur.type.spelling)
			print(" " * (level * 4), "  - typedef_name:", cur.type.get_typedef_name())
			print(" " * (level * 4), "  - underlying_typedef_type", cur.underlying_typedef_type.spelling)
		elif cur.kind == clang.cindex.CursorKind.DECL_REF_EXPR:
			print(" " * (level * 4), "  - type", cur.type)
			print(" " * (level * 4), "  - type", cur.type.spelling)
			print(" " * (level * 4), "  - referenced type", cur.referenced.type.spelling)
		elif cur.kind == clang.cindex.CursorKind.ENUM_CONSTANT_DECL:
			print(" " * (level * 4), "  - type", cur.type.spelling)
			print(" " * (level * 4), "  - enum_value", cur.enum_value)
			print(" " * (level * 4), "  - parents", cur.lexical_parent.type.spelling, cur.semantic_parent.type.spelling,  cur.semantic_parent.kind)
			print(" " * (level * 4), "  - parents obj eq", prev_enum_decl == cur.lexical_parent, prev_enum_decl == cur.semantic_parent)
		elif cur.kind == clang.cindex. CursorKind.ENUM_DECL:
			prev_enum_decl = cur
			print(" " * (level * 4), "  - referenced", cur.referenced, cur.referenced.spelling)
			print(" " * (level * 4), "  - type name", cur.type.spelling)
			print(" " * (level * 4), "  - type kind", cur.type.kind)
			print(" " * (level * 4), "  - is_anonymous", cur.is_anonymous())
			print(" " * (level * 4), "  - parents", cur.lexical_parent.spelling, cur.semantic_parent.spelling)
			print(" " * (level * 4), "  - enum_type", cur.enum_type, cur.enum_type.spelling)

		tree(cur.get_children(), level + 1)

tree(tu.cursor.get_children(), 0)