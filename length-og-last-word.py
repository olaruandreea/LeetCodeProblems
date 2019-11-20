#Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

#If the last word does not exist, return 0.

#Note: A word is defined as a character sequence consists of non-space characters only.

#Example:
#Input: "Hello World"
#Output: 5
import re

class Solution(object):
    def lengthOfLastWord(self, s):
	containsAlpha = re.search('[a-zA-Z]', s)
        if containsAlpha == None:
            return 0
	elif len(s) == 0:
	    return 0
        else:
            tokens = s.split()
            return len(tokens[-1])
#Test

#test = Solution()     
#print test.lengthOfLastWord("         ") //0
#print test.lengthOfLastWord("andreea") //7 
#print test.lengthOfLastWord("sean") //4
#print test.lengthOfLastWord("engineering") //11
