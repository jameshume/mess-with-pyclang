import clang.cindex
import sys

index = clang.cindex.Index.create()
tu = index.parse('test_files/test1.c')
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

def tree(children, level):
	for cur in children:
		print(" " * (level * 4), "kind =", "n/a" if cur.kind is None else cur.kind, "spel =", cur.spelling)
		if cur.kind == clang.cindex.CursorKind.INTEGER_LITERAL:
			print(" " * (level * 4), "  - tokens:", [a.spelling for a in cur.get_tokens()])
		elif cur.kind == clang.cindex.CursorKind.BINARY_OPERATOR:
			print(" " * (level * 4), "  - tokens:", [a.spelling for a in cur.get_tokens()])
		elif cur.kind == clang.cindex.CursorKind.VAR_DECL:
			print(" " * (level * 4), "  - type:", cur.type, "=", cur.type.spelling, "| const?:", cur.type.is_const_qualified() , ", pod?:", cur.type.is_pod(), ", volatile?:", cur.type.is_volatile_qualified())
		elif cur.kind == clang.cindex.CursorKind.TYPEDEF_DECL:
			print(" " * (level * 4), "  - spelling:", cur.spelling)
			print(" " * (level * 4), "  - type.spelling:", cur.type.spelling)
			print(" " * (level * 4), "  - typedef_name:", cur.type.get_typedef_name())
			print(" " * (level * 4), "  - underlying_typedef_type", cur.underlying_typedef_type.spelling)
		tree(cur.get_children(), level + 1)

tree(tu.cursor.get_children(), 0)