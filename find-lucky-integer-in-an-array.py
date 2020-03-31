"""
Given an array of integers arr, a lucky integer is an integer which has a frequency in the array equal to its value.

Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. If there is no lucky integer return -1.

 

Example 1:

Input: arr = [2,2,3,4]
Output: 2
Explanation: The only lucky number in the array is 2 because frequency[2] == 2.

"""

class Solution(object):
    def findLucky(self, arr):
        d = {}
        output = []
        for each in arr:
            if int(each) not in d:
                d[int(each)] = 1
            else:
                d[int(each)] += 1 
        for key,val in d.items():
            if int(key) == int(val):
                output.append(int(key))
        if len(output) == 0:
            return -1
        else:
            return max(output)


arr = []
Test = Solution().findLucky(arr)
print Test     
