class Solution:
    def solve(self, n):
      if n == 1: return 1
      
      return n * self.solve(n-1)
         
sample = Solution()
print(sample.solve(3))