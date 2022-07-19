# https://binarysearch.com/problems/Minimum-String
from collections import Counter

class Solution:
    def solve(self, s, t):
        s_map = Counter(s)
        t_map = Counter(t)

        changes = 0
        
        for item in t_map.keys():
            s_item = s_map[item]
            t_item = t_map[item]

            if s_item != t_item:
                if t_item > s_item:
                    changes+=abs(t_item - s_item)
                
        return changes