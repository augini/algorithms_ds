class Solution:
   def solve(self, deadlines, credits):
      a = sorted(list(zip(deadlines, credits)), key=lambda x: x[1], reverse=True)
      if not a:
         return 0
      res = [0] * (max(deadlines) + 1)
      ans = 0
      for i, j in a:
         for k in range(i, -1, -1):
            if not res[k]:
               res[k] = 1
               ans += j
               break
      return ans

ob = Solution()
deadlines = [1, 2, 2, 2]
credits = [4, 5, 6, 7]
print(ob.solve(deadlines, credits))