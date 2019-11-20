###Given a 32-bit signed integer, reverse digits of an integer.
#Example 1:
#Input: 123
#Output: 321

class Solution: 
    def reverse(self, number):
        reverseNumber = str(number)[::-1]
        if number == 0:
            return 0
        elif reverseNumber[len(reverseNumber)-1] == "+":
            return "+" + reverseNumber[0:len(reverseNumber)-1]
        elif reverseNumber[len(reverseNumber)-1] == "-":

            return "-" + reverseNumber[0:len(reverseNumber)-1]
        elif int(reverseNumber[0]) == int(0):
            return reverseNumber[1:]
        else:
            return reverseNumber
number = raw_input()
output = Solution()
print output.reverse(number)
