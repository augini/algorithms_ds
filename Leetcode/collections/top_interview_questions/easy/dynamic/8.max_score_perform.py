class Solution:
    def maximumScore(self, nums: list[int], multipliers: list[int]) -> int:

      def dp(i, l):
         
         if len(multipliers) == i:
            return 0
         
         r = len(nums) - (i - l) -1
         opt_1 = (multipliers[i] * nums[l]) + dp(i+1, l+1)
         opt_2 = (multipliers[i] * nums[r]) + dp(i+1, l)
         
         return max(opt_1, opt_2)
      
      return dp(0, 0)

sample = Solution()
# print(sample.maximumScore([1,2,3], [3,2,1]))
print(sample.maximumScore([-5,-3,-3,-2,7,1], [-10,-5,3,4,6]))

class _Solution:
    def maximumScore(self, nums: list[int], multipliers: list[int]) -> int:
      
      length_num = len(nums)
      length_mult = len(multipliers)
      
      memo = [[-float('inf')] * (length_mult+1) for _ in range(length_mult+1)]
      
      for i in range(length_mult):
         for left in range(i+1):
            if i == 0:
               memo[i][left] = 0
            right = length_num - i + left - 1 
            
            score = memo[i][left]
            memo[i+1][left+1] = max(memo[i+1][left+1], score + nums[left] * multipliers[i])
            memo[i+1][left] = max(memo[i+1][left], score + nums[right] * multipliers[i])

      return max(memo[length_mult]) 