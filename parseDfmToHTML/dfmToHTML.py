from pyparsing import nestedExpr
import json
import sys

elems = {
	'row': '<div class="two-col-grid grouped-items">*elem_inner*</div>\n',
	'TPanel': '<div class="pnlExport">\n*elem_inner*</div>',
	'TLabel': '<div>*elem_caption*: TLabel</div>\n',
	'TCheckBox': '<div>*elem_name*: TCheckBox</div><div>*elem_caption*</div>\n',
	'TComboBox': '<div>*elem_name*: TComboBox</div>\n',
	'TBevel': '<hr>\n',
	'TRxCalcEdit': '<div>*elem_name*: TRxCalcEdit</div>\n',
	'TGroupBox': {
		'default': '<div class="two-col-grid outlined-grouped-items">\n*elem_inner*</div>',
		'labeled': """
<div class="outlined-grouped-items">
<div class="outlined-grouped-items-header">*elem_caption*</div>
<div class="two-col-grid">
*elem_inner*
</div>
</div>
"""
	}
}

def get_json(l):
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
				tmp_tree[l[i][0]].update(get_json(l[i][2:]))
				i = i + 1
	return tmp_tree

def by_top(d):
	return int(d['Top'])

def align_lines(l):
	levels = [int(l[0]['Top'])]

	for i in range(1, len(l)):
		new_level = True
		for level in levels:
			if abs(level - int(l[i]['Top'])) < 5:
				l[i]['Top'] = str(level)
				new_level = False
				break
		if new_level:
			levels.append(int(l[i]['Top']))

	return l

def get_childs(d):
	childs_list = []
	for key, value in d.items():
		if isinstance(value, dict):
			childs_list.append(value)

	return childs_list

def merge_lines(l):

	new_list = [l[0]]

	last_top = int(l[0]['Top'])

	for i in range(1, len(l)):
		if l[i]['Type'] == 'TCheckBox':
			new_list.append({"Name": "row", "Type": "row", l[i]['Name']: l[i]})
		else:
			current_top = int(l[i]['Top'])
			if abs(last_top - current_top) < 5:
				row_elems = new_list.pop()
				if 'row' not in row_elems:
					row_elems = {"Name": "row", "Type": "row", "Top": current_top, row_elems['Name']: row_elems, l[i]['Name']: l[i]}
				else:
					row_elems.update({l[i]['Name']: l[i]})
				new_list.append(row_elems)
			else:
				last_top = current_top
				new_list.append(l[i])

	return new_list


def dict_to_html(d):
	elem_type = d['Type']
	elem_name = d['Name']

	if elem_type == 'TGroupBox':
		if 'Caption' in d:
			elem_html = elems['TGroupBox']['labeled']
		else:
			elem_html = elems['TGroupBox']['default']
	else:
		elem_html = str(elems[elem_type])

	inner_html = ''

	childs_list = get_childs(d)

	if len(childs_list) > 1:
		childs_list = align_lines(childs_list)

	childs_list.sort(key=by_top)

	if d['Name'] != 'row' and d['Type'] != 'TGroupBox' and len(childs_list) != 0:
		childs_list = merge_lines(childs_list)

	if isinstance(childs_list, list):
		for child in childs_list:
			inner_html = inner_html + dict_to_html(child)

	if '*elem_inner*' in elem_html:
		elem_html = elem_html.replace('*elem_inner*', inner_html)

	if '*elem_caption*' in elem_html:
		elem_html = elem_html.replace('*elem_caption*', d['Caption'].replace("'", ''))

	if '*elem_name*' in elem_html:
		elem_html = elem_html.replace('*elem_name*', elem_name)

	return elem_html

def main():
	elems_tree = {}

	inputfile = sys.argv[1]
	jsonfile = inputfile.replace('.dfm', '.json')
	outputfile = inputfile.replace('.dfm', '.html')

	with open(inputfile) as dfm:
		dfm_text="".join(line.rstrip() for line in dfm)

	# Обработка dfm

	dfm_text = dfm_text.replace(' = ', ' ')
	dfm_text = dfm_text.replace(':', '')

	nested_items = nestedExpr("object", "end")
	elems_nested_list = nested_items.parseString(dfm_text).asList()[0]

	elems_tree = get_json(elems_nested_list)

	json_tree = json.dumps(elems_tree, indent = 4)

	with open(jsonfile, 'w') as f:
		sys.stdout = f
		print(json_tree)

	inp = open(inputfile)

	pnl_export = elems_tree['pnlExport']

	with open(outputfile, 'w') as outp:
		sys.stdout = outp
		print(dict_to_html(pnl_export))

if __name__ == "__main__":
	main()