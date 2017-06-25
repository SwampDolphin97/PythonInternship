customer_details = { 1001 : "John", 1004 : "Jill", 1005: "Joe", 1003 : "Jack" }

#1
print customer_details
#2
print len(customer_details)
#3
sortedCustomerNames = sorted(customer_details.values())
print sortedCustomerNames
#4
del customer_details[1005]
print customer_details
#5
customer_details[1003]="Mary"
print customer_details
#6
flag = 0
for key in customer_details:
	if(key==1002):
		flag=1
if(flag==1):
	print "Exists!"
else:
	print"Doesn't Exists"
