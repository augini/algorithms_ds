class Solution:
    def solve(self, n):
        primes = []
        for i in range(2, n+1):
           if self.isPrime(i):
              primes.append(i)
        return primes
     
    def isPrime(self, n):
       if n == 2 or n == 3:
          return True
       
       x = 2
       while x*x <= n:
          if n % x == 0:
             return False
          x+=1
          
       return True
    
     
sample = Solution()
print(sample.solve(10))