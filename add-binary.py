#Given two binary strings, return their sum (also a binary string).
#The input strings are both non-empty and contains only characters 1 or 0.
#Example 1:


class Solution(object):
    def addBinary(self, a, b):
       return (bin(int(a,2) + int(b,2))).split("b")[1]

Test= Solution()
print Test.addBinary("11","1")
        
