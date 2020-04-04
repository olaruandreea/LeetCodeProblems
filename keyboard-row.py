class Solution(object):
	def findWords(self, words):
		raw1 = "QWERTYUIOPqwertyuiop"
		raw2 = "ASDFGHJKLasdfghjkl"
		raw3 = "ZXCVBNMzxcvbnm"
		outputList = []
		for word in words:
			count1 = count2 = count3 = 0
			for letter in word:
				if letter in raw1:
					count1+=1
				elif letter in raw2:
					count2+=1
				elif letter in raw3:
					count3+=1	
			if count1 == len(word) or count2 == len(word) or count3 == len(word):
				outputList.append(word)
		return outputList


words = ["Hello", "Alaska", "Dad", "Peace"]
Test = Solution().findWords(words)
print Test
