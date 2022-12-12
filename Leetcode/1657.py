# https://leetcode.com/problems/determine-if-two-strings-are-close/
from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        if len(word1) != len(word2):
            return False

        c1, c2 = Counter(word1), Counter(word2)

        c1_occ, c1_chars = sorted(list(c1.keys())), sorted(list(c1.values()))
        c2_occ, c2_chars = sorted(list(c2.keys())), sorted(list(c2.values()))

        # print(c1_occ, c2_occ)

        if c1_occ == c2_occ and c1_chars == c2_chars:
            return True
        return False
