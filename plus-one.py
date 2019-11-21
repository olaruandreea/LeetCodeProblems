class Solution(object):
    def plusOne(self, digits):
	i = 0 
	outputList = []
	while i < (len(digits)):
		if i == (len(digits))-1:
			increment = (int(digits[i]) + 1)
			if increment > 9:
				outputList.append(str(increment)[0])
				outputList.append(str(increment)[1])
			else:
				outputList.append(int(digits[i]) + 1)
		else:
			outputList.append(digits[i])
		i+=1 
	return outputList

Test = Solution()
print Test.plusOne(["1","2","3","9"])
        
