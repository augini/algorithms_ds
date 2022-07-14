class Solution:
    def solve(self, n):
      if n == 0:
         return "0"
      
      result = ""
      
      while n > 0:
         remainder = n % 3
         result += str(remainder)
         n //= 3
      result = result[::-1]
      return result
     
sample = Solution()
print(sample.solve(7))