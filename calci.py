x=int(input("enter the first number:"))
y=int(input("enter the second number:"))
m=int(input("1.add \n 2.sub \n 3.multi \n 4.div /n 5.power:"))
if m==1:
  print("1",x+y)
elif m==2:
  print("2",x-y)
elif m==3:
  print("3",x*y)
elif m==4:
  print("4",x/y)
elif m==5:
  print("5",x**y)
else:
  print("invalid")
 
