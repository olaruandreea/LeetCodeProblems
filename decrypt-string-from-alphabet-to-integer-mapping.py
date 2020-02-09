"""
Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively. 
Return the string formed after mapping.

It's guaranteed that a unique mapping will always exist.

 

Example 1:

Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
"""

import string
class Solution(object):
    def freqAlphabets(self, s):
	i = 0 
	j = 1
	d = {}
	while i < 9:
		d[j] = string.ascii_lowercase[i]
		j+=1
		i+=1	
	i = 9
	j = 10
	while i < len(string.ascii_lowercase):
		d[str(j) + "#"] = string.ascii_lowercase[i]
		j+=1
		i+=1	

	i = 0
	outputString = ""
	while i < len(s):
		if i + 2 < len(s) and s[i+2] == "#":
			outputString += d[s[i:i+3]]			
			i+=3
		else:
			 
			outputString += d[int(s[i])]	
			i+=1
	return outputString
s = raw_input()
Test = Solution().freqAlphabets(s)
print Test



