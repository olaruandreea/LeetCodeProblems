class Solution(object):
    def removeElement(self, nums, val):
        return [x for x in nums if int(x) != int(val)]

nums =  [3,2,2,3]
val = 3
Test = Solution().removeElement(nums,val)
print Test
