#1
id = raw_input("Enter student ID(Numbers only):")
print id
if( id.isdigit() == True):
	print "Valid"
else:
	print "Not Valid"

#2
name  = raw_input("Enter student name(Alphabets only):")
if(name.isalpha() == True):
	print "Valid"
else:
	print "Not Valid"

#3
fees = input("Enter student fee:")

#4
email = ""
if(id.isdigit()==True and name.isalpha()==True):
	email += name
	email += "@ABC.com"

#5
print "Student_id:",id
print "Student_name:",name
print "Fees amount:",round(fees,2)
print "Email:",email
