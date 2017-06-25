def FIBO(number):
	if(number==0):
		return 0
	elif(number == 1):
		return 1
	else:
		return FIBO(number-1) + FIBO(number-2)

num = int(input("Enter a number:"))
res = FIBO(num)
print res
