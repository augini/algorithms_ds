class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
       
       current_sum = 0
       max_sum = nums[0]
       
       for num in nums:
          current_sum = current_sum + num
          
          if current_sum >= max_sum:
             max_sum = current_sum
             
          if current_sum < 0:
             current_sum = 0
             
       return max_sum
    
    
Sample = Solution()
# print(Sample.maxSubArray([5,4,-1,7,8]))
print(Sample.maxSubArray([-1]))
