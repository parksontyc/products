import os #operating system

def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品, 價格\n' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	return products

def user_input(products):
	while True:
		name = input('請輸入商品名稱：')
		if name == 'q':
			break
		price = input('請輸入價格：')
		price = int(price)
		products.append([name, price])
	print(products)
	return products

def print_products(products):
	for i in products:
		print(i[0], '的價格是', i[1])

def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('商品, 價格\n')
		for i in products:
			f.write(i[0] + ',' + str(i[1]) + '\n')

def main():
	filename = 'products.csv'
	products = []
	if os.path.isfile(filename):
		print('有檔案')
		products = read_file(filename)
	else:
		print('沒有檔案')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)


main()