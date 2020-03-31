'''
Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 

Return the number of negative numbers in grid.

 

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
'''
class Solution(object):
    def countNegatives(self, grid):
        count  = 0 
        for row in grid:
            for element in row:
                if int(element) < 0:
                    count += 1
        return count        

grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Test = Solution().countNegatives(grid)
print Test

