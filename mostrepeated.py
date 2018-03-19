import collections
s = input("Enter the charecter")
print(collections.Counter(s).most_common(1)[0]) 
