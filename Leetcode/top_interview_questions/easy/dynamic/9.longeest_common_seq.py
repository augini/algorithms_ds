
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
      count = [0*len(text1)][0*len(text2)]
         
      return 0
     
sample = Solution()
# print(sample.longestCommonSubsequence("abc", "def"))
# print(sample.longestCommonSubsequence("abcde", "ace"))
# print(sample.longestCommonSubsequence("abc", "abc"))
print(sample.longestCommonSubsequence("oxcpqrsvwf", "shmtulqrypy"))