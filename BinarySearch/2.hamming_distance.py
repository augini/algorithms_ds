class Solution:
    def solve(self, x, y):
      answer = 0
      for i in range(31,-1,-1):
         b1 = x>>i&1
         b2 = y>>i&1
         answer += not(b1==b2)
      return answer
         
sample = Solution()
print(sample.solve(5,9))