def fibonacci(x):
	sum1 = 0
	sum2 = 1
	print sum1
	print sum2
	for count in range(2,x,1):
		res = sum1 + sum2
		sum1 = sum2
		sum2 = res
		print res
	return

num = int(input("Enter a number:"))
fibonacci(num)

