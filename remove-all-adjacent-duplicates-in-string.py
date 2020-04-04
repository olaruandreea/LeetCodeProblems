"""
Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.

 

Example 1:

Input: "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
"""

import string
class Solution(object):
	def removeDuplicates(self, S):
		alpha = string.ascii_lowercase
		letters = []       
		for each in alpha:
			letters.append(2*each)
		i = 0
		while i < len(letters):
			if letters[i] in S:
				S = S.replace(letters[i],"")
				i = 0
			else:
				i+=1		
		return S			

			
S =  "aadbbaca"
Test = Solution().removeDuplicates(S)
print Test



