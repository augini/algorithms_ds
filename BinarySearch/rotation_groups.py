from collections import defaultdict, Counter
class Solution:
    def solve(self, words):
      length_map = defaultdict(list)
      
      for w in words:
        length_map[frozenset(Counter(w).items())].append(w)
        
      rotation_map = defaultdict(list)
      
      for item in list(length_map.items()):
        current = item[1][0]
        
        for word in item[1]:
          if word in current+current:
            rotation_map[current].append(word)
          else:
            rotation_map[word].append(word)
        
      return len(list(rotation_map.keys()))
     
sample = Solution()
print(sample.solve(["abc", "xy", "yx", "z", "bca"]))