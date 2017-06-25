num = int(input("Enter a number:"))
flag = 0
for count in range(2,num,1):
	if(num%count==0):
		flag = 1

if (flag == 1):
	print "Not a Prime number"
else:
	print "Prime number"
