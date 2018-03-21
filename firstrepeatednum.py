l = [1,2,1,3,2,5]
found = 0
for i in range (0 , 6):
    item = abs(l[i])
    if(l[item - 1] > 0):
        l[item - 1] = -1 * l[item - 1]
    else:
        found = abs(l[i])
        break    
print (found)
