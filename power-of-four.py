import math 
class Solution(object):
    def isPowerOfFour(self, n):
	if n == 0:
		return False
	while n != 1:
		if n % 4 != 0:
			return False
		n = n / 4
	return True 

Test = Solution()
print Test.isPowerOfFour(4096)
