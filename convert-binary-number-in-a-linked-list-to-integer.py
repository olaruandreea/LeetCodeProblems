'''
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
'''
class Solution(object):
    def getDecimalValue(self, head):
        decimalString = ''   
        node = head
        while node:
            decimalString+=str(node.val)
            node = node.next
        i = output = 0 
        for number in decimalString[::-1]:
            output += (int(number) * (2 **i))
            i+=1
        return output
