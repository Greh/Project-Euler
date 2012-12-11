print ("project Euler problem 2: find the sum of the even valued terms of the fibonacci sequence")
total=1
dunnoyet=2
m=1
n=2 
while total < 4000000: 
	total=m+n
	m= n
	n= total 
	#print ("fibonnaci", total)
	if n%2==0: 
		dunnoyet= dunnoyet + n
		#print ("sum", dunnoyet) 
		continue 
	else: continue
	
print (dunnoyet)

