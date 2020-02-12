"""
Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

 

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
"""
class Solution(object):
	def uniqueOccurrences(self, arr):
		dictionary = {}
		for each in arr:
			if each not in dictionary:
				dictionary[each] = 1
			else:
				dictionary[each] += 1
		listOfKeys = []
		for key,value in dictionary.items():
			if value not in listOfKeys:
				listOfKeys.append(value)
			else:
				return False 
		return True



arr = [1,2]
print Solution().uniqueOccurrences(arr)
