lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
print("Maximum num is :", max(lst), "\nMinimum num is :", min(lst))  
