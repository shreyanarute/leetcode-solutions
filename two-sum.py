class Solution:
    def twoSum(self, nums, target):
        
        # Check every possible pair
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                
                # If pair sum equals target
                if nums[i] + nums[j] == target:
                    return [i, j]
