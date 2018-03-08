a = int(input('Please input the first integer:'))
b = int(input('Please input the second integer:'))
while b != 0:
    mat=b
    b = a % b
    a=mat
print(mat) 
