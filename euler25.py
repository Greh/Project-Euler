print "what is the first term in the fibonacci sequence to contain 1000 digits?"
total=1
m=1
n=2
i=3
while (len(str(total))-1000)<0: 
	total=m+n
	m=n
	n=total
	i=i+1
	print i

