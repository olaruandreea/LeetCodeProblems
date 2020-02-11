"""
We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words. 

You may return the list in any order.

 

Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]
"""


class Solution(object):
    def uncommonFromSentences(self, A, B):
        tokens1 = A.split(" ")
	tokens2 = B.split(" ")
	l = []
	for word in tokens1:
		if word not in tokens2 and tokens1.count(word) == 1:
			l.append(word)
	for word in tokens2:
		if word not in tokens1 and tokens2.count(word) == 1:
			l.append(word)
	return l

A = "apple apple"
B = "banana"
print Solution().uncommonFromSentences(A, B)
