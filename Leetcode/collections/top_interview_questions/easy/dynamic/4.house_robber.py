class Solution:
    def rob(self, nums: list[int]) -> int:
        
        if len(nums) == 1:
           return nums[0]
        elif len(nums) == 2:
           return nums[0] if nums[0] > nums[1] else nums[1]
                       
        profits = [nums[0], nums[1], nums[0]+nums[2]]
        
        for num in range (3, len(nums)):
           _gain = max(profits[num-2], profits[num-3]) + nums[num]
           profits.append(_gain)
       
        return max(profits)