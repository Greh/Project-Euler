#!/usr/bin/env python 3.1
from math import sqrt 
def nextprime(number): 
	"This function will find the smallest prime larger than the current number"
	potential= number
	j=2
	while j<potential:
	        if potential%j:
			j=j+1
		else:
			#print "not prime"
			potential=potential +1
			j=2
			continue
	#print potential
	return potential 
print ("project euler problem 7: what is the 10001st prime number?")
number =2
for i in range (10001):
	number = nextprime(number) 
	#print (number)
	number = number +1
	continue 
#number = nextprime(number)	
number = number -1 
print number
