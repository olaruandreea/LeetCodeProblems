"""
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

 

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: 
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6
"""

class Solution(object):
	def countCharacters(self, words, chars):
		l = []		
		lenghtSum = 0
		temp = chars
		for word in words:
			chars = temp
			boolean = True
			for letter in word:
				if letter in chars:
					chars = chars.replace(letter,"",1)
				else:
					boolean = False
			if boolean == True:
				lenghtSum += len(word)
		return lenghtSum

words = ["hello","world","leetcode"]
chars = "welldonehoneyr"
Test = Solution().countCharacters(words,chars)
print Test
