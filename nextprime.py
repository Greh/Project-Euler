#!/usr/bin/env python 3.1
#doesn't work for numbers less than 4
from math import sqrt 
def nextprime(number): 
	"This function will find the smallest prime larger than the current number"
	potential=number
	j=2
	while j<=sqrt(potential): 
	        if potential%j: #not divisible by j 
			#print "j", j #for debugging 
			j=j+1
		else: #divisible by j 
			#print "j", j #for debugging 
			#print potential, "is not prime" #for debugging 
			potential=potential +1 #could I change this to make it skip even numbers? 
			j=2
			continue
	#print potential, "is prime" #for debugging 
	return potential
a= raw_input('Pick a number ') 
#int(a) #for debugging 
number = int(a)
number = nextprime(number)
print "the next prime number is ", number 
