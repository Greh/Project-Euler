#!/usr/bin/env python 3.1
from math import sqrt 
def nextprime(number): 
	"This function will find the smallest prime larger than the current number"
	potential= number
	j=3
	while j<=sqrt(potential):
	        if potential%j:
			#print "j", j #for debugging
			j=j+2 #note: it is trying to divide potential by all odd numbers but necessarily primes, so its catching all the non primes as quickly as possible but taking longer than necessary on the primes
		else:
			#print "j", j #for debugging
			#print potential, "not prime" #for debugging  
			potential=potential +2 #skips even numbers  
			j=3
			continue
	#print potential #for debugging 
	return potential 
print ("project euler problem 7: what is the 10001st prime number?")
number =3
for i in range (1, 10001):
	number = nextprime(number) 
	print (number)
	number = number +2
	continue 
#number = nextprime(number)	
