# https://leetcode.com/problems/permutation-in-string/description/?envType=study-plan&id=algorithm-i
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1 = sorted(s1)
        l1, l2 = len(s1), len(s2)

        for i in range(0, l2 - l1 + 1):
            temp = sorted(s2[i : i + l1])
            if s1 == temp:
                return True

        return False

    def _checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        c1, c2 = Counter(s1), Counter(s2[0:l1])

        for i in range(0, l2 - l1):
            if c1 == c2:
                return True

            # print(s2[i:i+l1], c2, s2[i], s2[i+l1])
            c2[s2[i]] -= 1
            c2[s2[i + l1]] += 1

        if c1 == c2:
            return True

        return False
