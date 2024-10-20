class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i, value in enumerate(nums):
            remaining = target - nums[i]
            if remaining in seen:
                return [seen[remaining], i]
            else:
                seen[value] = i
      
    