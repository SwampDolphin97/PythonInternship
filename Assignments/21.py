listProducts = ["Sofa Set","Dining Table","T.V. Stand","Cupboard"]
listCosts = [20000,8500,4,599,13920]
Counter = int(input("How many Sofa Set you want to purchase"))
Bill = Counter*listCosts[0]
print listProducts[0]
Counter = int(input("How many Dining Table you want to purchase"))
print listProducts[1]
Bill += Counter*listCosts[1]
Counter = int(input("How many T.V Stand you want to purchase"))
print listProducts[1]
Bill += Counter*listCosts[2]
Counter = int(input("How many Cupboard you want to purchase"))
print listProducts[2]
Bill += Counter*listCosts[3]
print "Bill:",Bill

