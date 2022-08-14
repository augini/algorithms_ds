# https://binarysearch.com/room/NullPointerException-R7KRzx6Lcy?questionsetIndex=1

from collections import defaultdict

class Solution:
    dp_table = defaultdict(int)

    def _solve(self, s1, s2):
        if len(s1) == 0 or len(s2) == 0:
            return 0

        if s1[-1] == s2[-1]:
            tpl = tuple([s1, s2])
            rem1, rem2 = s1[:-1], s2[:-1]

            if self.dp_table[tpl]:
                return self.dp_table[tpl]
            else:
                ans = 1 + self.solve(rem1, rem2)
                self.dp_table[tpl] = ans
                return ans
        else:
            tmp1, tmp2 = s1[:-1], s2[:-1]
            tpl1, tpl2 = (tuple([s1, tmp2]), tuple([s2, tmp1]))
            
            if self.dp_table[tpl1] and self.dp_table[tpl2]:
                return max(self.dp_table[tpl1],self.dp_table[tpl2] )
            else:
                res1 = self.solve(s1, s2[:-1])
                res2 = self.solve(s1[:-1], s2)

                self.dp_table[tpl1] = res1
                self.dp_table[tpl2] = res2

                return max(res1, res2)
      
    def solve(self,s1,s2):
       if len(s1) == 0 or len(s2) == 0:
           return 0
           
       dp = [[0 for  i in range(len(s2)+1)] for j in range(len(s1)+1)]
       
       for i in range(0, len(s1)):
          for j in range(0, len(s2)):
            #  print(i, j)
             if s1[i] == s2[j]:
                dp[i][j] = dp[i-1][j-1] + 1
             else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])


       return dp[-2][-2]

sample = Solution()
print(sample.solve("abvce", "bv"))
# print(sample.solve("hbhjwtlpgcyzifxpziwvknmbo", "msvvexligpwzkaekwplxbrlsu"))
