'''
Given an integer number n, return the difference between the product of its digits and the sum of its digits
Example 1:
Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15
'''

def read_input(s):
	product = 1
	sumNumber = 0 
	lista = []
	for each in s:
		product *= int(each)
		sumNumber+= int(each)
	lista.append(product)
	lista.append(sumNumber)
	return int(lista[0])-int(lista[1])

s = raw_input()
print read_input(s)
