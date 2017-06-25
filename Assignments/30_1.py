def mult3(n):
    if n == 1:
        return 3
    else:
        return mult3(n-1) + 3

n = int(input("Enter value of N:"))
for i in range(1,n+1):
    print(mult3(i))

