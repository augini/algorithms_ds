import math

class Solution:
    def isPrime(self, n: int) -> int:
       if n <= 1: return False
       
       x=2
       while x*x <= n:
          if n % x == 0:
             return False
          x=x+1
          
       return True
   
    def countPrimes(self, n: int) -> int:
       count = 0
       
       for c in range(0, n):
          if self.isPrime(c):
             count = count+1
             
       return count

Sample = Solution()
# print(Sample.countPrimes(0))
print(Sample.countPrimes(10))