# Rachel Peterson, 07/08/2020

# calculate factorial method
def factorial(num):
	if (num != 0):
		return num * factorial(num - 1)
	else:
		return 1

# check factorial method
#print(factorial(3))

# calculate the number of different paths 
# from (0, 0) to (n, k) is equal to (n+k // n) = (n+k)! / n!((n+k)! - n)!
def numLatticePaths(n, k): 
	return factorial(n+k) // (factorial(n) * factorial(k))


print(numLatticePaths(20, 20))