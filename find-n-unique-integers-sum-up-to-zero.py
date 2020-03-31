'''
Given an integer n, return any array containing n unique integers such that they add up to 0.

 

Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
Example 2:

Input: n = 3
Output: [-1,0,1]
'''
class Solution(object):
    def sumZero(self, n):
        array = []
        if n ==  0:
            return [0]
        if n ==  1:
            return [0]
        for i in range(1,(n/2)+1):
            array.append(int(i))
            array.append(-int(i))
        if n % 2 != 0:
            array.append(0)
        return array
        

n = 2
Test = Solution().sumZero(n)
print Test
