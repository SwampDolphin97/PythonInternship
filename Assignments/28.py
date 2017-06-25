def Baggage_check(weight):
	if(weight>=0 and weight<=40):
		return True
	else:
		return False

def Immigration_check(year):
	if(year>=2001 and year<=2025):
		return True
	else:
		return False

def Security_check(status):
	if(status=="valid" or status=="VALID"):
		return True
	else:
		return False
def traveler():
	try:
		traveler_id = int(input("Enter ID:"))
	except NameError:
        	print "Please enter correct input!"
	traveler_name = raw_input("Enter name:")
	try:
		baggage_weight = int(input("Enter baggage weight:"))
	except NameError:
	        print "Please enter correct input!"
	try:
		expiry_date = int(input("Enter expiry date:"))
	except NameError:
	        print "Please enter correct input!"	
	noc_status = raw_input("Enter status:")
	
	a = Baggage_check(baggage_weight)
	b = Immigration_check(expiry_date)
	c =Security_check(noc_status)
	print a,b,c
	if(a & b & c == True):
		print "Allow Traveler to fly"
	else:
		print "ID:",traveler_id,"Name:",traveler_name
		print "Detail for Re-checking"
	return 

traveler()
