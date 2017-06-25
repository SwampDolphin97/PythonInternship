str = raw_input("Enter String:")
num = 1
resstr = ""
for index,count in enumerate(str):
	if(count==" "):
		continue
	num += 1
	if (num%2==0):
		resstr += count

print "Resultant String:",resstr
print "Expected Output:",resstr[::-1]
