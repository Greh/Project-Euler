print "Project Eueler 36, sum of all the numbers that are binary in base 10 and base 2" 

def ipalindrome(x): 
	thing=str(x)
	gniht=thing[::-1] 
	if thing==gniht:
		return 1 
	else: 
		return 0 
total=0 
i=1 
while i<1000000: 
	isit=ipalindrome(i)
	if isit==1:
		print "passed first check", i 
		b=bin(i)+"b0"
		print b 
		isitalso=ipalindrome(b) 
		if isitalso==1: 
			print "passed second check", b 
			total=total+i
	i=i+1
print total 
