class Solution:
    def solve(self, nums):
      result = [1] *len(nums)

      p = 1
      for i in range(len(nums)):
         result[i] *=p
         p *= nums[i]
         
      p = 1
      for i in range (len(nums)-1, -1, -1):
         result[i]*=p
         p*=nums[i]
      return result
      
         
     
sample = Solution()
print(sample.solve([1, 2, 3, 4, 5]))