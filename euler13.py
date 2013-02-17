print "project euler problem 12: work out the first ten digits of the sum of the following one hundred 50-digit numbers" 
total=0
filez= open("problem13.txt", "r") 
for n in filez: 	
	print n 
	total=total+int(n)
print total
