print "make a factorial using recursion" 

def factorial(n): 
	if n==1: 
		return 1
	else:
		return n*int(factorial(n-1))

start=int(raw_input("enter an integer and press enter ")) 
end=factorial(start)
print end 
