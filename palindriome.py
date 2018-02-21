 name ='mathan'
name = name.casefold()
rev_str = reversed(name)
if list(name) == list(rev_str):
   print("It is palindrome")
else:
   print("It is not palindrome")
