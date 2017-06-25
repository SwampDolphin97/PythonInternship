def sumOfNaturalNumbers(x):
	res = 0	
	for count in range(0,x+1,1):
		res = res+count
	print res
	return

num = int(input("Enter a number:"))
sumOfNaturalNumbers(num)

	
