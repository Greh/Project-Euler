print ("project euler problem 3 find the largest prime factor of 600851475143") 
divisor=3
total=600851475143
while divisor<total: 
	if total%divisor == 0:
		total= total/divisor
		#print (divisor)
		continue 
	divisor = divisor +1 
	continue 
print (total)

