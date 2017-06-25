num = int(input("Enter number:"))
sum2 = 1
sum1 = 1
print sum1
print sum2
for count in range(0,num-2,1):
	res = sum1 + sum2
	print res
	sum2 = sum1
	sum1 = res
