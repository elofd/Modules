site = {
	'html': {
		'head': {
			'title': 'Мой сайт'
		},
		'body': {
			'h2': 'Здесь будет мой заголовок',
			'div': 'Тут, наверное, какой-то блок',
			'p': 'А вот здесь новый абзац'
		}
	}
}
def seach(dct, key, depth):
	if key in dct.keys():
		return dct[key]
	find_key = None
	if depth > 1 or depth <= 0:
		for item in dct.values():
			if isinstance(item, dict):
				find_key = seach(item, key, depth-1)
	return find_key

my_key = input('Введите искомый ключ: ')
my_depth = 0
if input('Хотите ввести максимальную глубину? Y/N: ') == 'y':
	my_depth = int(input('Введите максимальную глубину: '))
print(seach(site, my_key, my_depth))
