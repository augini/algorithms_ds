class Solution:
    def rob(self, nums: list[int]) -> int:
        
        if len(nums) == 1:
           return nums[0]
        elif len(nums) == 2:
           return nums[0] if nums[0] > nums[1] else nums[1]
                       
        profits = [nums[0], nums[1], nums[0]+nums[2]]
        _max = max(profits)
        
        for num in range (3, len(nums)):
           if profits[num - 2] > profits[num-3]:
              _gain = profits[num-2] + nums[num]
              profits.append(_gain)
              
           elif profits[num - 2] <= profits[num-3]:
              _gain = profits[num-3] + nums[num]
              profits.append(_gain)
            
           if _gain > _max:
              _max = _gain
       
        return _max
     
Sample = Solution()

# print(Sample.rob([1,2,3,1]))
# print(Sample.rob([0,9,12]))
# print(Sample.rob([2,1,1,2]))
# print(Sample.rob([2,7,9,3,1]))
