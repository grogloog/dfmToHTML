from pyparsing import nestedExpr
import json

def get_tree(l):
	i = 0
	tmp_tree = {}
	while i < len(l):
		if not isinstance(l[i], list):
			tmp_tree[l[i]] = l[i + 1]
			i = i + 2
		else:
			tmp_tree['HasChild'] = True
			tmp_tree[l[i][0]] = {"Name": l[i][0], "Type": l[i][1]}
			if len(l[i][2:]) != 0:
				tmp_tree[l[i][0]].update(get_tree(l[i][2:]))
				i = i + 1
	return tmp_tree

			

def main():
	with open("TApcASP4ReaderWrapCtrlTZ.dfm") as dfm:
		data="".join(line.rstrip() for line in dfm)

	data = data.replace(' = ', ' ')
	data = data.replace(':', '')

	nested_items = nestedExpr("object", "end")
	elems_nested_list = nested_items.parseString(data).asList()[0]

	tree = get_tree(elems_nested_list)

	json_tree = json.dumps(tree, indent = 4)

	print(json_tree)

if __name__ == "__main__":
	main()
