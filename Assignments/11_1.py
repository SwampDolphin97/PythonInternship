#Initialization
a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))

print("Before Swapping")
print("Number1:",a,"Number2:",b)

#Logic
a = a + b
b = a - b
a = a - b

#Output
print("After Swapping")
print("Number1:",a,"Number2:",b)