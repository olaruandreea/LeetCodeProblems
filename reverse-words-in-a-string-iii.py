'''
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
'''
class Solution(object):
    def reverseWords(self, s):
	tokens = s.split()
	outputList = []
	for each in tokens:
		outputList.append(each[::-1])
	return ' '.join(outputList)


s = "Let's take LeetCode contest"
Test = Solution().reverseWords(s)
print Test
