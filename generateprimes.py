#!/usr/bin/env python 3.1
#doesn't work for numbers less than 4 
from math import sqrt 
def nextprime(number): 
	"This function will find the smallest prime larger than the current number"
	potential= number
	j=2
	while j<=sqrt(potential):
        	if potential%j:
			j=j+1
		else:
			#print "not prime"
			potential=potential +1
			j=2
			continue
	#print potential
	return potential 
number =4  
rawstop = raw_input('I want to find all the prime numbers below ')
stop = int(rawstop)
print 2
print 3
while number < stop:
	number = nextprime(number) 
	if number<stop: 
		print number  
	number= number +1 #would changing the one to a two allow me to skip testing even numbers? yes, now its faster 
	continue 
	number = nextprime(number)
print "done"
