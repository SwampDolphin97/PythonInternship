Products = { "Sofa" : 20000 , "Dining Table" : 8500 , "T.V Stand" : 4599 , "Cupboard" : 13920 }
print Products
name = raw_input("Enter Product name:")
qty = int(input("Enter Quantity:"))
for key,rate in Products.items():
    if (name == key):
        rate = Products[key]
	print rate*qty


