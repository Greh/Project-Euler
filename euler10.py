print "find the sum of all prime numbers below two million"

total=0 
print "seive of eratosthenes"
end=raw_input("find all the primes below... ") 
bucket = [];
for i in range(0,int(end)):
    bucket.append(0);
#print bucket
j=2
while j**2<=int(end): 
	for i in range(j+j, len(bucket), j): 
		bucket[i]=1
	#print bucket
	j=j+1
bucket[0]=1
bucket[1]=1
for i in range(len(bucket)):
	if bucket[i]==0:
		total=total+i 
		print total 
	
