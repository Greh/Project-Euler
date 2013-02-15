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
longest=0
winner=0
for i in range (1, 1000000):
	length=collatz_step(i)
	if length>longest: 
		winner= i 
		longest=length
		print winner 
print winner 

#plan: shove the function in a for loop which also checks if its the largest and print it at the end 








