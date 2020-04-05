"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.


Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
The above arrows point to positions where the corresponding bits are different.
"""

class Solution(object):
	def hammingDistance(self, x, y):
		binaryX = []
		binaryY = []
		while x != 0:
			remainder = x % 2
			binaryX.append(remainder)
			x = x / 2	
		while y != 0:
			remainder = y % 2
			binaryY.append(remainder)
			y = y / 2
		if len(binaryX) < len(binaryY):
			while len(binaryX) != len(binaryY):
				binaryX.append(0)
		elif len(binaryY) < len(binaryX):
			while len(binaryY) != len(binaryX):
				binaryY.append(0)
		j  = 0 
		count = 0 
		while j < len(binaryX):
			if binaryX[j] != binaryY[j]:
				count +=1
			j+=1
		return count 
x = 1
y = 4
Test = Solution().hammingDistance(x,y)
print Test
