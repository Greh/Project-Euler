#nested for loops a, b. c defined by a, b in for loops. if statement 
print "find the product of the pythagorean triple that adds up to 1000"
from math import sqrt 
for i in range (999):
	a=i 
	for j in range (999):
		b=j
		c=sqrt((a*a)+(b*b))
		if a+b+c==1000 and a<b and b<c:
			print a*b*c
