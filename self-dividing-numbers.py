'''
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
'''

class Solution(object):
    def selfDividingNumbers(self, left, right):
        l = []
        for i in range(left,right+1):
            if '0' not in str(i):
                for each in str(i):
                    if int(i) % int(each) == 0:
                        boolean = True
                    else:
                        boolean = False
                        break
                if boolean == True:
                    l.append(i)
        return l

left = 10
right = 23
Test = Solution().selfDividingNumbers(left,right)
print Test
