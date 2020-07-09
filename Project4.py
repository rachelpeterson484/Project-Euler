# Rachel Peterson, 07/08/2020
# calculate the largest palindrome made from the product of two 2-diti numbers (ex: 9009 = 91 x 99)

import math

# checks whether a number is a palindrome, returns true if is a palindrome
def checkPal(num):

	# convert num to list of integers
	numList = list(map(int, str(num)))
	# checks the first half digits to the second half digits
	digitsToCheck = math.floor(len(numList)/2)

	palindrome = True
	i = 0
	
	while (i < digitsToCheck and palindrome == True):
		if not(numList[i] == numList[len(numList)-i-1]):
			palindrome=False
		i += 1

	return palindrome

# find the largest 3-digit palindrome product
def findLargest():
	largest = 0
	for x in range(100, 1000):
		for y in range(100, 1000):
			if (x*y) > largest and checkPal(x*y):
				largest = x*y
	return largest


print(findLargest())

# check palindrom method by from 1 to 1000
#start = 1
#for start in range(1000):
#	print(start, " ", checkPal(start))

