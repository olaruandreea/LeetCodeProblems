class Solution(object):
    def removeElement(self, nums, val):
        nums[:] = [x for x in nums if int(x) != int(val)]
        return len(nums)

nums =  [1,4,3,3,3,4]
val = 4
Test = Solution().removeElement(nums,val)
print Test
