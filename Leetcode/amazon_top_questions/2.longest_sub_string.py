class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # handle edge cases  
        if len(s) == 0:
           return 0
        elif len(s) == 1:
           return 1
        
        max_length = 1
        fast, slow = 1, 0
        
        while fast < len(s):
           substring = s[slow:fast]
           
           if s[fast] not in substring:
              
              if fast == len(s) - 1:
                 return fast - slow + 1
              
              fast=fast+1
              
           elif s[fast] in substring:
              length = len(substring)
              
              if length > max_length:
                 max_length = length
                 
              slow = slow + 1
        
        return max_length

Sample = Solution()
# print(Sample.lengthOfLongestSubstring("pwwkew"))
# print(Sample.lengthOfLongestSubstring("dvdf"))
# print(Sample.lengthOfLongestSubstring("bbbb"))
print(Sample.lengthOfLongestSubstring(" "))

