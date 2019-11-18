###Given a 32-bit signed integer, reverse digits of an integer.
#Example 1:
#Input: 123
#Output: 321

def reverseNumber(number):
    reverse = number[::-1]
    if reverse[len(reverse)-1] == "+":
        return "+" + reverse[0:len(reverse)-1]
    elif reverse[len(reverse)-1] == "-":
        return "-" + reverse[0:len(reverse)-1]
    elif int(reverse[0]) == int(0):
        return reverse[1:]
    else:
        return reverse
number = raw_input()
print reverseNumber(number)