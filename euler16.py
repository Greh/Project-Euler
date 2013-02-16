print "project euler 16: add up the digits of 2^1000"  
a=(2**1000)
b=str(a)  
d=0 
for i in b: 
	d=d+int(i) 
print d 
