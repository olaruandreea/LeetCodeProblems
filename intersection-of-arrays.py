'''
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
'''


class Solution(object):
    def intersection(self, nums1, nums2):
        output = [x for x in set(nums1) if x in set(nums2)]
	return output
        
#TestOutput = Solution()
#nums1 = [3,1,2,2,1]
#nums2 = [2,3,2]
#print TestOutput.intersection(nums1,nums2)
