num = input("Enter number:")
sum1 = 0
sum2 = 1
res = 0
list = []
list.append(str(sum1))
list.append(str(sum2))
for count in range(2,num,1):
	res = sum1 + sum2
	sum1 = sum2
	sum2 = res
	list.append(str(res))
print list
