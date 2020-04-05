'''
Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
 

Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.
'''
class Solution(object):
    def shortestToChar(self, S, C):
		output = []
		new = []
		i = 0 
		while i < len(S):
			if S[i] == C:
				output.append("0")
			elif S[i] != C:
				rightHandSide = S[i:]	
				leftHandSide = S[:i+1]	
				j = 0 
				count1 = 0  
				if C in rightHandSide:
					while rightHandSide[j] != C:
						count1 +=1
						j+=1
				if count1 != 0:
					new.append(count1)
				j2 = len(leftHandSide) -1 
				count2 = 0  
				if C in leftHandSide:
					while leftHandSide[j2] != C:
						count2 +=1
						j2 = j2 - 1
				if count2 != 0 :
					new.append(count2)
				output.append(min(new))
				new = []
			i+=1
		return output
        

S = "aaba"
C = 'b'
Test = Solution().shortestToChar(S,C)
print Test
