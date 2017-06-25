import module2
def is_prime(x):
	flag = 0
	for count in range(2,x,1):
		if(x%count == 0):
			flag = 1
	if(flag == 0):
		print "Number is prime"
	else:
		print "Number is not prime"
def is_even(x):
	if(x%2==0):
		print "Even"
	else:
		print "Not Even"
