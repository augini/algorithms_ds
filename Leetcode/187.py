# https://leetcode.com/problems/repeated-dna-sequences/description/
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        temp, res = set(), set()
        l = len(s)

        for i in range(l - 9):
            sub = s[i : i + 10]

            if sub in temp:
                res.add(sub)

            temp.add(sub)

        return list(res)
