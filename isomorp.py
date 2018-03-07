MAX_CHARS = 256 

 
def isomorphic(string1, string2):
	m = len(string1)
	n = len(string2)

 
	if m != n:
		return "Not isomorphic."

 
	marked = [False] * MAX_CHARS

 
	map = [-1] * MAX_CHARS

 
	for i in range(n):

	 
		if map[ord(string1[i])] == -1:
 
		 
			if marked[ord(string2[i])] == True:
				return "Not isomorphic."

		 
			marked[ord(string2[i])] = True

		 
			map[ord(string1[i])] = string2[i]

	 
		elif map[ord(string1[i])] != string2[i]:
			return "Not isomorphic."

	return True
print (isomorphic("1232","2342")) 
