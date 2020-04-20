'''
Given n and m which are the dimensions of a matrix initialized by zeros and given an array indices where indices[i] = [ri, ci]. For each pair of [ri, ci] you have to increment all cells in row ri and column ci by 1.

Return the number of cells with odd values in the matrix after applying the increment to all indices.
Input: n = 2, m = 3, indices = [[0,1],[1,1]]
Output: 6
Explanation: Initial matrix = [[0,0,0],[0,0,0]].
After applying first increment it becomes [[1,2,1],[0,1,0]].
The final matrix will be [[1,3,1],[1,3,1]] which contains 6 odd numbers.
'''
class Solution(object):
    def oddCells(self, n, m, indices):
			matrix = [ [ 0 for i in range(m) ] for j in range(n) ] 
			i = 0
			row = []
			columns = []
			while i < len(indices):
				row.append(indices[i][0])
				columns.append(indices[i][1])
				i+=1

			i = 0 
			while i < len(row):
				j = 0 
				while j < len(matrix[row[i]]):
					matrix[row[i]][j] = str(int(matrix[row[i]][j]) + 1) 
					j+=1
				i+=1
			
			i = 0
			while i < len(columns):
				for each in matrix:
					each[columns[i]] = int(each[columns[i]]) +1
				i+=1
			
			odd = 0
			for each in matrix:
				i = 0
				while i < len(each):
					if int(each[i]) % 2 != 0:
						odd +=1
					i+=1
			return odd
n = 2
m = 3
indices =   [[0,1],[1,1]]
Test = Solution().oddCells(n,m, indices)
print Test
