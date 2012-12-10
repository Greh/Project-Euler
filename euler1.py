print ("Project Euler problem 1: find the sum of all multiples of 5 or 3 below 1000") 
buffer = 0 
for i in range(1000):
	if i%3==0 or i%5==0:  
		buffer = buffer + i 
		continue 
print (buffer)
