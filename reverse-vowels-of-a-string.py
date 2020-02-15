"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
"""

class Solution(object):
    def reverseVowels(self, s):
        vowelsList = ["a","A","e","E","i","I","o","O","u","U"]
	vowelsInString = []
	for letter in s:
		if letter in vowelsList:
			vowelsInString.append(letter)
	i = 0 
	j = 0
	t = ""
	while i < len(s):
		if s[i] not in vowelsList:
			t+=s[i]
			i+=1
		else:
			t += vowelsInString[::-1][j]
			j+=1
			i+=1
	return t
s = "hello"
print Solution().reverseVowels(s)
