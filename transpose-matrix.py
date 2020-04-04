"""
Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.
"""
class Solution(object):
    def transpose(self, A):
		output = []
		l = []		
		i = 0 
		while i < len(A[0]):
			for raw in A:
				l.append(str(raw[i]))
			output.append(l)
			l = []
			i+=1
		return output
A = [[1,2,3],[4,5,6],[7,8,9]]
Test = Solution().transpose(A)
print Test
