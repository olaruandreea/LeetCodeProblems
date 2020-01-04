'''
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed

Example 1:
Input: text = "nlaebolko"
Output: 1
'''

class Solution(object):
    def maxNumberOfBalloons(self, text):
        d = {}
    	for i in text:
       		d[i] = d.get(i,0)+1
	try:
	    	minimum_b_a_or_n = min(d['b'],d['a'],d['n']) 
		minimum_l_o =  (min(d['l'],d['o']) / 2)
		return min(minimum_b_a_or_n,minimum_l_o)
	except KeyError:
		return 0

	

text = "balloonsballoonsballoonssassssaaaaaaaaaaaaaaaaaaa"

Test = Solution().maxNumberOfBalloons(text)
print (Test)



