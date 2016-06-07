def fact(m):
	if(m == 0):
		return 1
	else:
		return(m * fact(m-1))
print(fact(5))
