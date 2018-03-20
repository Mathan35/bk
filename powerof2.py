n=int(input("Enter the num:"))
if n > 0 and (n & (n - 1)) == 0:
  print("it is power of 2",n)
else:
    print("it is not a power of 2",n)
 
  
