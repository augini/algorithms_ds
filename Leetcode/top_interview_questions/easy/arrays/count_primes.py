
from collections import Counter


class Solution:
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
    
class _Solution:
    def countPrimes(self, n: int) -> int:
       nums = list(range(n))
       
       for i, val in enumerate(nums, 2):
          if val == -1:
             continue

          for j in range(i+i, len(nums), i):
            #  print(j, nums[j])
             nums[j] = -1
      #  print(nums)
       count = Counter(nums)
       return len(nums) -count[-1] - count[0] - count[1] 
   
sample = _Solution()
# print(sample.countPrimes(499979))
print(sample.countPrimes(10))
# print(sample.countPrimes(5))
