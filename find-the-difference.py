"""
Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:

Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.
"""
class Solution(object):
    def findTheDifference(self, s, t):
        for letter in t:
            if letter not in s:
                return letter
            if letter in s and s.count(letter) != t.count(letter):
                return letter


s = "abcd"
t = "abcde"
print Solution().findTheDifference(s,t)
