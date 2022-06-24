from pyparsing import nestedExpr
import json
import sys
import codecs

elems = {
	'row': '<div class="two-col-grid grouped-items">*elem_inner*</div>\n',
	'TPanel': '<div class="pnlExport">\n*elem_inner*</div>',
	'TLabel': '<div>*elem_caption*: TLabel</div>\n',
	'TCheckBox': '<div>*elem_name*: TCheckBox</div><div>*elem_caption*</div>\n',
	'TComboBox': '<div>*elem_name*: TComboBox</div>\n',
	'TButton': '<div>*elem_name*: TButton</div>\n',
	'TDateTimePicker': '<div>*elem_name*: TDateTimePicker</div>\n',
	'TEdit': '<div>*elem_name*: TEdit</div>\n',
	'TBitBtn': '<div>*elem_name*: TBitBtn</div>\n',
	'TRxSpinEdit': '<div>*elem_name*: TRxSpinEdit</div>\n',
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

# Заменяет коды utf-8 символов в dfm на сами символы
def replace_utf8(s):
	while '#' in s:
		code_pos = s.find('#')
		code = s[code_pos:code_pos + 5]
		s = s.replace(code, chr(int(code[1:])))
	return s

# Переделывает структуру из вложенных списков в структуру из вложенных словарей
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

# Для сортировки
def by_top(d):
	return int(d['Top'])

# Элементам, которые находятся в одной строке, но имеют разное значение Top присваивает одинаковое значение Top
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

# Возвращает список вложенных словарей-элементов родительского словаря
def get_childs(d):
	childs_list = []
	for key, value in d.items():
		if isinstance(value, dict):
			childs_list.append(value)

	return childs_list

# Оборачивает элементы с одинаковым top в элемент-строку
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

# Преобразовывает дерево элементов(структуру из вложенных словарей) в HTML код
def dict_to_html(d):
	elem_type = d['Type']
	elem_name = d['Name']

	if elem_type == 'TGroupBox' or elem_type == 'TRadioGroup':
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

	dfm_text = ''
	with open(inputfile) as dfm:
		for line in dfm:
			if 'Anchors' not in line and 'DesignSize' not in line and ('=' in line or 'object' in line or 'end' in line):
				if 'Caption = ' in line or 'Text = ' in line:
					line = replace_utf8(line).replace("'", '').replace(' = ', " = '").replace('\n', "'\n")
					line = line.encode('utf-8').decode('utf-8')
				dfm_text = dfm_text + line

	# Обработка dfm

	dfm_text = dfm_text.replace(' = ', ' ')
	dfm_text = dfm_text.replace(':', '')

	nested_items = nestedExpr("object", "end")
	elems_nested_list = nested_items.parseString(dfm_text).asList()[0]

	# print(elems_nested_list)

	elems_tree = get_json(elems_nested_list)

	# json_tree = json.dumps(elems_tree, indent = 4, ensure_ascii=False)

	# with codecs.open(jsonfile, 'w', 'utf-8') as f:
	# 	sys.stdout = f
	# 	print(json_tree)

	pnl_export = elems_tree['pnlExport']

	# sys.stdout = sys.__stdout__

	# print(dict_to_html(pnl_export))

	with codecs.open(outputfile, 'w', 'utf-8') as outp:
		sys.stdout = outp
		print(dict_to_html(pnl_export))

if __name__ == "__main__":
	main()