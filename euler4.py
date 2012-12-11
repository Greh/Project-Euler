print ("project euler problem 4: find the largest palindrome made from the product two 3 digit numbers")
number =0  
winner =0
for i in range (999,100, -1): 
	#print (i)
	for j in range (999,100, -1): 
		number= i*j 
		#print (number) 
		thing= str(number)
		gniht= thing[::-1] 
		#print (gniht)
		if thing == gniht: 
			#print "yes", number
			if number>winner: 
				winner=number 
				#print (winner) 
			continue 
		continue 
print (winner)
#thing = "hello" 
#gniht = thing[::-1]
#print thing, gniht
