from collections import defaultdict, Counter


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
      result = defaultdict(list)
      
      # time complexity is n * m * log(m)
      # for str in strs:
      #    _sorted = "".join(sorted(str))
      #    result[_sorted].append(str)

   
     # we can bring it down this time complexity to n * m
     
      for str in strs:
         _keys = frozenset(Counter(str).items())
         result[_keys].append(str)
         
      return list(result.values())

     
sample = Solution()
print(sample.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))