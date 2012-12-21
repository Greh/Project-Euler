print ("project euler 6")
summation=0
sumsquare=0
for i in range (101):
	summation= summation +i
	print ("summation", summation) 
squaresum= summation**2
print ("squaresum", squaresum) 
for j in range (101): 
	sumsquare= (sumsquare + (j**2))
	print ("sumsquare", sumsquare)
total = squaresum - sumsquare
print (total) 
