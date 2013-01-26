print "project euler problem 12: what is the value of the first triangle number to have over 500 divisors" 
from math import sqrt 
triangle=0 
def findtriangle(j): 
	"this function calculates the jth triangle number and prints it"
	number= 0 
	for n in range(1,j+1): 
		number=number+n
	return number 
def findfactors(triangle): 
	#this function calculates how many factors the triangle number has and returns that number 
	factor =0 
	n=1 
	while n<(sqrt(triangle)+1): #TEST WHAT THE HIGHEST DENOMINATOR THAT WORKS FOR THIS IS 
		#mod
		if triangle%n: #triangle number isn't divisible by the factor 
			n=n+1
		else: # it is divisible by factor 	
			#print n
			factor=factor+2 
			n=n+1
	return factor 

j = 1 #counter starts at 1 
factors=1 
mostfactors=1 
while factors<=509: #this while print j and the jth triangle number 
	triangle=findtriangle(j) 
	#print "the ", j, "th triangle number is ", triangle
	factors=findfactors(triangle) 
	#print "and it has ", factors, "factors" 
	if factors>mostfactors: 
		print "the ", j, "th triangle number is ", triangle, " it has ", factors, " factors" 
		mostfactors=factors 
	j=j+1 
print triangle 







