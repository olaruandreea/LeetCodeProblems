'''
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.

 

Example 1:

Input: [1,2,3,3]
Output: 3
'''

class Solution(object):
    def repeatedNTimes(self, A):
        d = {}
        for each in A:
            if each not in d:
                d[each] = 1
            else:
                d[each] += 1
        return (max(d, key=d.get))

A = [1,2,3,3]
Test = Solution().repeatedNTimes(A)
print Test
