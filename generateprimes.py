#!/usr/bin/env python 3.1
#doesn't work for numbers less than 4 
from math import sqrt 
def nextprime(number): 
	"This function will find the smallest prime larger than the current number"
	potential= number
	j=3
	while j<=sqrt(potential):
        	if potential%j:
			j=j+2
		else:
			#print "not prime"
			potential=potential +2
			j=3
			continue
	#print potential
	return potential 
number =3
rawstop = raw_input('I want to find all the prime numbers below ')
stop = int(rawstop)
print 2
while number < stop:
	number = nextprime(number) 
	if number<stop: 
		print number  
	number= number +2
	continue 
	number = nextprime(number)
print "done"
