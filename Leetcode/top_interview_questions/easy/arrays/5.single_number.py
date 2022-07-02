class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for x in nums:
           result = result ^ x
        return result
     
sample = Solution()
print(sample.singleNumber([4,1,2,1,2]))