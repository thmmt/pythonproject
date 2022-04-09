print("1 : mohasebat shamel * / + - ^")
print("2 : entekhab n, r")
a = int(input())
if(a == 1) : 
	s = input()
	c = s[1]
	for i in range len(3, s + 1):
		i = i + 1
		if(s[i] == '+') : c = c + ord(s[i - 1])
		elif(s[i] == '-') : c = c - ord(s[i - 1])
		elif(s[i] == '*') : c = c * ord(s[i - 1])
		elif(s[i] == '/') : c = c / ord(s[i - 1])
		elif(s[i] == '^') : c = c ** ord(s[i - 1])

# pythonproject
