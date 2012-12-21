#this program is not ideally suited to change the divisor variable into an array of indexed primes, use nextprime.py instead
print "find the sum of all prime numbers below two million"
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
number =3 #this number must stay three, do not change or all the +2 counters will skip odd numbers and check even numbers 
summation = 2 
stop = 2000000
while number < stop:
	number = nextprime(number) 
	if number<stop: 
		print number 
		summation = summation + number 
	number= number +2 #skips even numbers 
	continue 
print summation 
