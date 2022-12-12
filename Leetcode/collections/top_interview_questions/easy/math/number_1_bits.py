from collections import Counter

class Solution:
    def hammingWeight(self, n: int) -> int:
        num = 0
        while n:
            num+=n%2
            n = n >> 1
        return num
     
sample = Solution()
print(sample.hammingWeight(11111111111111111111111111111101))
# print(sample.hammingWeight(00000000000000000000000000001011))
