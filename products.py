
products = []

with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		if '商品，價格' in line:
			continue
		name, price = line.strip().split(',')
		products.append([name, price])
print(products)


while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入價格：')
	price = int(price)
	p = []
	p.append(name)
	p.append(price)   #p = [name, price]
	products.append(p)
print(products)

print(products[0][0])

for i in products:
	print(i)

with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品, 價格\n')
	for i in products:
		f.write(i[0] + ',' + str(i[1]) + '\n')