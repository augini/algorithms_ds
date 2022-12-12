# https://leetcode.com/problems/sort-characters-by-frequency/
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)

        s = sorted(c.items(), key=lambda pair: pair[1], reverse=True)
        result = ""
        for pair in s:
            result = result + str(int(pair[1]) * pair[0])
        return result
