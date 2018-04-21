def multiarg(*args):
	result = 0
	for x in args:
		result=result+x
	return result
	
print(multiarg(10,20,30))