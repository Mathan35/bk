while True:
	print("Enter '0' for exit.")
	ch = input("Enter any character: ")
	if ch == '0':
		break
	else:
		if(ch>='a' and ch<='z'):
			print(ch, "is an alphabet.\n")
		else:
			print(ch, "is not an alphabet.\n")
