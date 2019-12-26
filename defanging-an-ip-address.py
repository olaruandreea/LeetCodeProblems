"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".
Example 1:
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
"""

class Solution(object):
    def defangIPaddr(self, address):
        for character in address:
		if character == ".":
			new = address.replace(character,"[.]")
	return new




address = raw_input()
Test = Solution().defangIPaddr(address)
print Test
