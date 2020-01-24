"""
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cba" can be written as "-.-..--...", (which is the concatenation "-.-." + "-..." + ".-"). We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.

Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation: 
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."
There are 2 different transformations, "--...-." and "--...--.".
"""

class Solution(object):
	# Create dictionary with all alphabet letters and the input data
	def CreateDictionary(self):
		data = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
		test_list = [chr(x) for x in range(ord('a'), ord('z') + 1)] 
		d = {}
		i = 0 
		while i < len(test_list):
			d[test_list[i]] = data[i]
			i+=1
		return d

	# Return the number of different transofrmations
	def uniqueMorseRepresentations(self,words):
		d = self.CreateDictionary()
		string = "" 
		lista = []
		for word in words:
			for letter in word:
				string += d[letter]
			lista.append(string)
			string = ""
		return len(set(lista))


#words = ["gin", "zen", "gig", "msg"]
#Test = Solution().uniqueMorseRepresentations(words)
#print Test
