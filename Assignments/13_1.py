bill = int(input("Enter bill:"))
if (bill>=1000):
	amount = bill + (bill*5/100)
elif (bill>=500 and bill>1000):
	amount  = bill - bill*.02
else:
	amount = bill - bill*.01

print "Bill:",amount
