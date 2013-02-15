print "project euler problem 14: find the longest collatz sequence starting under 1 million" 
# everything between here 
memo= { }
def collatz_step(x):
	global memo 
	if x==1:
		return 0
	if x in memo:
		return memo[x]
	if x%2==0:
		memo[x]=collatz_step(x/2)+1 
	else: 
		memo[x]=collatz_step(3*x +1) +1 
	return memo[x] 
#and here is pseudo code that Bart helped me write 
start=int(raw_input('enter an integer and press enter '))

length=collatz_step(start)
print length 







