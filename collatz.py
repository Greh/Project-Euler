print "project euler problem 14: find the longest collatz sequence starting under 1 million"  
def sequence(start): 
	#so this function takes the variable named "start" and prints out the collatz sequence that results from it
	n=start 
	while n>1:
		if n%2: 
			n=3*n+1
			print n 
		else: 
			n=n/2 
			print n 
	return end
start=int(raw_input('type an integer and press enter ')) 
print start 
end=0 
end=sequence(start)
print end 








