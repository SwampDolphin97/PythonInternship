#Initialization
numberOfHours = int(input("Enter number of hours in a week:"))
payRate = int(input("Enter pay rate:"))
noOfWeeks = int(input("Enter no of weeks in a month:"))

#Logic
monthlyPay = numberOfHours * payRate * noOfWeeks

#Output
print("Monthly Pay:",monthlyPay)