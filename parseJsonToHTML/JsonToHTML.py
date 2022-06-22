import json

elems = {
	'row': '<div class="two-col-grid grouped-items">*elem_inner*</div>',
	'TPanel': '<div class="pnlExport">\n*elem_inner*</div>',
	'TLabel': '<div>*elem_caption*: TLabel</div>\n',
	'TCheckBox': '<div>*elem_name*: TCheckBox</div><div>*elem_caption*</div>\n',
	'TComboBox': '<div>*elem_name*: TComboBox</div>\n',
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

def by_top(d):
	return int(d['Top'])

def get_childs(d):
	childs_list = []
	for key, value in d.items():
		if isinstance(value, dict):
			childs_list.append(value)

	return childs_list


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

	childs_list.sort(key=by_top)

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
	f = open('parsed.json')
	elems_tree = json.load(f)['pnlExport']

	print(dict_to_html(elems_tree))

if __name__ == "__main__":
	main()