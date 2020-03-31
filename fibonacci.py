'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).

 

Example 1:

Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
'''

class Solution(object):
    def fibonnaci(self, N):
        if int(N) == 0:
            return 0
        elif int(N) == 1:
            return 1
        else:
            return Solution().fibonnaci(N -1) + Solution().fibonnaci(N-2) 


N = 5
Test = Solution().fibonnaci(N)
print Test