class Solution:
    def solve(self, nums):
        result = self.helper(nums, 1)
        return result
    
    def helper(self, nums, i):
        if i >= len(nums):
            return 0
        
        return 2 * abs(nums[i] - nums[i-1]) + self.helper(nums, i+1)
            


sample = Solution()
print(sample.solve([1, 3, 6]))

