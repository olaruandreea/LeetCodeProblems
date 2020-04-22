'''
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

 

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
'''
import string
class Solution(object):
    def commonChars(self, A):
		i = 0
		d = {}
		while i < len(A):
			for char in string.ascii_lowercase:
				if str(char) in A[i]:
					if str(char) not in d:
						d[char] = [1,[A[i].count(str(char))]]
					else:
						d[char][0] +=1
						d[char][1].append(A[i].count(str(char)))
			i+=1	
		output = []
		for key,value in d.items():
			if int(value[0]) == len(A):
				i = 0					
				while i < min(value[1][0:]):
					output.append(key)
					i+=1
			
		return output
A = ["bella","label","roller"]
Test = Solution().commonChars(A)
print Test
