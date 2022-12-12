class Solution:
    def isPowerOfThree(self, n: int) -> bool:
       if n <= 0:
          return False
       
       if pow(3,19) % n == 0:
          return True
       return False
     

Sample = Solution()
print(Sample.isPowerOfThree(9))