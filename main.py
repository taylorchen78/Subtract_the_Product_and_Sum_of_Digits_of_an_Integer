"""
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
"""

def subtractProductAndSum(num):
	numList = [int(x) for x in str(num)]
	print(numList)

	numProduct = 1
	numSum = 0

	for num in numList:
		numProduct *= num
		numSum += num

	return numProduct-numSum

print(subtractProductAndSum(234))
print(subtractProductAndSum(4421))