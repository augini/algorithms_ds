class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
       unique = set(nums)
       
       return len(unique) != len(nums) 


sample = Solution()
print(sample.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))