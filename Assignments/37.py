try:
	num = int(input("Enter a number:"))
except NameError:
	print "Please enter correct input!"
res = 0
for count in range(0,num+1,1):
	res = res+count
print res
