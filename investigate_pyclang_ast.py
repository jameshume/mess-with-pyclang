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

	indent_str="|   " * level

	for cur in children:
		#print(" " * (level * 4), ">>> NODE: obj=", cur, "type=", cur.type, "kind =", "n/a" if cur.kind is None else cur.kind, "spel = '{}' (len={})".format(cur.spelling, len(cur.spelling)))
		print("{}+-- NODE: ".format(indent_str), "n/a" if cur.kind is None else cur.kind, "spel = '{}' (len={})".format(cur.spelling, len(cur.spelling)))
		if cur.kind == clang.cindex.CursorKind.INTEGER_LITERAL:
			#print(" " * (level * 4), "  - tokens:", [a.spelling for a in cur.get_tokens()])
			print("{}|       : tokens:".format(indent_str), [a.spelling for a in cur.get_tokens()])
		elif cur.kind == clang.cindex.CursorKind.BINARY_OPERATOR:
			print("{}|       : tokens:".format(indent_str), [a.spelling for a in cur.get_tokens()])
			# Damin it!!!! CCant get ops
		elif cur.kind == clang.cindex.CursorKind.VAR_DECL:
			print("{}|       : type:".format(indent_str), cur.type, "=", cur.type.spelling, "| const?:", cur.type.is_const_qualified() , ", pod?:", cur.type.is_pod(), ", volatile?:", cur.type.is_volatile_qualified())
		elif cur.kind == clang.cindex.CursorKind.TYPEDEF_DECL:
			print("{}|       : referenced".format(indent_str), cur.referenced, cur.referenced.spelling)
			print("{}|       : type.spelling:".format(indent_str), cur.type.spelling)
			print("{}|       : spelling:".format(indent_str), cur.spelling)
			#vvv Did not work with sealang - more up to date libclang or sealang not up to date with pyclang??
			#print(" " * (level * 4), "  - typedef_name:", cur.type.get_typedef_name())
			print("{}|       : underlying_typedef_type".format(indent_str), cur.underlying_typedef_type.spelling)
		elif cur.kind == clang.cindex.CursorKind.DECL_REF_EXPR:
			print("{}|       : type".format(indent_str), cur.type)
			print("{}|       : type".format(indent_str), cur.type.spelling)
			print("{}|       : referenced type".format(indent_str), cur.referenced.type.spelling)
		elif cur.kind == clang.cindex.CursorKind.ENUM_CONSTANT_DECL:
			print("{}|       : type".format(indent_str), cur.type.spelling)
			print("{}|       : enum_value".format(indent_str), cur.enum_value)
			print("{}|       : parents".format(indent_str), cur.lexical_parent.type.spelling, cur.semantic_parent.type.spelling,  cur.semantic_parent.kind)
			print("{}|       : parents obj eq".format(indent_str), prev_enum_decl == cur.lexical_parent, prev_enum_decl == cur.semantic_parent)
		elif cur.kind == clang.cindex. CursorKind.ENUM_DECL:
			prev_enum_decl = cur
			print("{}|       : referenced".format(indent_str), cur.referenced, cur.referenced.spelling)
			print("{}|       : type name".format(indent_str), cur.type.spelling)
			print("{}|       : type kind".format(indent_str), cur.type.kind)
			print("{}|       : is_anonymous".format(indent_str), cur.is_anonymous())
			print("{}|       : parents".format(indent_str), cur.lexical_parent.spelling, cur.semantic_parent.spelling)
			print("{}|       : enum_type".format(indent_str), cur.enum_type, cur.enum_type.spelling)

		tree(cur.get_children(), level + 1)

tree(tu.cursor.get_children(), 0)