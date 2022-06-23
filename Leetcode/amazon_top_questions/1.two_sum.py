
# two sum in O(n) time

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
      container = {}
      
      for i in range (0, len(nums)):
         toTarget = target - nums[i]
         
         if toTarget in container:
            return [container[toTarget], i]
         
         container[nums[i]] = i
     
Sample = Solution()
print(Sample.twoSum([2,7,11,15], 9))