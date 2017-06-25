str1 = raw_input("Enter String 1:")
str2 = raw_input("Enter String 2:")
strout = ""
for count in str1:
	if(count.isupper()):
		strout += count

for count in str2:
	if count.isupper():
		strout += count
print strout
