
from collections import Counter


class _Solution:
    def __init__(self):
        self.prime_nums = [2,3]
        
    def countPrimes(self, n: int) -> int:
       counter = 0
       for i in range(2,n):
          if self.isPrime(i):
             self.prime_nums.append(i)
             counter+=1
             
       return counter
    
    def isPrime(self, n):
      if n == 2 or n == 3:
         return True
     
      i = 0
      current = self.prime_nums[i]
      while current*current <= n:
         if n % current == 0:
            return False
         i = i+1
         current = self.prime_nums[i]
         
      return True
   
############### Sieve of Eratosthenes
    
class Solution:
    def countPrimes(self, n: int) -> int:
       nums = list(range(n))
       _len = len(nums)
        
       i = 0
       while i*i < _len and _len > 2:
          i+=1
          val = nums[i]
          
          if val <= 1:
             continue
            
          for j in range(i+i, len(nums), i):
             nums[j] = -1
                
       count = Counter(nums)
       
       return len(nums) - count[-1] - count[0] - count[1] 
   
sample = Solution()
# print(sample.countPrimes(499979))
# print(sample.countPrimes(100))
# print(sample.countPrimes(5))
print(sample.countPrimes(10000)) # 1229
print(sample.countPrimes(10))