lower=int(input("Enter the limit1:"))
upper=int(input("Enter the limit2:"))
for i in range(lower,upper+1):
    if(i%2!=0):
        print(i)
