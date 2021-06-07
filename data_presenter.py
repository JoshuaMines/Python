open_file = open('CupcakeInvoices.csv')

# for row in open_file:
#     print(row)

# for row in open_file:
#     values = row.split(',')
#     print (values[2])

# for value in open_file:
#     value = float(open_file[4])
#     print (value)

total_invoices = 0
for row in open_file:
    values = row.split(',')
    total_invoices = total_invoices + int(values[3]) * float(values[4])
print (total_invoices)

open.file.close