open_file = open("CupcakeInvoices.csv")

for row in open_file:
    print(row)
    
for row in open_file:
    items = row.split(',')
    print('Cupcake type is: ', items[2])

for row in open_file:
    items = row.split(',')
    total = float(items[3]) * float(items[4])
    total = round(total)
    print('Order total is: ', total)

total_all = 0
for row in open_file:
    items = row.split(',')
    total = float(items[3]) * float(items[4])
    total = round(total)
    total_all += total
print('Total for all orders is: ', total_all)

open_file.close()
    
    