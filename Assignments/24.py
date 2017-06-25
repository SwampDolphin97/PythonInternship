#HaveToFix
stu = { "John" : 86.5 , "Jack" : 91.2 , "Jill" : 84.5 , "Harry" : 72.1 , "Joe" : 80.5 }
#1
print stu
#2
from collections import OrderedDict
sortedstu = sorted(stu.items())
print sortedstu
#3
total = 0
for key,value in stu.items():
	total += value
total = total/5
print "Average:",total
