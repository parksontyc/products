
products = []
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入價格：')
	p = []
	p.append(name)
	p.append(price)   #p = [name, price]
	products.append(p)
print(products)

print(products[0][0])

for i in products:
	print(i)

with open('products.txt', 'w') as f:
	for i in products:
		f.write(i[0] + ',' + i[1] + '\n')