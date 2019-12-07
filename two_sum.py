class Solution(object):
	def twoSum(self, nums, target):
		list_input = sorted(nums)
		l = 0 
		r = len(list_input)-1
		output = []
		while int(l) < int(r):
			if int(list_input[l]) + int(list_input[r]) == int(target): 
				output.append(nums.index(list_input[l]))
				nums[nums.index(list_input[l])] = 0.12
				print nums
				output.append(nums.index(list_input[r]))
				return output
			elif int(list_input[l]) + int(list_input[r]) < int(target):
				l +=1
			else:
				r -=1
			
		


nums = [3,3]
target = 6
Test = Solution()
print(Test.twoSum(nums,target))
