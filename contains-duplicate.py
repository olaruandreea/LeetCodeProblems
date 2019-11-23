'''
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
'''

class Solution(object):
    def containsDuplicate(self, nums):
	l = sorted(nums)        
	for i in range(0, len(l)-1):
		if l[i] == l[i+1]:
			return True
	return False

###Test = Solution()
###print Test.containsDuplicate(["12","2"])
