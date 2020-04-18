"""
Given a string s. You should re-order the string using the following algorithm:
Pick the smallest character from s and append it to the result.
Pick the smallest character from s which is greater than the last appended character to the result and append it.
Repeat step 2 until you cannot pick more characters.
Pick the largest character from s and append it to the result.
Pick the largest character from s which is smaller than the last appended character to the result and append it.
Repeat step 5 until you cannot pick more characters.
Repeat the steps from 1 to 6 until you pick all characters from s.
In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

Return the result string after sorting s with this algorithm.
"""
import string
class Solution(object):
	def sortString(self, s):
		dictionary = {}
		for letter in s:
			if letter in dictionary.keys():
				dictionary[letter] += int(1)
			else:
				dictionary[letter] = int(1)

		print dictionary
		condition = all(value == 0 for value in dictionary.values())
		'''		
		False
		'''
		newString = ""
		while condition != True:
			for character in string.ascii_lowercase:
				if character in dictionary and dictionary[character] >= 1:
					newString += character
					dictionary[character] -= 1						
			for character in string.ascii_lowercase[::-1]:
				if character in dictionary and dictionary[character] >= 1:
					newString += character
					dictionary[character] -= 1	
			condition = all(value == 0 for value in dictionary.values())
		return newString
        


s = "rat"
Test = Solution().sortString(s)
print Test
