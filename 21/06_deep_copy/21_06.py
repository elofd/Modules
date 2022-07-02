def sample(n):
	site_lst = []
	for i in range(n):
		product = input('Введите название продукта для нового сайта: ')
		site = {
			'html': {
				'head': {
					'title': 'Куплю/продам {0} недорого'.format(product)
				},
				'body': {
					'h2': 'У нас самая низкая цена на {0}'.format(product),
					'div': 'Купить',
					'p': 'Продать'
				}
			}
		}
		site_lst.append(site)
		for item in site_lst:
			print(item)

x = int(input('Сколько сайтов: '))
sample(x)
